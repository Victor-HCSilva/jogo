import pygame

def circles(screen, color: tuple = (250, 0, 0), pos: tuple = (20, 20), size: int = 40, quantity: int = 1, spacing: int = 20):
    """
    Desenha múltiplos círculos em uma linha, lado a lado, com espaçamento opcional.

    Args:
        screen (pygame.Surface): A superfície na qual os círculos serão desenhados.
        color (tuple, optional): A cor dos círculos em formato RGB. Padrão: (250, 0, 0).
        pos (tuple, optional): A posição do centro do primeiro círculo (x, y). Padrão: (20, 20).
        size (int, optional): O raio dos círculos. Padrão: 40.
        quantity (int, optional): O número de círculos a desenhar. Padrão: 1.
        spacing (int, optional): O espaçamento entre os centros dos círculos. Padrão: 0.
    """
    pos = pygame.Vector2(pos)

    for i in range(quantity):
        pygame.draw.circle(screen, color, pos, size)
        pos += pygame.Vector2(size + spacing, 0)  # Move para a direita (horizontalmente)



NEGRITO = True
ITALICO = True
FONTE_TAMANHO = 40
FONTE_NOME = 'arial'
mensagem = 'ola teste !!!'

def write_italic(font_size:int=20, bold:bool=True, italic:bool=True, message:str='None', color_text:tuple=(250,0,0)):
    '''21/01/2025
    Escreve na tela, de forma rápida
    Como usar: 
    Inicio do código:

    var1,var2 = write_italic(font_size=50,message='Estou usando a função de escrever!!')
    Final do loop 
    screen.blit(var1,var2)
    '''
    FONTE = pygame.font.Font(None, font_size)
    texto_formatado = FONTE.render(message, True, color_text)
    text_rect = texto_formatado.get_rect(topleft=(500, 500))  # Posição do texto

    if mensagem:
        return texto_formatado, text_rect

if __name__=='__main__':
    ...
    