"""Deterministic original four-bar QuizParty music loops, synthesized without samples."""
from pathlib import Path
import wave
import numpy as np

RATE = 22050
BPM = 120
BEAT = 60 / BPM
LENGTH = 8.0  # four bars, exact sample boundary
OUT = Path(__file__).resolve().parents[1] / 'src/QuizParty.Godot/Art/Music'
OUT.mkdir(parents=True, exist_ok=True)

def render(name, chords, melody, style):
    rng = np.random.default_rng(472 + style)
    audio = np.zeros(int(RATE * LENGTH), dtype=np.float64)
    def add(signal, start, gain):
        pos = int(start * RATE)
        # Wrap tails into the next loop to avoid an abrupt cutoff.
        indices = (np.arange(len(signal)) + pos) % len(audio)
        np.add.at(audio, indices, signal * gain)
    def tone(note, duration, kind):
        t = np.arange(int(RATE * duration)) / RATE
        f = 440 * 2 ** ((note - 69) / 12)
        if kind == 'pad':
            env = (1 - np.exp(-t * 12)) * np.exp(-t * 1.5)
            return env * (np.sin(2*np.pi*f*t) + .18*np.sin(2*np.pi*2*f*t))
        if kind == 'bass':
            env = (1 - np.exp(-t * 100)) * np.exp(-t * 5)
            return env * (np.sin(2*np.pi*f*t) + .2*np.sin(2*np.pi*2*f*t))
        env = (1 - np.exp(-t * 250)) * np.exp(-t * 7)
        return env * (np.sin(2*np.pi*f*t) + .3*np.sin(2*np.pi*3*f*t)*np.exp(-t*10))
    for bar, chord in enumerate(chords):
        for n in chord: add(tone(n, 1.9, 'pad'), bar*2, .055)
        for beat in range(4):
            pos = bar*2 + beat*BEAT
            add(tone(chord[0]-12 + (7 if beat == 2 else 0), .45, 'bass'), pos, .13)
            t = np.arange(int(RATE*.14))/RATE
            kick = np.sin(2*np.pi*(110*t-220*t*t))*np.exp(-t*28)
            if beat in (0, 2): add(kick, pos, .13)
            if beat in (1, 3): add(rng.standard_normal(len(t))*np.exp(-t*40), pos, .035)
            for half in range(2):
                tt=np.arange(int(RATE*.045))/RATE
                add(rng.standard_normal(len(tt))*np.exp(-tt*90), pos+half*.25, .012)
    for i, note in enumerate(melody):
        if note: add(tone(note, .7, 'bell'), i*.25, .09 if style != 1 else .065)
    audio = np.tanh(audio)
    audio *= .65 / max(.65, np.max(np.abs(audio)))
    with wave.open(str(OUT / (name + '.wav')), 'wb') as wav:
        wav.setnchannels(1); wav.setsampwidth(2); wav.setframerate(RATE)
        wav.writeframes((audio*32767).astype('<i2').tobytes())
    print(name, len(audio)/RATE, 'seconds', 'peak', round(float(np.max(np.abs(audio))), 3))

render('menu', [[48,52,55],[45,48,52],[53,57,60],[43,47,50]], [72,0,76,79,0,76,74,0,72,0,69,72,76,0,74,0,72,0,69,72,77,0,76,0,74,0,71,74,79,0,76,0], 0)
render('question', [[45,48,52],[41,45,48],[48,52,55],[43,47,50]], [69,0,72,0,76,0,72,0,69,0,72,0,77,0,72,0,67,0,72,0,76,0,72,0,67,0,71,0,74,0,71,0], 1)
render('reveal', [[48,52,55],[50,53,57],[53,57,60],[43,47,50]], [76,0,79,0,84,0,79,0,77,0,81,0,84,0,81,0,77,0,81,0,84,0,81,0,74,0,79,0,83,0,79,0], 2)
render('final', [[48,52,55],[53,57,60],[45,48,52],[43,47,50]], [72,76,79,0,84,0,79,76,77,81,84,0,81,0,77,0,76,79,81,0,84,0,81,79,74,79,83,0,86,0,83,79], 3)

render('tension', [[45,48,52],[41,45,48],[50,53,57],[40,47,50]], [69,72,76,72,69,72,76,72,69,72,77,72,69,72,77,72,74,77,81,77,74,77,81,77,71,74,79,74,71,74,79,74], 4)
render('scoreboard', [[53,57,60],[48,52,55],[50,53,57],[43,47,50]], [77,0,81,0,84,0,81,0,76,0,79,0,84,0,79,0,74,0,77,0,81,0,77,0,71,0,74,0,79,0,74,0], 5)

def sting(name, notes, duration):
    audio = np.zeros(int(RATE * duration), dtype=np.float64)
    for note, start in notes:
        t = np.arange(int(RATE * min(1.1, duration-start))) / RATE
        f = 440 * 2 ** ((note - 69) / 12)
        envelope = (1 - np.exp(-t * 160)) * np.exp(-t * 5)
        sound = (np.sin(2*np.pi*f*t) + .35*np.sin(2*np.pi*2*f*t) + .12*np.sin(2*np.pi*3*f*t)) * envelope
        offset = int(start * RATE)
        audio[offset:offset+len(sound)] += sound * .12
    audio *= .65 / max(.65, np.max(np.abs(audio)))
    with wave.open(str(OUT / ('sting-' + name + '.wav')), 'wb') as wav:
        wav.setnchannels(1); wav.setsampwidth(2); wav.setframerate(RATE)
        wav.writeframes((audio*32767).astype('<i2').tobytes())
    print('sting-' + name, duration, 'seconds')

sting('reveal', [(72,0), (76,.10), (79,.20), (84,.32)], 1.4)
sting('score', [(60,0), (67,.12), (72,.24), (76,.36)], 1.5)
sting('final', [(60,0), (64,.14), (67,.28), (72,.42), (76,.55), (79,.69), (84,.85)], 2.0)
