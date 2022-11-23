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


class Espinho_lado_esquerdo(pygame.sprite.Sprite):
    def __init__(self,espinho_img_e):
        self.image = espinho_img_e
        pygame.sprite.Sprite.__init__(self)

        # Atualizando a posição do espinho
        # Sorteando a posição do espinho
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = random.randint(0, HEIGHT)


class Espinho_lado_direito(pygame.sprite.Sprite):
    def __init__(self,espinho_img_d):
        self.image = espinho_img_d
        pygame.sprite.Sprite.__init__(self)

        # Atualizando a posição do espinho
        # Sorteando a posição do espinho
        self.rect = self.image.get_rect()
        self.rect.x = 440
        self.rect.y = random.randint(0, HEIGHT)



# Criando um grupo de meteoros
all_sprites = pygame.sprite.Group()
all_espinhos_e = pygame.sprite.Group()
all_espinhos_d = pygame.sprite.Group()

# Criando os meteoros
while len(all_espinhos_e) < 4:
    espinho = Espinho_lado_esquerdo(espinho_img_e)
    hits = pygame.sprite.spritecollide(espinho, all_espinhos_e, True)
    if len(hits) == 0:
        all_espinhos_e.add(espinho)


# Criando os meteoros
while len(all_espinhos_d) < 4:
    espinho = Espinho_lado_direito(espinho_img_e)
    hits = pygame.sprite.spritecollide(espinho, all_espinhos_d, True)
    if len(hits) == 0:
        all_espinhos_d.add(espinho)
# ----- Inicia estruturas de dados
game = True

all_sprites.add(all_espinhos_e)
all_sprites.add(all_espinhos_d)

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((194, 175, 181))  # Preenche com a cor cinza
    window.blit(window, (0, 0))
    # Desenha os espinhos
    all_sprites.draw(window)
    

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

