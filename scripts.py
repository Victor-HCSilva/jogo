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

def write(font_size:int=20, bold:bool=True, italic:bool=True, message:str='None', color_text:tuple=(250,0,0), posicao:tuple=(500,500)):
    '''21/01/2025
    Escreve na tela, de forma rápida
    Como usar: 
    Inicio do código:

    var1,var2 = write(font_size=50,message='Estou usando a função de escrever!!')
    Final do loop 
    screen.blit(var1,var2)
    '''
    FONTE = pygame.font.Font(None, font_size)
    texto_formatado = FONTE.render(message, True, color_text)
    text_rect = texto_formatado.get_rect(topleft=posicao)  # Posição do texto

    if message:
        return texto_formatado, text_rect

import pygame

def image(name_image: str = 'image.png', pos_x: int = 0, pos_y: int = 0, width: int = 100, height: int = 100, redimensionar:bool=True):
    """
    Carrega, posiciona e redimensiona uma imagem. Retorna a imagem e seu retângulo ou mensagens de erro.
    Uso:
    bola = image(name_image="images/bolinha.png", width=1000, height=550, pos_x=300, pos_y=300 ),
    bola = bola[0]#removendo primeira tupla
    reta = bola[1]#pegando primeiro valor
    bola = bola[0] #pegando segundo valor

    screen.blit(bola, reta)

    """
    
    if not isinstance(name_image, str) or not name_image:
         return "Erro: Nome da imagem inválido."
    if not isinstance(pos_x, int) or not isinstance(pos_y, int):
        return "Erro: Posições X e Y devem ser números inteiros."
    if not isinstance(width, int) or not isinstance(height, int) or width <= 0 or height <= 0:
        return "Erro: Largura e altura devem ser números inteiros positivos."

    try:
        imagem = pygame.image.load(name_image)
        retangulo = imagem.get_rect()
        retangulo.x = pos_x
        retangulo.y = pos_y

        if redimensionar:
            imagem_redimensionada = pygame.transform.scale(imagem, (width, height))
            return imagem_redimensionada, retangulo
        return imagem, retangulo
    except pygame.error as e:
        return f"Erro ao carregar a imagem: {e}"


class SaveConfigs():
    def __init__(self, file, score):
        self.file = '.'+file
        self.score = score

    def save_(self):
        try:#tenta ler antes
            with open(self.file, mode='r') as file:
                context = file.read()
                #pega o valor existente e soma
                self.score+=int(context)

            #salva novamente somado
            with open(self.file, mode='w') as file:
                file .write(f'{self.score}')

        except:#se não existir cria
            with open(self.file, mode='w') as file:
                file.write(f'{self.score}')

    def show_score_(self):
        return self.score
    
if __name__=='__main__':
    bola = image(name_image="images/bolinha.png", width=1000, height=550, pos_x=300, pos_y=300 ),
    bola = bola[0]
    reta = bola[1]
    bola = bola[0] 
    