valor = int(input('Digite o valor do produto: '))

if valor >= 200:
    print(f'Você ganhou um desconto de 20%. Você pagará {valor*0.8}')
else:
    print('Você não teve desconto')