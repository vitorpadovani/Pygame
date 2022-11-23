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
espinho_img = pygame.image.load('assets/img/espinho.png').convert_alpha()
espinho_img = pygame.transform.scale(espinho_img, (40, 40))

class Espinho(pygame.sprite.Sprite):
    def __init__(self,espinho_img):
        self.image = espinho_img
        pygame.sprite.Sprite.__init__(self)

        # Atualizando a posição do espinho
        # Sorteando a posição do espinho
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = random.randint(0, HEIGHT)


# Criando um grupo de meteoros
all_espinhos = pygame.sprite.Group()
# Criando os meteoros
for i in range(3):
    espinho = Espinho(espinho_img)
    all_espinhos.add(espinho)
# ----- Inicia estruturas de dados
game = True


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
    all_espinhos.draw(window)

    

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

