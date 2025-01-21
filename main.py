import pygame
from import_me import *

pygame.init()

screen = pygame.display.set_mode(SCREEN)
POSICAO = (screen.get_width() / 2, screen.get_height() / 2)
PLAYER_POS = pygame.Vector2(POSICAO)

NEGRITO = True
ITALICO = True
FONTE_TAMANHO = 40
FONTE_NOME = 'arial'
mensagem = 'ola teste !!!'

try:
    FONTE = pygame.font.SysFont(FONTE_NOME, FONTE_TAMANHO, bold=NEGRITO, italic=ITALICO)
except pygame.error:
    print(f"Erro ao carregar a fonte: {FONTE_NOME}. Usando a fonte padrão.")
    FONTE = pygame.font.Font(None, FONTE_TAMANHO, bold=NEGRITO, italic=ITALICO)

texto_formatado = FONTE.render(mensagem, True, WHITE)
text_rect = texto_formatado.get_rect(topleft=(500, 500))  # Posição do texto

message = '''
Ai nobras apelaumm
'''
    
teste, teste1 = write_italic(font_size=50, message=message)

# Variáveis do jogo
clock = pygame.time.Clock()
running = True

def circles(screen, color: tuple = (255, 0, 0), pos: tuple = (20, 20), size: int = 40, quantity: int = 1, spacing: int = 0):
    pos = pygame.Vector2(pos)
    for i in range(quantity):
        pygame.draw.circle(screen, color, pos, size)
        pos += pygame.Vector2(size + spacing, 0)  

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
    circles(screen, color=RED, pos=(50, 50), size=30, quantity=3)
    screen.blit(texto_formatado, text_rect)  # Desenha o texto na tela
    screen.blit(teste, teste1) 
    # Atualiza a tela
    pygame.display.flip()

pygame.quit()