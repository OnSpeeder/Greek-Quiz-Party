"""Original deterministic synthesized reveal sting. No samples or third-party audio.
Requires the existing NumPy tool environment. Writes 48 kHz stereo PCM, peaks -3 dBFS.
"""
from pathlib import Path
import wave
import numpy as np

RATE = 48000
rng = np.random.default_rng(261026)
mix = np.zeros((int(5.2 * RATE), 2), dtype=np.float64)


def add(signal, start, pan=0.0, gain=1.0):
    offset = int(start * RATE)
    count = min(len(signal), len(mix) - offset)
    angle = (pan + 1) * np.pi / 4
    mix[offset:offset + count, 0] += signal[:count] * np.cos(angle) * gain
    mix[offset:offset + count, 1] += signal[:count] * np.sin(angle) * gain


def mallet(note, duration=.6):
    t = np.arange(int(duration * RATE)) / RATE
    f = 440 * 2 ** ((note - 69) / 12)
    attack = 1 - np.exp(-t * 650)
    return attack * (np.sin(2 * np.pi * f * t) * np.exp(-t * 7)
                     + .24 * np.sin(2 * np.pi * f * 3.99 * t) * np.exp(-t * 18)
                     + .08 * np.sin(2 * np.pi * f * 9.8 * t) * np.exp(-t * 35))


# Quiet brushed anticipation, rising C-major-sixth figure, then a bright flourish.
for i, start in enumerate([.08, .28, .48, .68, .86, 1.02, 1.15, 1.27]):
    t = np.arange(int(.09 * RATE)) / RATE
    noise = rng.standard_normal(len(t))
    brush = np.diff(noise, prepend=0) * np.exp(-t * 65) * (1 - np.exp(-t * 1000))
    add(brush, start, -.25 + i / 16, .018 + i * .002)
for note, start in zip([60, 64, 67, 69, 72], [.45, .65, .85, 1.05, 1.24]):
    add(mallet(note), start, -.3, .11)
for note in [48, 60, 64, 67, 74]:
    add(mallet(note, 1.4), 1.4, -.15, .14)
for note, start in zip([84, 79, 76, 72], [1.42, 1.5, 1.58, 1.66]):
    add(mallet(note), start, .25, .10)
# Comic descending rounded reed-like ornament after Orange's double-take.
t = np.arange(int(.38 * RATE)) / RATE
frequency = 310 - 120 * t / .38 + 9 * np.sin(2 * np.pi * 8 * t)
phase = 2 * np.pi * np.cumsum(frequency) / RATE
reed = (np.sin(phase) + .17 * np.sin(3 * phase)) * np.sin(np.pi * t / .38) ** 2
add(reed, 2.35, .45, .16)
for note, start in [(67, 3.0), (72, 3.18), (76, 3.36)]:
    add(mallet(note, .9), start, 0, .07)
# Small stereo room reflections, not a long wash over the joke.
dry = mix.copy()
for delay, gain in [(.047, .12), (.083, .08), (.127, .045)]:
    n = int(delay * RATE)
    mix[n:] += dry[:-n, ::-1] * gain
peak = np.max(np.abs(mix))
mix *= 10 ** (-3 / 20) / peak
output = Path(__file__).resolve().parents[1] / 'src/QuizParty.Godot/Art/LivingShow/reveal-sting.wav'
with wave.open(str(output), 'wb') as wav:
    wav.setnchannels(2)
    wav.setsampwidth(2)
    wav.setframerate(RATE)
    wav.writeframes((mix * 32767).astype('<i2').tobytes())
print(f'{output}: 5.2 s, stereo 48 kHz, peak -3 dBFS, original synthesized instruments')
