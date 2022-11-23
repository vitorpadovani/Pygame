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
pygame.display.set_caption('Exemplo de pula')
WIDTH_bird = 50
HEIGHT_bird = 100


# ----- Inicia assets
background = pygame.image.load('assets/img/fundo.png').convert()
bird_img = pygame.image.load('assets/img/bird.png').convert_alpha()
bird_img = pygame.transform.scale(bird_img, (HEIGHT_bird, WIDTH_bird))


# ----- Inicia estruturas de dados
game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 40

# ===== Loop principal =====
aplica_gravidade = False

#Velocidade inicial do passaro
bird_speed_x = 0
bird_speed_y = 0

#posição inicial do passaro
bird_x = (WIDTH/2)
bird_y = HEIGHT/2

# Gravidade aplicada a cada frame
ACELERACAO = 0.8

print('aperte espaço para pular com a bola')
while game:
    clock.tick(FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speed_y = -8
                if bird_speed_x < 0:
                    bird_speed_x = -8
                else:
                    bird_speed_x = 8
                aplica_gravidade = True

    # ----- Atualiza estado do jogo
    #aplicando gravidade
    if aplica_gravidade:
        bird_speed_y += ACELERACAO
        bird_y += bird_speed_y
        bird_x += bird_speed_x

        
    #Quando bater na parede
    if bird_x + WIDTH_bird >= 480:
        bird_speed_x *= -1
        bird_x += bird_speed_x

    elif bird_x <= 0:
        bird_speed_x *= -1
        bird_x += bird_speed_x


    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    # Desenhando a bola na janela
    window.blit(bird_img, (bird_x, bird_y))
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
