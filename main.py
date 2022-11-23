# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init() 

# ----- Gera tela principal
WIDTH = 480
HEIGHT = 650
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

background = pygame.image.load('assets/img/fundo1.png').convert()
background = pygame.transform.scale(background, (480, 650))
background2 = pygame.image.load('assets/img/fundo2.png').convert()
background2 = pygame.transform.scale(background2, (480, 650))
background3 = pygame.image.load('assets/img/fundo3.png').convert()
background3 = pygame.transform.scale(background3, (480, 650))



class Espinho_lado_esquerdo(pygame.sprite.Sprite):
    def __init__(self,espinho_img_e):
        self.image = espinho_img_e
        pygame.sprite.Sprite.__init__(self)

        # Atualizando a posição do espinho
        # Sorteando a posição do espinho
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = random.randint(40, HEIGHT-40)

class Espinho_lado_direito(pygame.sprite.Sprite):
    def __init__(self,espinho_img_d):
        self.image = espinho_img_d
        self.image = pygame.transform.flip(espinho_img_d,True,False)
        pygame.sprite.Sprite.__init__(self)

        # Atualizando a posição do espinho
        # Sorteando a posição do espinho
        self.rect = self.image.get_rect()
        self.rect.x = 440
        self.rect.y = random.randint(40, HEIGHT-40)

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


# Criando um grupo de meteoros
all_sprites = pygame.sprite.Group()
all_espinhos_e = pygame.sprite.Group()
all_espinhos_d = pygame.sprite.Group()
all_espinhos_cima = pygame.sprite.Group()
all_espinhos_baixo = pygame.sprite.Group()

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

# ----- Inicia estruturas de dados
game = True

all_sprites.add(all_espinhos_e)
all_sprites.add(all_espinhos_d)
all_sprites.add(all_espinhos_cima)
all_sprites.add(all_espinhos_baixo)

# ===== Loop principal =====
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
    all_sprites.draw(window)
    

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

