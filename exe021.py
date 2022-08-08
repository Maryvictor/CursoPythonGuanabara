#Faça um programa que abra um e reproduza o audio de um arquivo mp3

import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('audio.mp3')
pygame.mixer.music.play()
pygame.event.wait()

