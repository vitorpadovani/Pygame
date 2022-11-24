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
WIDTH_bala = 30
HEIGHT_bala = 30

background = pygame.image.load('assets/img/fundo.png').convert()
img_bala_azul = pygame.image.load('assets/img/balaazulpng').convert_alpha()
img_bala_preta = pygame.image.load('assets/img/balapretapng').convert_alpha() 
img_bala_rosa = pygame.image.load('assets/img/balarosapng').convert_alpha()
img_bala_roxa = pygame.image.load('assets/img/balaroxapng').convert_alpha()
img_bala_laranja = pygame.image.load('assets/img/balalaranjapng').convert_alpha()
img_bala_azul = pygame.transform.scale(img_bala_azul, (HEIGHT_bala, WIDTH_bala))
img_bala_preta = pygame.transform.scale(img_bala_preta, (HEIGHT_bala, WIDTH_bala))
img_bala_rosa= pygame.transform.scale(img_bala_rosa, (HEIGHT_bala, WIDTH_bala))
img_bala_roxa = pygame.transform.scale(img_bala_roxa, (HEIGHT_bala, WIDTH_bala))
img_bala_laranja = pygame.transform.scale(img_bala_laranja, (HEIGHT_bala, WIDTH_bala))


#lista_posic_y = [0,30,60,90,120,150,180,210,240,270,300,330,360,390,420,450,480,510,540,570]

class Bala_azul(pygame.sprite.Sprite):
    def __init__(self,img_bala_azul,y):
        self.image = img_bala_azul
        pygame.sprite.Sprite.__init__(self)

        # Adicionando a posição da bala
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = random.randint(30, HEIGHT-30)


all_sprites = pygame.sprite.Group()
bala_azul = pygame.sprite.Group()
bala_preta = pygame.sprite.Group()
bala_rosa = pygame.sprite.Group()
bala_roxa = pygame.sprite.Group()
bala_laranja = pygame.sprite.Group()

# Criando os espinhod da parede 1
# while len(bala_azul) < 2:
#     espinho = Bala_azul(img_bala_azul)
#     hits = pygame.sprite.spritecollide(bala_azul, , True)
#     if len(hits) > 0:
#         b1 = Bala_azul(pygame.sprite.Sprite)
#         all_sprites.add(b1)
#         bala_azul.add(b1)


all_sprites.add(bala_azul)
all_sprites.add(bala_preta)
all_sprites.add(bala_rosa)
all_sprites.add(bala_roxa)
all_sprites.add(bala_laranja)

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
    window.blit(all_sprites)
    

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

