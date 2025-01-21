import pygame
from import_me import *

pygame.init()
screen = pygame.display.set_mode(SCREEN)
#imagem_personagem,retangulo_personagem = image("images/treated_images/image1.png", pos_x=300,pos_y=300, width=1000, height=550)
POSICAO = (screen.get_width() / 2, screen.get_height() / 2)
PLAYER_POS = pygame.Vector2(POSICAO)

#message = f'''PONTOS: {score.show_score_()}'''
#complemento,frase  = write(font_size=MIN_SIZE, message=message,posicao=TEXT_POSITION, color_text=WHITE )

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
    
    
    pygame.draw.circle(screen, RED, PLAYER_POS, 40)
    #screen.blit(complemento, frase) 
    #screen.blit(imagem_personagem, retangulo_personagem)
    pygame.display.flip()

#score.create_()
pygame.quit()