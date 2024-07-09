from pydub import AudioSegment
from pydub.generators import Sine

def generate_solo_sound(path):
    sound = AudioSegment.silent(duration=0)
    for note in path:
        if isinstance(note, tuple) and len(note) == 3:
            effect, pos1, pos2 = note
            freq1 = note_to_frequency(pos1)
            freq2 = note_to_frequency(pos2)
            duration = 500  # duration in ms for effects
            if effect == "slide":
                sound += Sine(freq1).to_audio_segment(duration=duration).fade_out(50).fade_in(50).append(
                    Sine(freq2).to_audio_segment(duration=duration).fade_in(50).fade_out(50), crossfade=50)
            elif effect == "pull-off":
                sound += Sine(freq1).to_audio_segment(duration=duration).fade_out(50).fade_in(50).append(
                    Sine(freq2).to_audio_segment(duration=duration).fade_in(50).fade_out(50), crossfade=50)
            elif effect == "bend":
                sound += Sine(freq1).to_audio_segment(duration=duration).fade_out(50).fade_in(50).append(
                    Sine(freq2).to_audio_segment(duration=duration).fade_in(50).fade_out(50), crossfade=50)
        else:
            string, fret = note
            frequency = note_to_frequency(note)
            duration = 500  # duration in ms
            sound += Sine(frequency).to_audio_segment(duration=duration).fade_out(50).fade_in(50)
    
    sound.export("/static/solo.mp3", format="mp3")

def note_to_frequency(note):
    string, fret = note
    open_string_frequencies = {
        "e": 329.63,
        "B": 246.94,
        "G": 196.00,
        "D": 146.83,
        "A": 110.00,
        "E": 82.41
    }
    frequency = open_string_frequencies[string] * (2 ** (fret / 12))
    return frequency
