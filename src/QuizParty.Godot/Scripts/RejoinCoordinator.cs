using Godot;
using QuizParty.Networking;

namespace QuizParty.Presentation;

/// <summary>Scene-owned prompt and retry worker for the device's previous match.</summary>
public partial class RejoinCoordinator : Node
{
    private RejoinStore _store = null!;
    public RejoinStore? StoreOverride { get; set; }
    public bool EnableForTests { get; set; }
    private MatchDialog _dialog = null!;
    private Label _message = null!;
    private Node? _networkRoot;
    private SceneMultiplayer? _networkApi;
    private LobbyTransport? _delivery;
    private RejoinTicket? _delivering;
    private bool _working;

    public override void _Ready()
    {
        if (!EnableForTests && OS.IsDebugBuild() && (System.Environment.GetEnvironmentVariable("EnableGodotTests") == "true" ||
            MatchProcessProbe.LaunchArguments().Any(a => a.StartsWith("--ui-", StringComparison.Ordinal) || a.StartsWith("--match-", StringComparison.Ordinal)))) return;
        _store = StoreOverride ?? RejoinStore.Device();
        var layer = new CanvasLayer { Name = "RejoinLayer", Layer = 50 }; AddChild(layer);
        _dialog = new MatchDialog { Name = "RejoinPrompt" }; layer.AddChild(_dialog);
        _message = new Label { Text = "REJOIN_PROMPT", AutowrapMode = TextServer.AutowrapMode.WordSmart };
        _dialog.Body.AddChild(_message);
        var yes = new Button { Text = "REJOIN_YES", Name = "Rejoin", ThemeTypeVariation = "PrimaryAction", CustomMinimumSize = new(0, 64), SizeFlagsHorizontal = Control.SizeFlags.ExpandFill };
        var no = new Button { Text = "REJOIN_NO", Name = "Leave", CustomMinimumSize = new(0, 64), SizeFlagsHorizontal = Control.SizeFlags.ExpandFill };
        _dialog.Actions.AddChild(yes); _dialog.Actions.AddChild(no);
        yes.Pressed += Rejoin; no.Pressed += Leave;
        if (!GetTree().HasMeta("rejoin_navigation") && _store.Load() is not null)
        { _dialog.Show(); yes.GrabFocus(); }
        var timer = new global::Godot.Timer { WaitTime = 10, Autostart = true }; AddChild(timer);
        timer.Timeout += TryPending;
        Callable.From(TryPending).CallDeferred();
    }

    private void Rejoin()
    {
        if (_store.Load() is not { } ticket) { _dialog.Hide(); return; }
        _dialog.Hide();
        var tree = GetTree();
        if (tree.CurrentScene is LobbyScreen lobby) { lobby.ResumePrevious(ticket); return; }
        tree.SetMeta("rejoin_navigation", true);
        void Arrived()
        {
            tree.SceneChanged -= Arrived; tree.RemoveMeta("rejoin_navigation");
            if (tree.CurrentScene is LobbyScreen destination) destination.ResumePrevious(ticket);
        }
        tree.SceneChanged += Arrived;
        var error = tree.ChangeSceneToFile("res://Scenes/Lobby.tscn");
        if (error != Error.Ok)
        {
            tree.SceneChanged -= Arrived; tree.RemoveMeta("rejoin_navigation");
            _message.Text = "REJOIN_FAILED"; _dialog.Show();
            GD.PushWarning($"Rejoin navigation failed: {error}");
        }
    }

    private void Leave()
    {
        try
        {
            if (_store.Load() is { } ticket) _store.QueueDeparture(ticket);
            _dialog.Hide(); TryPending();
        }
        catch (Exception error) when (error is IOException or UnauthorizedAccessException or InvalidOperationException or System.Text.Json.JsonException)
        { GD.PushWarning($"Departure could not be saved: {error.GetType().Name}"); _message.Text = "REJOIN_SAVE_FAILED"; }
    }

    private void TryPending()
    {
        if (_working || !IsInsideTree()) return;
        try { _delivering = _store.Pending().FirstOrDefault(); }
        catch (Exception storageError) when (storageError is IOException or UnauthorizedAccessException or System.Text.Json.JsonException)
        { GD.PushWarning($"Pending departure could not be read: {storageError.GetType().Name}"); return; }
        if (_delivering is null) return;
        _working = true;
        _networkRoot = new Node { Name = "DepartureNetwork" }; AddChild(_networkRoot);
        _networkApi = new SceneMultiplayer(); GetTree().SetMultiplayer(_networkApi, _networkRoot.GetPath());
        // The normal host scene resolves RPCs at Lobby/Transport relative to /root.
        var lobby = new Node { Name = "Lobby" }; _networkRoot.AddChild(lobby);
        _delivery = new LobbyTransport { Name = "Transport" }; lobby.AddChild(_delivery);
        _delivery.StatusChanged += OnDeliveryStatus;
        var error = _delivery.DeliverDeparture(_delivering);
        if (error != Error.Ok) EndDelivery(false);
    }

    private void OnDeliveryStatus(string status)
    {
        if (status == "DepartureDelivered") Callable.From(() => EndDelivery(true)).CallDeferred();
        else if (status == "DepartureRetry") Callable.From(() => EndDelivery(false)).CallDeferred();
    }
    private void EndDelivery(bool delivered)
    {
        if (!_working) return;
        if (delivered && _delivering is { } ticket)
        {
            try { _store.RemovePending(ticket); }
            catch (Exception error) when (error is IOException or UnauthorizedAccessException or System.Text.Json.JsonException)
            { GD.PushWarning($"Departure receipt could not be saved: {error.GetType().Name}"); }
        }
        _working = false; _delivering = null;
        var root = _networkRoot; var api = _networkApi; _networkRoot = null; _networkApi = null; _delivery = null;
        if (root is not null && GodotObject.IsInstanceValid(root))
        {
            var path = root.GetPath();
            root.Free();
            GetTree().SetMultiplayer(null!, path);
        }
        api?.Dispose();
    }
    public override void _ExitTree()
    {
        if (_working) EndDelivery(false);
    }
}
