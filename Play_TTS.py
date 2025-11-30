import pygame
import time 

def play_wav(wav_filename="output.wav"):
    """
    Play a WAV file using pygame.
    """
    pygame.mixer.init()
    sound = pygame.mixer.Sound(wav_filename)
    sound.play()

    print(f"🔊 Playing: {wav_filename}")
    time.sleep(sound.get_length())

    pygame.mixer.quit()
