import pygame

pygame.mixer.init()
pygame.init()

pygame.mixer.music.load('ex021.wav')
pygame.mixer.music.play()
pygame.event.wait()
