n1 = int(input('Digite um número: '))

soma = 0

for i in range(1, n1+1):
  if i % 2 == 0:
    soma += i

print(soma)
