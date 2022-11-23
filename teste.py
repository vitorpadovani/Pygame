import pygame

pygame.init()
pygame.mixer.init()

# Carrega os sons do jogo
pygame.mixer.music.load('assets/sounds/M72VSQV-games-logo.mp3')
pygame.mixer.music.set_volume(0.4)
pulo_sound = pygame.mixer.Sound('assets/sounds/mixkit-player-jumping-in-a-video-game-2043.wav')
perdeu_sound = pygame.mixer.Sound('assets/sounds/mixkit-sad-game-over-trombone-471.wav')
bala_sound = pygame.mixer.Sound('assets/sounds/mixkit-space-coin-win-notification-271.wav')

pygame.mixer.music.play(loops=-1)

#pq esta em uma lista os sons no handout 20 
#linha 226 como saber qual som eh