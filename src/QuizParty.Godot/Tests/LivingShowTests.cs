using GdUnit4;
using Godot;
using QuizParty.Presentation;
using static GdUnit4.Assertions;

namespace QuizParty.Godot.Tests;

[TestSuite]
public class LivingShowTests
{
    [TestCase]
    [RequireGodotRuntime]
    public async Task ReplayAndReducedMotionCancelPerformanceAndKeepFinalInformation()
    {
        var tree = (SceneTree)Engine.GetMainLoop();
        using var root = new Control(); tree.Root.AddChild(root);
        var performance = new RevealPerformance { Size = new(900, 340) }; root.AddChild(performance);
        try
        {
            performance.Configure(false, false, .65f);
            performance.Replay();
            AssertThat(performance.Playing).IsTrue();
            AssertThat(performance.AnswerVisible).IsFalse();
            var player = performance.GetNode<AnimationPlayer>("Choreography");
            player.Advance(1.6); performance._Process(0);
            AssertThat(performance.AnswerVisible).IsTrue();
            AssertThat(performance.JokeVisible).IsFalse();
            performance.Replay();
            AssertThat(performance.AnswerVisible).IsFalse();
            AssertThat(player.CurrentAnimationPosition).IsEqual(0d);
            performance.Configure(true, false, .65f);
            AssertThat(performance.Playing).IsFalse();
            AssertThat(performance.AnswerVisible).IsTrue();
            AssertThat(performance.JokeVisible).IsTrue();
            AssertThat(performance.GetNode<AudioStreamPlayer>("PerformanceSound").Playing).IsFalse();
            performance.Replay();
            AssertThat(performance.Playing).IsFalse();
            AssertThat(performance.AnswerVisible).IsTrue();
            performance.Configure(false, true, 0);
            performance.Replay();
            AssertThat(performance.GetNode<AudioStreamPlayer>("PerformanceSound").Playing).IsFalse();
            root.RemoveChild(performance); performance.Free();
            await tree.ToSignal(tree, SceneTree.SignalName.ProcessFrame);
        }
        finally { root.Free(); }
    }

    [TestCase]
    [RequireGodotRuntime]
    public void PuppetSheetsHaveRealTransparentGuttersAndAudioIsBounded()
    {
        foreach (var character in new[] { "blue", "orange" })
        {
            using var image = GD.Load<Texture2D>($"res://Art/LivingShow/{character}-puppet.png").GetImage();
            AssertThat(image.GetWidth()).IsEqual(1536);
            AssertThat(image.GetHeight()).IsEqual(1024);
            AssertThat(image.GetPixel(0, 0).A < .01f).IsTrue();
            for (var y = 0; y < 2; y++)
                for (var x = 0; x < 3; x++)
                {
                    using var cell = image.GetRegion(new(x * 512, y * 512, 512, 512));
                    AssertThat(cell.GetUsedRect().Size.X > 100).IsTrue();
                }
        }
        var audio = GD.Load<AudioStream>("res://Art/LivingShow/reveal-sting.wav");
        AssertThat(Math.Abs(audio.GetLength() - RevealPerformance.Duration) < .01).IsTrue();
    }
}
