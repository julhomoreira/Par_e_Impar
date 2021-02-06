nome = input('Qual é o seu nome? ')
usuario = float(input(f'{nome}, Que horas são? '))

if usuario >= 0 and usuario <= 11:
    print(f'Bom dia!')

elif usuario >= 12 and usuario <= 17:
    print('Boa tarde!')

elif usuario >= 18 and usuario <= 23:
    print('Boa noite')

else:
    print('Boa madrugada! ')



