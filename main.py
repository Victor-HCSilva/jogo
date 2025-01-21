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

current_sprite_frame = 0
animation_speed = 16  # Ajustar a velocidade da animação (quanto menor, mais rápido)
animation_timer = 0
is_animating = False # Variável para controlar se a animação está ativa

POSICAO = (screen.get_width() / 2, screen.get_height() / 2)
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
            current_sprite_frame = (current_sprite_frame + 1) % len(sprite_images)  # Ciclo entre as imagens
    else:
        is_animating = False
        current_sprite_frame = 0  # Reinicia a animação para o primeiro frame quando não pressiona

    # Desenhar o sprite atual
    current_image, current_rect = sprite_images[current_sprite_frame]
    current_rect.center = PLAYER_POS  # Centralizar o sprite na posição do jogador
    screen.blit(current_image, current_rect)

    pygame.display.flip()

pygame.quit()