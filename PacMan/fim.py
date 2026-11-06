from player import jogador
from Inimigos import inimigo1, inimigo2, inimigo3, inimigo4
from comida import coordscomida
listinimigs = [inimigo1, inimigo2, inimigo3, inimigo4]
def final():
    coordsinimigas = [(i.x, i.y) for i in listinimigs if i.vivo]
    if (jogador.x, jogador.y) in coordsinimigas:
        print('Você morreu')
        jogador.vivo = False
    elif len(coordscomida)<=0:
        print("Você venceu!")
        jogador.vivo=False
    

if __name__=='__main__':
    print()