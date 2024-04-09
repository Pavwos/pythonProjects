import math

# a = int(input('Digite o valor de a: '))
# b = int(input('Digite o valor de b: '))
# c = int(input('Digite o valor de c: '))

def get_Delta(a, b, c):
  return b**2 - 4*a*c

def baskhara(a, b, c):
  delta = get_Delta(a, b, c)
  if delta < 0:
    print('a equação não possuí raízes reais, tente novamente')
    return
  x1 = (-b + math.sqrt(delta))/2*a
  x2 = (-b - math.sqrt(delta))/2*a
  return x1, x2

baskhara(1, 0, 1)
result = baskhara(1, -5, 6)
print(result)