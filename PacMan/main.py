from mapa import gerar_mapa, movimento
from fim import final
from player import jogador
from comida import comer
import time

if __name__=='__main__':
    while jogador.vivo:
        print("\033[H", end="")
        comer()
        gerar_mapa()
        movimento()
        final()
        time.sleep(0.05)