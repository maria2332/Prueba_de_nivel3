import random

baraja = [(numero, palo) for numero in range(1, 13) for palo in ('espada', 'basto', 'copa', 'oro')]
random.shuffle(baraja)

espadas = []
bastos = []
copas = []
oros = []

for carta in baraja:
    if carta[1] == 'espada':
        espadas.append(carta)
    elif carta[1] == 'basto':
        bastos.append(carta)
    elif carta[1] == 'copa':
        copas.append(carta)
    else:
        oros.append(carta)


espadas_ordenadas = sorted(espadas, key=lambda carta: carta[0])
