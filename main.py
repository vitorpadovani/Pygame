# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init() 

# ----- Gera tela principal
WIDTH = 480
HEIGHT = 650
window = pygame.display.set_mode((480, 650))
pygame.display.set_caption('Spikes!')

# ----- Inicia estruturas de dados
game = True

# ---- Inicia assets 
espinho_img = pygame.image.load('assets/img/espinho.png').convert_alpha()
espinho_img = pygame.transform.scale(espinho_img, (30, 30))

class Espinho(pygame.sprite.Sprite):
    def update(self):
        # Atualizando a posição do espinho

        # Sorteando a posição do espinho
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.y = random.randint(0, HEIGHT)


# Criando um grupo de meteoros
all_espinhos = pygame.sprite.Group()
# Criando os meteoros
for i in range(3):
    espinho = espinho(espinho_img)
    all_espinhos.add(espinho)


# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((194, 175, 181))  # Preenche com a cor cinza
    window.blit(espinho, (0, 0))
    

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

