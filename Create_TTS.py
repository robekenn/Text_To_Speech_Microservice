import pyttsx3
from pydub import AudioSegment
import os

def text_to_wav(text, wav_filename="output.wav"):
    """
    Create a clean WAV file from text using pyttsx3 + pydub.
    Works on Windows, Mac, and Linux.
    """

    temp_file = "temp_audio.aiff"  # pyttsx3 reliably creates AIFF on all systems

    # --- Generate the temporary audio file ---
    engine = pyttsx3.init()
    engine.save_to_file(text, temp_file)
    engine.runAndWait()

    # Ensure file exists
    if not os.path.exists(temp_file):
        raise RuntimeError("pyttsx3 failed to create audio file.")

    # --- Convert to WAV ---
    sound = AudioSegment.from_file(temp_file)
    sound.export(wav_filename, format="wav")

    # Cleanup temporary file
    os.remove(temp_file)

    print(f"WAV file created: {wav_filename}")
    return wav_filename




if __name__ == "__main__":
    # Text you want spoken
    text = message[1]

    # Convert text → WAV
    wav_file = text_to_wav(text, "output.wav")
