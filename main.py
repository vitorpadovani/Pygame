# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init() 
pygame.mixer.init()


# ----- Gera tela principal
WIDTH = 480
HEIGHT = 650
WIDTH_bala = 40
HEIGHT_bala = 40
window = pygame.display.set_mode((480, 650))
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Spikes!')


# ---- Inicia assets 
espinho_img_e = pygame.image.load('assets/img/espinho.png').convert_alpha()
espinho_img_e = pygame.transform.scale(espinho_img_e, (40, 40))

espinho_img_d = pygame.image.load('assets/img/espinho pro lado.png').convert_alpha()
espinho_img_d = pygame.transform.scale(espinho_img_d, (40, 40))
espinho_img_d = pygame.transform.flip(espinho_img_d, True,True)


espinho_img_cima = pygame.image.load('assets/img/espinho_pra_cima.png').convert_alpha()
espinho_img_cima = pygame.transform.scale(espinho_img_cima, (40, 40))

espinho_img_baixo = pygame.image.load('assets/img/espinho_pra_baixo.png').convert_alpha()
espinho_img_baixo = pygame.transform.scale(espinho_img_baixo, (40, 40))

img_bala_azul = pygame.image.load('assets/img/balaazul.png').convert_alpha()
img_bala_preta = pygame.image.load('assets/img/balapreta.png').convert_alpha() 
img_bala_rosa = pygame.image.load('assets/img/balarosa.png').convert_alpha()
img_bala_roxa = pygame.image.load('assets/img/balaroxa.png').convert_alpha()
img_bala_laranja = pygame.image.load('assets/img/balalaranja.png').convert_alpha()
img_bala_azul = pygame.transform.scale(img_bala_azul, (HEIGHT_bala, WIDTH_bala))
img_bala_preta = pygame.transform.scale(img_bala_preta, (HEIGHT_bala, WIDTH_bala))
img_bala_rosa= pygame.transform.scale(img_bala_rosa, (HEIGHT_bala, WIDTH_bala))
img_bala_roxa = pygame.transform.scale(img_bala_roxa, (HEIGHT_bala, WIDTH_bala))
img_bala_laranja = pygame.transform.scale(img_bala_laranja, (HEIGHT_bala, WIDTH_bala))

background = pygame.image.load('assets/img/fundo1.png').convert()
background = pygame.transform.scale(background, (480, 650))
background2 = pygame.image.load('assets/img/fundo2.png').convert()
background2 = pygame.transform.scale(background2, (480, 650))
background3 = pygame.image.load('assets/img/fundo3.png').convert()
background3 = pygame.transform.scale(background3, (480, 650))

pygame.mixer.music.load('assets/sounds/M72VSQV-games-logo.mp3')
pygame.mixer.music.set_volume(0.4)
pulo_sound = pygame.mixer.Sound('assets/sounds/mixkit-player-jumping-in-a-video-game-2043.wav')
perdeu_sound = pygame.mixer.Sound('assets/sounds/mixkit-sad-game-over-trombone-471.wav')
bala_sound = pygame.mixer.Sound('assets/sounds/mixkit-arcade-bonus-alert-767.wav')

class Espinho_lado_esquerdo(pygame.sprite.Sprite):
    def __init__(self,espinho_img_e):
        self.image = espinho_img_e
        pygame.sprite.Sprite.__init__(self)

        # Atualizando a posição do espinho
        # Sorteando a posição do espinho
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = random.randint(40, HEIGHT-60)

class Espinho_lado_direito(pygame.sprite.Sprite):
    def __init__(self,espinho_img_d):
        self.image = espinho_img_d
        self.image = pygame.transform.flip(espinho_img_d,True,False)
        pygame.sprite.Sprite.__init__(self)

        # Atualizando a posição do espinho
        # Sorteando a posição do espinho
        self.rect = self.image.get_rect() 
        self.rect.x = 440
        self.rect.y = random.randint(40, HEIGHT-60)

class Espinho_pra_cima(pygame.sprite.Sprite):
    def __init__(self,espinho_img_cima,x):
        self.image = espinho_img_cima 
        pygame.sprite.Sprite.__init__(self)

        # Adicionando a posição do espinho
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 610

class Espinho_pra_baixo(pygame.sprite.Sprite):
    def __init__(self,espinho_img_baixo,x):
        self.image = espinho_img_baixo
        pygame.sprite.Sprite.__init__(self)

        # Adicionando a posição do espinho
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 0

class Bala_azul(pygame.sprite.Sprite):
    def __init__(self,img_bala_azul):
        self.image = img_bala_azul
        pygame.sprite.Sprite.__init__(self)

        # Adicionando a posição da bala
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = random.randint(30, HEIGHT-30)

# Criando um grupo de meteoros
all_sprites = pygame.sprite.Group()
all_espinhos_e = pygame.sprite.Group()
all_espinhos_d = pygame.sprite.Group()
all_espinhos_cima = pygame.sprite.Group()
all_espinhos_baixo = pygame.sprite.Group()
bala_azul = pygame.sprite.Group()
bala_preta = pygame.sprite.Group()
bala_rosa = pygame.sprite.Group()
bala_roxa = pygame.sprite.Group()
bala_laranja = pygame.sprite.Group()

# Criando os espinhod da parede 1
while len(all_espinhos_e) < 4:
    espinho = Espinho_lado_esquerdo(espinho_img_e)
    hits = pygame.sprite.spritecollide(espinho, all_espinhos_e, True)
    if len(hits) == 0:
        all_espinhos_e.add(espinho)


# Criando os espinhos da parede 2
while len(all_espinhos_d) < 4:
    espinho = Espinho_lado_direito(espinho_img_d)
    hits = pygame.sprite.spritecollide(espinho, all_espinhos_d, True)
    if len(hits) == 0:
        all_espinhos_d.add(espinho)

# Criando os espinhos virados pra cima
lista_esp_cima = [0,40,80,120,160,200,240,280,320,360,400,440]
for i in range(0,len(lista_esp_cima)):
    x = lista_esp_cima[i]
    espinho = Espinho_pra_cima(espinho_img_cima, x)
    all_espinhos_cima.add(espinho)

# Criando os espinhos virados pra baixo
for i in range(0,len(lista_esp_cima)):
    x = lista_esp_cima[i]
    espinho = Espinho_pra_baixo(espinho_img_baixo, x)
    all_espinhos_baixo.add(espinho)

# Criando bala azul
while len(bala_azul) < 1:
    balinha = Bala_azul(img_bala_azul)
    hits = pygame.sprite.spritecollide(balinha, all_espinhos_e, True, pygame.sprite.collide_mask)
    hits2 = pygame.sprite.spritecollide(balinha, all_espinhos_baixo, True, pygame.sprite.collide_mask)
    hits3 = pygame.sprite.spritecollide(balinha, all_espinhos_cima, True, pygame.sprite.collide_mask)
    if len(hits) == 0 and len(hits2) == 0 and len(hits3) == 0:
        bala_azul.add(balinha)

# ----- Inicia estruturas de dados
game = True

all_sprites.add(all_espinhos_e)
all_sprites.add(all_espinhos_d)
all_sprites.add(all_espinhos_cima)
all_sprites.add(all_espinhos_baixo)
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


    all_sprites.update()
    
    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
   # window.blit(meteor_img_small, (meteor_x, meteor_y))
    # Desenha os sprites
    all_sprites.draw(window)
    

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

