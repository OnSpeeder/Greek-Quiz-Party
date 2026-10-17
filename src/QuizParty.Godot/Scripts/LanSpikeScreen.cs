using Godot;
using QuizParty.Networking;

namespace QuizParty.Presentation;

public partial class LanSpikeScreen : Control
{
    private LanSpikeTransport _transport = null!;
    private LineEdit _address = null!;
    private Label _status = null!;
    private Label _receipt = null!;
    private Button _send = null!;
    private bool _automatic;
    private int _acks;

    public override void _Ready()
    {
        const string content = "Margin/Scroll/Content/";
        _transport = GetNode<LanSpikeTransport>("Transport");
        _address = GetNode<LineEdit>(content + "Address");
        _status = GetNode<Label>(content + "Status");
        _receipt = GetNode<Label>(content + "Receipt");
        _send = GetNode<Button>(content + "Send");
        GetNode<Button>(content + "Host").Pressed += () => ShowResult(_transport.Host());
        GetNode<Button>(content + "Join").Pressed += () => ShowResult(_transport.Join(_address.Text));
        GetNode<Button>(content + "Disconnect").Pressed += () =>
        {
            _transport.Stop();
            _status.Text = Tr("SPIKE_IDLE");
        };
        GetNode<Button>(content + "Back").Pressed += () => GetTree().ChangeSceneToFile("res://Scenes/Main.tscn");
        _send.Pressed += () =>
        {
            _send.Disabled = true;
            _transport.SendAction();
        };
        _transport.Trace += ShowTrace;
        _transport.ReadyChanged += ready =>
        {
            _send.Disabled = !ready;
            if (!ready) _receipt.Text = "";
            if (ready && _automatic)
            {
                _transport.SendAction();
                _transport.SendAction(repeatPending: true);
            }
        };
        _transport.Acknowledged += count =>
        {
            _send.Disabled = false;
            _receipt.Text = string.Format(Tr("SPIKE_ACK_COUNT"), count);
            if (_automatic && ++_acks == 2)
            {
                GD.Print("LAN_SPIKE AUTO_PASS duplicate_ack_count=2");
                GetTree().Quit();
            }
        };
        var addresses = IP.GetLocalAddresses().Where(ip => ip.StartsWith("192.168.", StringComparison.Ordinal) || ip.StartsWith("10.", StringComparison.Ordinal));
        GetNode<Label>(content + "Addresses").Text = string.Format(Tr("SPIKE_ADDRESSES"), string.Join(", ", addresses));
        ApplyLaunchArguments(OS.GetCmdlineUserArgs());
    }

    private void ShowResult(Error result)
    {
        if (result == Error.Ok) return;
        _status.Text = string.Format(Tr("SPIKE_START_ERROR"), result);
        GD.Print($"LAN_SPIKE START_ERROR code={result}");
        if (_automatic) GetTree().Quit(2);
    }

    private void ShowTrace(string trace)
    {
        var key = trace.Split(' ', 2)[0] switch
        {
            "HOST_LISTENING" => "SPIKE_HOST_READY",
            "CLIENT_CONNECTING" => "SPIKE_CONNECTING",
            "CLIENT_READY" => "SPIKE_CONNECTED",
            "HOST_ACTION" => "SPIKE_HOST_RECEIVED",
            "CLIENT_ACK" => "SPIKE_ACK_RECEIVED",
            "CONNECTION_TIMEOUT" => "SPIKE_TIMEOUT",
            "CONNECTION_FAILED" => "SPIKE_FAILED",
            "SERVER_DISCONNECTED" => "SPIKE_SERVER_LEFT",
            "HELLO_REJECTED" => "SPIKE_REJECTED",
            _ => null,
        };
        if (key is not null) _status.Text = Tr(key);
        if (_automatic && key is "SPIKE_TIMEOUT" or "SPIKE_FAILED" or "SPIKE_REJECTED")
            GetTree().Quit(2);
    }

    private void ApplyLaunchArguments(string[] arguments)
    {
        _automatic = arguments.Contains("--spike-auto");
        var port = LanSpikeTransport.DefaultPort;
        var protocol = 1;
        foreach (var argument in arguments)
        {
            if (argument.StartsWith("--spike-port=", StringComparison.Ordinal) &&
                !int.TryParse(argument[13..], out port)) { GetTree().Quit(2); return; }
            if (argument.StartsWith("--spike-protocol=", StringComparison.Ordinal) &&
                !int.TryParse(argument[17..], out protocol)) { GetTree().Quit(2); return; }
        }
        _transport.ClientProtocol = protocol;
        if (arguments.Contains("--spike-host")) ShowResult(_transport.Host(port));
        var join = arguments.FirstOrDefault(argument => argument.StartsWith("--spike-join=", StringComparison.Ordinal));
        if (join is not null) ShowResult(_transport.Join(join[13..], port));
        if (_automatic)
            GetTree().CreateTimer(15).Timeout += () => GetTree().Quit(3);
    }
}
