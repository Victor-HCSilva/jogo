import pygame
from import_me import *

pygame.init()
screen = pygame.display.set_mode(SCREEN)

# Carregar as imagens do sprite
sprite_images = [
    image("images/treated_images/image1.png", width=1000, height=550),  # Ajuste width e height conforme necessário
    image("images/treated_images/image4.png", width=1000, height=500),
    image("images/treated_images/image5.png", width=1000, height=500),
    image("images/treated_images/image2.png", width=1000, height=550),
    image("images/treated_images/image3.png", width=1000, height=550),
]
Y_PROJETIL = 400
bola = image(name_image="images/bolinha.png", width=100, height=55, pos_x=X_PROJETIL, pos_y=Y_PROJETIL ),
bola = bola[0]#removendo primeira tupla
reta = bola[1]#pegando primeiro valor
bola = bola[0] #pegando segundo valor


current_sprite_frame = 0
animation_speed = 16  # Ajustar a velocidade da animação (quanto menor, mais rápido)
animation_timer = 0
is_animating = False # Variável para controlar se a animação está ativa

POSICAO = (X_PLAYER , Y_PLAYER)
PLAYER_POS = pygame.Vector2(POSICAO)

running = True

# Loop principal do jogo
while running:
    screen.fill(COLOR_SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Movimentação do jogador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        PLAYER_POS.y -= SPEED * CLOCK
    if keys[pygame.K_s]:
        PLAYER_POS.y += SPEED * CLOCK
    if keys[pygame.K_a]:
        PLAYER_POS.x -= SPEED * CLOCK
    if keys[pygame.K_d]:
        PLAYER_POS.x += SPEED * CLOCK
    
    # Lógica da Animação com Espaço
    if keys[pygame.K_SPACE]:
        is_animating = True
        animation_timer += 1
        if animation_timer >= animation_speed:
            animation_timer = 0
            current_sprite_frame = (current_sprite_frame + 1) % len(sprite_images)  
    else:
        is_animating = False
        current_sprite_frame = 0  

    #ataque

    # Desenhar o sprite atual
    current_image, current_rect = sprite_images[current_sprite_frame]
    current_rect.center = PLAYER_POS  

    screen.blit(bola, reta)
    screen.blit(current_image, current_rect)
    
    pygame.display.flip()

pygame.quit()