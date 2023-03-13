# Este é um jogo de adivinhar o número.

import random  # importa pacote random

numerosecreto = random.randint(1, 20)  # gera um numero interiro  de 1 a 20

print('Estou pensando em um número entre 1 e 20.')

# o jogador tem 6 chances para acertar

for adivinhe in range(1, 7):
    print('adivinhe ?')
    adv = int(input())
    if adv < numerosecreto:
        print('seu numero é menor')
    elif adv > numerosecreto:
        print('seu numero é maior')
    elif adv == numerosecreto:
        print('bom trabalho, você acertou na ' + str(adivinhe) + ' tentativa!')
        break
else:
    print('desculpe , mas o número é' + str(numerosecreto))
