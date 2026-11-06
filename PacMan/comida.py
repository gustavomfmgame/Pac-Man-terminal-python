from const import matriz
from player import jogador
from Inimigos import inimigo1, inimigo2, inimigo3, inimigo4

listinimigs = [inimigo1,inimigo2,inimigo3,inimigo4]
coordscomida = set()

coordsinimigs = [(i.x, i.y) for i in listinimigs if i.vivo]

for i, linha in enumerate(matriz):
    for j, caractere in enumerate(linha):
        if (j, i) not in coordsinimigs and (j, i) != (jogador.x, jogador.y) and matriz[i][j] != '#' and (j,i)!=(1,14) and (j,i)!=(26,14):
            coordscomida.add((j,i))

def comer():
            coordscomida.discard((jogador.x, jogador.y))

if __name__=='__main__':
    print()