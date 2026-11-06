from Inimigos import inimigo1, inimigo2, inimigo3, inimigo4
from player import jogador
from const import matriz
from comida import coordscomida

def gerar_mapa():
    for i, linha in enumerate(matriz):
        for j, caractere in enumerate(linha):
            if (j,i) == (inimigo1.x, inimigo1.y):
                print('1', end=' ')
            elif (j,i) == (inimigo2.x, inimigo2.y):
                print('2', end=' ')
            elif (j,i) == (inimigo3.x, inimigo3.y):
                print('3', end=' ')
            elif (j,i) == (inimigo4.x, inimigo4.y):
                print('4', end=' ')
            elif (j,i) == (jogador.x, jogador.y):
                print('K', end=' ')
            elif (j,i) in coordscomida:
                print('.', end=' ')
            else:
                print(caractere, end=' ')
        print()

def movimento():
    if inimigo1.delay>=4:
        inimigo1.mover()
        inimigo2.mover()
        inimigo3.mover()
        inimigo4.mover()
        inimigo1.delay=0
    inimigo1.delay+=1
    jogador.mov_jogador()
        

if __name__=='__main__':
    print()