
# neste jogo você digita uma letra e o programa tenta adivihar qual é...

secreto = 'perfume'
lista_digitadas = []
chance = 3

while True:
    if chance <= 0:
        print('Você perdeu!!!')
        break

    letra = input('Digite uma letra: ')
    print('-*-'*10)

    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra')
        continue

    lista_digitadas.append(letra)

    if letra in secreto:
        print(f'Está indo bem, a letra "{letra}" existe. ')

    else:
        print(f'Affz... a letra "{letra}" NÃO EXISTE NA PALAVRA SECRETA.')
        lista_digitadas.pop()

    complemento = ''
    for letra_secreto in secreto:
        if letra_secreto in lista_digitadas:
            complemento += letra_secreto
        else:
            complemento += '*'

    if complemento == secreto:
        print(f'Que legal Você ganhouuu! A palavra era {complemento}')
        break
    else:
        print(f'A palavra secreta está assim: {complemento}')

    if letra not in secreto:
        chance -=1
        print(f'vccê ainda tem {chance} chances.')
    print('-~-'*10)




