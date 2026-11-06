Pac-Man Terminal (Python)

https://github.com/user-attachments/assets/25c224c1-c232-4b2f-b02e-3c7103a396e8

Uma implementação simplificada e modular do clássico jogo Pac-Man, projetada para rodar diretamente no terminal utilizando Python.

Funcionalidades

Mapa em Terminal: Renderização limpa e contínua do labirinto sem o efeito de tela piscando (flickering), através do uso de códigos de escape ANSI.

Movimentação do Jogador: Controle em tempo real (W, A, S, D) via captura direta de teclas (msvcrt).

Sistema de Inimigos: Fantasmas autônomos com mecanismo básico para evitar movimentos repetitivos imediatos.

Mecânicas de Jogo:

Coleta de comidas.

Teletransporte através dos túneis laterais.

Condições de vitória (limpar o mapa) e derrota (colisão com fantasmas).

📁 Estrutura do Projeto

main.py — Loop principal do jogo e controle de execução.

const.py — Matriz representando a estrutura do labirinto.

player.py — Classe e lógica do jogador (Pac-Man).

Inimigos.py — Classe e lógica dos fantasmas.

comida.py — Geração e gerenciamento das pastilhas coletáveis.

mapa.py — Função responsável por desenhar o mapa e os elementos no terminal.

fim.py — Checagem de condições de fim de jogo (Vitória / Derrota).

⌨️ Controles

W: Mover para cima

S: Mover para baixo

A: Mover para a esquerda

D: Mover para a direita 
