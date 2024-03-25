import math

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))
delta = b**2 - 4*a*c

#fazer sem else
if delta < 0:
  print('a equação não possuí raízes reais, tente novamente')
else:
  x1 = (-b + math.sqrt(delta))/2*a
  x2 = (-b - math.sqrt(delta))/2*a

  print(f'O valor do x1 é de {x1} e do x2 de {x2}.')