idade = int(input('Qual a sua idade?: '))

if idade < 16:
  print('Você não é eleitor!')
elif idade >= 18 and idade <= 65:
  print('Você é eleitor obrigatório!')
elif idade > 65 or idade >= 16 and idade < 18:
  print('Você é eleitor facultativo!')
else:
  print('???')