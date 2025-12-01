import pygame
import time 

def play_wav(wav_filename="output.wav"):
    #init sound
    pygame.mixer.init()
    sound = pygame.mixer.Sound(wav_filename)

    #play sound
    sound.play()

    print(f"Playing: {wav_filename}")
    time.sleep(sound.get_length())

    pygame.mixer.quit()
    return "OK"

