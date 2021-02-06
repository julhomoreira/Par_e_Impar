# contando quantas letras têm seu nome...

nome = input('Esceve aqui o seu primeiro nome: ')
cont = len(nome)

if cont <= 4:
    print(f'{nome}, Seu nome tem {cont} letras e é curto!')

elif cont >=5 and cont <= 6:
    print(f'{nome}, Seu nome tem {cont} e é normal!')

elif cont > 6:
    print(f'{nome}, Seu nome tem {cont} e é muito grande!')
else:
    print('Digite somente seu primeiro nome!')


