import msvcrt
from const import matriz

class Player:

    def __init__(self, vivo, x, y):
        self.vivo = vivo
        self.x = x
        self.y = y

    def mov_jogador(self):

        if msvcrt.kbhit():
            try:
                direcao = msvcrt.getch().decode("utf-8").upper()    
                if direcao == 'D' and matriz[self.y][self.x+1] != '#':
                    self.x+=1
                elif direcao == 'A' and matriz[self.y][self.x-1] != '#':
                    self.x-=1
                elif direcao == 'W' and matriz[self.y-1][self.x] != '#':
                    self.y-=1
                elif direcao == 'S' and matriz[self.y+1][self.x] != '#':
                    self.y+=1
            except:
                pass
        if (self.x, self.y) == (1, 14):
            (self.x, self.y) = (25, 14)
        elif (self.x, self.y) == (26, 14):
            (self.x, self.y) = (2, 14)

jogador = Player(True, 14, 17)

if __name__=='__main__':
    print()