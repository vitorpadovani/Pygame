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


def init_screen(screen):
    # VariÃ¡vel para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    tela_inicio = pygame.image.load(path.join(IMG_DIR, 'inicio.png')).convert()
    tela_inicio= pygame.transform.scale(tela_inicio, (480, 650))

    tela_inicio_rect = tela_inicio.get_rect()

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botÃ£o, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    state = GAME
                    running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(tela_inicio, tela_inicio_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state