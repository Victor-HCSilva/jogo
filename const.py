import pygame

#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)
PINK = (255, 192, 203)
PURPLE = (128, 0, 128)
BROWN = (165, 42, 42)
GRAY = (128, 128, 128)
LIGHT_BLUE = (173, 216, 230)
DARK_GREEN = (0, 100, 0)

#SCREEN
COLOR_SCREEN = BLACK
WIDTH=1300
HEIGTH=800
SCREEN=(WIDTH, HEIGTH)

# objects
OBJECT = pygame.draw

#FONTS; TEXT
fonts = {
    'arial': 'arial',
    'times_new_roman': 'times new roman',
    'calibri': 'calibri',
    'verdana': 'verdana',
    'courier_new': 'courier new',
    'georgia': 'georgia',
    'tahoma': 'tahoma',
    'impact': 'impact',
    'comic_sans_ms': 'comic sans ms',
    'palatino_linotype': 'palatino linotype',
    'helvetica': 'helvetica',
    'bookman_old_style': 'bookman old style'
}

TEXT_POSITION = (30,30)
MAX_SIZE = 80
MED_SIZE = 60
MIN_SIZE = 30