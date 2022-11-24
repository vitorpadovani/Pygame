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
WIDTH_bala = 50
HEIGHT_bala = 50


# ----- Inicia assets
background = pygame.image.load('assets/img/fundo.png').convert()
bala_azul = pygame.image.load('assets/img/balaazulpng').convert_alpha()
bala_preta = pygame.image.load('assets/img/balapretapng').convert_alpha()
bala_rosa = pygame.image.load('assets/img/balarosapng').convert_alpha()
bala_roxa = pygame.image.load('assets/img/balaroxapng').convert_alpha()
bala_laranja = pygame.image.load('assets/img/balalaranjapng').convert_alpha()
bala_azul = pygame.transform.scale(bala_azul, (HEIGHT_bala, WIDTH_bala))
bala_preta = pygame.transform.scale(bala_preta, (HEIGHT_bala, WIDTH_bala))
bala_rosa= pygame.transform.scale(bala_rosa, (HEIGHT_bala, WIDTH_bala))
bala_roxa = pygame.transform.scale(bala_roxa, (HEIGHT_bala, WIDTH_bala))
bala_laranja = pygame.transform.scale(bala_laranja, (HEIGHT_bala, WIDTH_bala))



class Bala_azul(pygame.sprite.Sprite):
    def __init__(self,bala_azul,x):
        self.image = espinho_img_baixo
        pygame.sprite.Sprite.__init__(self)

        # Adicionando a posição do espinho
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 0

# ----- Inicia estruturas de dados
game = True

all_sprites = pygame.sprite.Group()

all_sprites.add(bala_azul)
all_sprites.add(bala_preta)
all_sprites.add(bala_rosa)
all_sprites.add(bala_roxa)
all_sprites.add(bala_laranja)
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
    window.blit(all_sprites)
    

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

