n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
operador = input('Digite o operador: ')

if operador == '+':
  print(n1 + n2)
elif operador == '-':
  print(n1 - n2)
elif operador == '*':
  print(n1 * n2)
elif operador == '/':
  print(n1 / n2)
else:
  print('Operador inválido')