# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import math

pygame.init() 
pygame.mixer.init()


# ----- Gera tela principal
WIDTH = 480
HEIGHT = 650
WIDTH_bala = 40
HEIGHT_bala = 40
WIDTH_bird = 43 
HEIGHT_bird = 53
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
img_bala_rosa = pygame.image.load('assets/img/balarosa.png').convert_alpha()
img_bala_roxa = pygame.image.load('assets/img/balaroxa.png').convert_alpha()
img_bala_laranja = pygame.image.load('assets/img/balalaranja.png').convert_alpha()
img_bala_azul = pygame.transform.scale(img_bala_azul, (HEIGHT_bala, WIDTH_bala))
img_bala_rosa= pygame.transform.scale(img_bala_rosa, (HEIGHT_bala, WIDTH_bala))
img_bala_roxa = pygame.transform.scale(img_bala_roxa, (HEIGHT_bala, WIDTH_bala))
img_bala_laranja = pygame.transform.scale(img_bala_laranja, (HEIGHT_bala, WIDTH_bala))

bird_img_dir = pygame.image.load('assets/img/bird.png').convert_alpha()
bird_img_dir = pygame.transform.scale(bird_img_dir, (HEIGHT_bird, WIDTH_bird))
bird_img_esq = pygame.image.load('assets/img/bird2.png').convert_alpha()
bird_img_esq = pygame.transform.scale(bird_img_esq, (HEIGHT_bird, WIDTH_bird))
bird_img = pygame.image.load('assets/img/bird.png').convert_alpha()
bird_img = pygame.transform.scale(bird_img, (HEIGHT_bird, WIDTH_bird))

# background = pygame.image.load('assets/img/fundo1.png').convert()
# background = pygame.transform.scale(background, (480, 650))
background = pygame.image.load('assets/img/fundo2.png').convert()
background = pygame.transform.scale(background, (480, 650))

pygame.mixer.music.load('assets/sounds/M72VSQV-games-logo.mp3')
pygame.mixer.music.set_volume(0.05)
pulo_sound = pygame.mixer.Sound('assets/sounds/mixkit-player-jumping-in-a-video-game-2043.wav')
perdeu_sound = pygame.mixer.Sound('assets/sounds/mixkit-sad-game-over-trombone-471.wav')
bala_sound = pygame.mixer.Sound('assets/sounds/mixkit-arcade-bonus-alert-767.wav')
fonte_score = pygame.font.Font('assets/fonte/PressStart2P.ttf', 28)


class Espinho_lado_esquerdo(pygame.sprite.Sprite):
    def __init__(self,espinho_img_e):
        self.image = espinho_img_e
        pygame.sprite.Sprite.__init__(self)

        # Atualizando a posição do espinho
        # Sorteando a posição do espinho
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
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
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 440
        self.rect.y = random.randint(40, HEIGHT-60)

class Espinho_pra_cima(pygame.sprite.Sprite):
    def __init__(self,espinho_img_cima,x):
        self.image = espinho_img_cima 
        pygame.sprite.Sprite.__init__(self)

        # Adicionando a posição do espinho
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = 610

class Espinho_pra_baixo(pygame.sprite.Sprite):
    def __init__(self,espinho_img_baixo,x):
        self.image = espinho_img_baixo
        pygame.sprite.Sprite.__init__(self)

        # Adicionando a posição do espinho
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = 0

class Bala_azul(pygame.sprite.Sprite):
    def __init__(self,img_bala_azul):
        self.image = img_bala_azul
        pygame.sprite.Sprite.__init__(self)

        # Adicionando a posição da bala
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 0
        self.rect.y = random.randint(30, HEIGHT-60)

class Bala_rosa(pygame.sprite.Sprite):
    def __init__(self, img_bala_rosa):
        self.image = img_bala_rosa
        pygame.sprite.Sprite.__init__(self)

        # Adicionando a posição da bala
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 0
        self.rect.y = random.randint(30, HEIGHT-60)

class Bala_roxa(pygame.sprite.Sprite):
    def __init__(self, img_bala_roxa):
        self.image = img_bala_roxa
        pygame.sprite.Sprite.__init__(self)

        # Adicionando a posição da bala
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = WIDTH-WIDTH_bala
        self.rect.y = random.randint(30, HEIGHT-60)

class Bird(pygame.sprite.Sprite):
    def __init__(self, bird_img_dir, bird_img_esq):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.ultima_atualizacao = pygame.time.get_ticks()
        self.score = 0
        self.tempo_poder = pygame.time.get_ticks()
        self.cor = ''
        self.image = bird_img_dir
        self.image_dir = bird_img_dir
        self.image_esq = bird_img_esq
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT/2
        self.bird_speed_x = 0
        self.bird_speed_y = 0
        self.indo_direita = True

    def update(self):
        # Atualização da posição do passaro
        if self.cor == 'azul':
            now = pygame.time.get_ticks()
            if now - self.tempo_poder > 5000:
                self.cor = ''
            else:
                if self.bird_speed_x > 0:
                    self.rect.x += 5
                else:
                    self.rect.x -= 5
        if self.cor == 'rosa':
            now = pygame.time.get_ticks()
            if now - self.tempo_poder > 10000:
                self.cor = ''
            if self.rect.bottom > 610:
                self.rect.bottom = 610
            if self.rect.top < 40:
                self.rect.top = 40
            # if self.rect.right < HEIGHT - 30:
            #     self.rect.right = HEIGHT - 30
        if self.cor == 'roxa':
            now = pygame.time.get_ticks()
            if now - self.tempo_poder > 500:
                self.cor = ''
            else:
                self.score += 1
        self.rect.x += self.bird_speed_x
        self.rect.y += self.bird_speed_y

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        if self.rect.left < 0:
            self.rect.left = 0
        
        #Quando bater na parede
        if self.rect.x + self.rect.width >= 480:
            self.indo_direita = False
            self.bird_speed_x *= -1
            self.rect.x += self.bird_speed_x
            self.image = self.image_esq
            now = pygame.time.get_ticks()
            if now - self.ultima_atualizacao > 500:
                self.score += 1
                self.ultima_atualizacao = now
        if self.rect.x <= 0:
            self.indo_direita = True
            self.bird_speed_x *= -1
            self.rect.x += self.bird_speed_x
            self.image = self.image_dir
            now = pygame.time.get_ticks()
            if now - self.ultima_atualizacao > 500:
                self.score += 1
                self.ultima_atualizacao = now

        if aplica_gravidade:
            self.bird_speed_y += ACELERACAO
            self.rect.y += self.bird_speed_y
            self.rect.x += self.bird_speed_x


# Criando um grupo de espinhos
all_sprites = pygame.sprite.Group()
all_espinhos_e = pygame.sprite.Group()
all_espinhos_d = pygame.sprite.Group()
all_espinhos_cima = pygame.sprite.Group()
all_espinhos_baixo = pygame.sprite.Group()
all_espinhos = pygame.sprite.Group()
esp_e = pygame.sprite.Group()
esp_d = pygame.sprite.Group()
bala_azul = pygame.sprite.Group()
bala_rosa = pygame.sprite.Group()
bala_roxa = pygame.sprite.Group()
bala_laranja = pygame.sprite.Group()
player = Bird(bird_img_dir, bird_img_esq)
all_sprites.add(player)
balinha_azul = None
balinha_rosa = None
balinha_roxa = None

# Criando os espinhos da parede 1
if player.score <= 20:
    while len(all_espinhos_e) < 4:
        espinho = Espinho_lado_esquerdo(espinho_img_e)
        hits = pygame.sprite.spritecollide(espinho, all_espinhos_e, True)
        if len(hits) == 0:
            all_espinhos_e.add(espinho)
elif player.score > 20 and player.score <= 40: 
    while len(all_espinhos_d) < 6:
        espinho = Espinho_lado_direito(espinho_img_d)
        hits = pygame.sprite.spritecollide(espinho, all_espinhos_d, True)
        if len(hits) == 0:
            all_espinhos_d.add(espinho)

# Criando os espinhos da parede 
if player.score <= 20: 
    while len(all_espinhos_d) < 4:
        espinho = Espinho_lado_direito(espinho_img_d)
        hits = pygame.sprite.spritecollide(espinho, all_espinhos_d, True)
        if len(hits) == 0:
            all_espinhos_d.add(espinho)
elif player.score > 20 and player.score <= 40: 
    while len(all_espinhos_d) < 6:
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
    hits = pygame.sprite.spritecollide(balinha, esp_d, True, pygame.sprite.collide_mask)
    hits1 = pygame.sprite.spritecollide(balinha, esp_e, True, pygame.sprite.collide_mask)
    hits2 = pygame.sprite.spritecollide(balinha, all_espinhos_baixo, True, pygame.sprite.collide_mask)
    hits3 = pygame.sprite.spritecollide(balinha, all_espinhos_cima, True, pygame.sprite.collide_mask)
    if len(hits) == 0 and len(hits1) == 0 and len(hits2) == 0 and len(hits3) == 0:
        bala_azul.add(balinha)

# Criando bala rosa
while len(bala_rosa) < 1:
    balinha1 = Bala_rosa(img_bala_rosa)
    hits = pygame.sprite.spritecollide(balinha1, esp_d, True, pygame.sprite.collide_mask)
    hits1 = pygame.sprite.spritecollide(balinha1, esp_e, True, pygame.sprite.collide_mask)
    hits2 = pygame.sprite.spritecollide(balinha1, all_espinhos_baixo, True, pygame.sprite.collide_mask)
    hits3 = pygame.sprite.spritecollide(balinha1, all_espinhos_cima, True, pygame.sprite.collide_mask)
    if len(hits) == 0 and len(hits1) == 0 and len(hits2) == 0 and len(hits3) == 0: 
        bala_rosa.add(balinha1)

# Criando bala roxa
while len(bala_roxa) < 1:
    balinha2 = Bala_roxa(img_bala_roxa)
    hits = pygame.sprite.spritecollide(balinha2, esp_d, True, pygame.sprite.collide_mask)
    hits1 = pygame.sprite.spritecollide(balinha2, esp_e, True, pygame.sprite.collide_mask)
    hits2 = pygame.sprite.spritecollide(balinha2, all_espinhos_baixo, True, pygame.sprite.collide_mask)
    hits3 = pygame.sprite.spritecollide(balinha2, all_espinhos_cima, True, pygame.sprite.collide_mask)
    if len(hits) == 0 and len(hits1) == 0 and len(hits2) == 0 and len(hits3) == 0: 
        bala_roxa.add(balinha2)

# ----- Inicia estruturas de dados
game = True
clock = pygame.time.Clock()
FPS = 40
aplica_gravidade = False
ACELERACAO = 0.475


all_sprites.add(all_espinhos_cima)
all_sprites.add(all_espinhos_baixo)

all_espinhos.add(all_espinhos_cima)
all_espinhos.add(all_espinhos_baixo)

esp_e.add(all_espinhos_e)
esp_d.add(all_espinhos_d)
ba = pygame.sprite.Group()
brs = pygame.sprite.Group()
brx = pygame.sprite.Group()
tempo1 = pygame.time.get_ticks()
tempo2 = pygame.time.get_ticks()
tempo3 = pygame.time.get_ticks()
next_bala_azul = 7000
kill_bala_azul = 5000
next_bala_rosa = 5000
kill_bala_rosa = 5000
next_bala_roxa = 10000
kill_bala_roxa = 5000

# ===== Loop principal =====
pygame.mixer.music.play(loops=-1)
while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pulo_sound.play()
                player.bird_speed_y = -4
                if player.bird_speed_x < 0:
                    player.bird_speed_x = -4
                else:
                    player.bird_speed_x = 4
            aplica_gravidade = True

    all_sprites.update() 
    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    
    # Desenha e apaga os sprites das balas
    now1 = pygame.time.get_ticks()
    if balinha_azul == None:
        if now1 - tempo1 > next_bala_azul:
            balinha_azul = Bala_azul(img_bala_azul)
            next_bala_azul *= 2
            tempo1 = now1
            ba.add(balinha_azul)
    else:
        if now1 - tempo1 > kill_bala_azul:
            tempo1 = now1
            balinha_azul.kill()
            balinha_azul = None
    if balinha_rosa == None:
        if now1 - tempo2 > next_bala_rosa:
            balinha_rosa = Bala_rosa(img_bala_rosa)
            next_bala_rosa *= 2
            tempo2 = now1
            brs.add(balinha_rosa)
    else:
        if now1 - tempo2 > kill_bala_rosa:
            tempo2 = now1
            balinha_rosa.kill()
            balinha_rosa = None
    if balinha_roxa == None:
        if now1 - tempo3 > next_bala_roxa:
            balinha_roxa = Bala_rosa(img_bala_roxa)
            next_bala_roxa *= 2
            tempo2 = now1
            brx.add(balinha_roxa)
    else:
        if now1 - tempo3 > kill_bala_roxa:
            tempo2 = now1
            balinha_roxa.kill()
            balinha_roxa = None


    all_sprites.draw(window)

    hits = pygame.sprite.spritecollide(player, all_espinhos, True, pygame.sprite.collide_mask)
    if len(hits) != 0 and player.cor != 'rosa':
        game = False
    if player.indo_direita == True:
        hits = pygame.sprite.spritecollide(player, esp_d, True, pygame.sprite.collide_mask)
        if len(hits) != 0 and player.cor != 'rosa':
            game = False 
        esp_d.draw(window)
    else:
        for espinho in esp_d:
            espinho.kill()
        while len(esp_e) < 4:
            espinho = Espinho_lado_esquerdo(espinho_img_e)
            hits = pygame.sprite.spritecollide(espinho, esp_e, True, pygame.sprite.collide_mask)
            if len(hits) == 0:
                esp_e.add(espinho)

    if player.indo_direita == False:
        hits = pygame.sprite.spritecollide(player, esp_e, True, pygame.sprite.collide_mask)
        if len(hits) != 0 and player.cor != 'rosa':
            game = False
        esp_e.draw(window)
    else:
        for espinho in esp_e:
            espinho.kill()
            #criar lista da direita depois de bater
        while len(esp_d) < 4:
            espinho = Espinho_lado_direito(espinho_img_d)
            hits = pygame.sprite.spritecollide(espinho, esp_d, True, pygame.sprite.collide_mask)
            if len(hits) == 0:
                esp_d.add(espinho)

    # Pegando a bala azul
    hits = pygame.sprite.spritecollide(player, ba, True, pygame.sprite.collide_mask)
    if len(hits) > 0:
        player.cor = 'azul'
        player.tempo_poder = pygame.time.get_ticks()
        bala_sound.play()

    # Pegando a bala rosa
    hits = pygame.sprite.spritecollide(player, brs, True, pygame.sprite.collide_mask)
    if len(hits) > 0:
        player.cor = 'rosa'
        player.tempo_poder = pygame.time.get_ticks()
        bala_sound.play()

    # Pegando a bala roxa
    hits = pygame.sprite.spritecollide(player, brx, True, pygame.sprite.collide_mask)
    if len(hits) > 0:
        player.cor = 'roxa'
        player.tempo_poder = pygame.time.get_ticks()
        bala_sound.play()
    
    # Desenhando o score
    text_surface = fonte_score.render("{:05d}".format(player.score), True, (255, 255, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (WIDTH / 2,  40)
    window.blit(text_surface, text_rect)
    ba.draw(window)
    brs.draw(window) 
    brx.draw(window) 
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados



