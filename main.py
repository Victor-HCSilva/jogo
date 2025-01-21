import pygame
from import_me import *

pygame.init()
screen = pygame.display.set_mode(SCREEN)

POSICAO = (screen.get_width() / 2, screen.get_height() / 2)
PLAYER_POS = pygame.Vector2(POSICAO)

#message = f'''PONTOS: {score.show_score_()}'''
complemento,frase  = write(font_size=MIN_SIZE, message=message,posicao=TEXT_POSITION, color_text=WHITE )

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
    
    # Desenha elementos do jogo
    pygame.draw.circle(screen, RED, PLAYER_POS, 40)
    #circles(screen, color=RED, pos=(50, 50), size=30, quantity=3)
    screen.blit(complemento, frase) 
    # Atualiza a tela
    pygame.display.flip()

score.create_()
pygame.quit()