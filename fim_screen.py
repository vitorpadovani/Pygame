import pygame
import random
from os import path

FPS=40
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
GAME=1
QUIT=2
INICIO=3
OVER=4
BLACK=(0,0,0)


def fim_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    tela_fim = pygame.image.load(path.join(IMG_DIR, 'fim.png')).convert()
    tela_fim= pygame.transform.scale(tela_fim, (480, 650))

    tela_fim_rect = tela_fim.get_rect()
    tempo = pygame.time.get_ticks()
    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(tela_fim, tela_fim_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        now = pygame.time.get_ticks()
        if now - tempo < 4000:
            pygame.quit()
    return state