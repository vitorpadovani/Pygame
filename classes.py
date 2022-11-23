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
HEIGHT_bird = 60


# ----- Inicia assets
background = pygame.image.load('assets/img/fundo.png').convert()
bird_img_dir = pygame.image.load('assets/img/bird.png').convert_alpha()
bird_img_dir = pygame.transform.scale(bird_img_dir, (HEIGHT_bird, WIDTH_bird))
bird_img_esq = pygame.image.load('assets/img/bird2.png').convert_alpha()
bird_img_esq = pygame.transform.scale(bird_img_esq, (HEIGHT_bird, WIDTH_bird))
bird_img = pygame.image.load('assets/img/bird.png').convert_alpha()
bird_img = pygame.transform.scale(bird_img, (HEIGHT_bird, WIDTH_bird))

# ----- Inicia estruturas de dados
game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 40

# ===== Loop principal =====
aplica_gravidade = False


class Bird(pygame.sprite.Sprite):
    def __init__(self, bird_img_dir, bird_img_esq):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = bird_img_dir
        self.image_dir = bird_img_dir
        self.image_esq = bird_img_esq
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.bird_speed_x = 0
        self.bird_speed_y = 0 

    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.bird_speed_x
        self.rect.y += self.bird_speed_y

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        if self.rect.left < 0:
            self.rect.left = 0
        
        if self.rect.x + self.rect.width >= 480:
            self.bird_speed_x *= -1
            self.rect.x += self.bird_speed_x
            bird_img = bird_img_esq

        if self.rect.x <= 0:
            self.bird_speed_x *= -1
            self.rect.x += self.bird_speed_x
            bird_img = bird_img_dir
        if aplica_gravidade:
            self.bird_speed_y += ACELERACAO
            self.rect.y += self.bird_speed_y
            self.rect.x += self.bird_speed_x

            
        #Quando bater na parede
        if self.rect.x + WIDTH_bird >= 480:
            self.bird_speed_x *= -1
            self.rect.x += self.bird_speed_x
            bird_img = bird_img_esq

        elif self.bird_speed_x <= 0:
            self.bird_speed_x *= -1
            self.rect.x += self.bird_speed_x
            bird_img = bird_img_dir
        bird_x = self.rect.x


#posição inicial do passaro
# bird_x = (WIDTH/2)
# bird_y = HEIGHT/2

# Gravidade aplicada a cada frame 
ACELERACAO = 0.8

print('aperte espaço para pular com a bola')

all_sprites = pygame.sprite.Group()
player = Bird(bird_img_esq, bird_img_dir)
all_sprites.add(player)
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
    # if aplica_gravidade:
    #     bird_speed_y += ACELERACAO
    #     bird_y += bird_speed_y
    #     bird_x += bird_speed_x

        
    # #Quando bater na parede
    # if bird_x + WIDTH_bird >= 480:
    #     bird_speed_x *= -1
    #     bird_x += bird_speed_x
    #     bird_img = bird_img2

    # elif bird_x <= 0:
    #     bird_speed_x *= -1
    #     bird_x += bird_speed_x
    #     bird_img = bird_img1

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    # Desenhando o passaro na janela
    all_sprites.draw(window)
    #window.blit(player)
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
