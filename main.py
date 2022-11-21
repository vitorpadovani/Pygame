# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init() 

# ----- Gera tela principal
window = pygame.display.set_mode((480, 650))
pygame.display.set_caption('Spikes!')

# ----- Inicia estruturas de dados
game = True

# ---- Inicia assets 
espinho = pygame.image.load('assets/img/espinho.png').convert_alpha()
espinho = pygame.transform.scale(espinho, (30, 30))

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

