import os
import wave
import pygame

print("File exists:", os.path.exists("output.wav"))

try:
    w = wave.open("output.wav")
    print("WAV params:", w.getparams())
except Exception as e:
    print("WAV open error:", e)

try:
    pygame.mixer.init()
    sound = pygame.mixer.Sound("output.wav")
    sound.play()
    print("Pygame successfully loaded the sound!")
except Exception as e:
    print("Pygame error:", e)
