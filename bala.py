# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import math

pygame.init()

# ----- Gera tela principal
WIDTH = 480
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bala')
WIDTH_bala = 60
HEIGHT_bala = 60


# ----- Inicia assets
background = pygame.image.load('assets/img/fundo.png').convert()
bala_img = pygame.image.load('assets/img/bird.png').convert_alpha()
bala_img = pygame.transform.scale(bala_img, (HEIGHT_bala, WIDTH_bala))

# ----- Inicia estruturas de dados
game = True


# ===== Loop principal =====
pygame.mixer.music.play(loops=-1)
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
   # window.blit(meteor_img_small, (meteor_x, meteor_y))
    # Desenha os espinhos
    window.blit(bala_img, (bala_x, bala_y))
    

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
