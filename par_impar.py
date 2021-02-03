

nome = input('Digite seu nome: ')
usua1 = input('Agora Digite um número inteiro: ')

if usua1.isdigit():
    usua1 = int(usua1)

    if usua1 % 2 == 0:
        print('='*10)
        print(f'{nome} digitou o número {usua1} e é PAR.')
    else:
        print('='*10)
        print(f'{nome} digitu o número {usua1} e é ÍMPAR.')

else:
    print('-*-' * 20)
    print('Entada incorreta! Por favor, digite somente números inteiros!')

