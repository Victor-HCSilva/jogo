import pygame

SPEED = 300 #NORMAL
TICK = 300 #QUANTO MAIOR, MAIS LENTO
CLOCK = pygame.time.Clock().tick(TICK) / 1000
SCORE = 1

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
    p = SaveConfigs('pontos', SCORE)
    p.save_()
    print(p.show_score_())