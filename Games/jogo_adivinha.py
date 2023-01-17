secreto = 'Gabriel'.upper()
digitadas = []
chances = 4

while True:
    if chances <= 0:
        print('Perdeu!')
        break

    letra = input('Digite uma letra -> ').upper()

    if len(letra) > 1:
        print('Ahhh isso não vale.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'A letra "{letra}" existe na palavra secreta.')
    else:
        print(f'A letra "{letra}" NÃO EXISTE na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'VOCÊ GANHOU!!! A palavra era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()