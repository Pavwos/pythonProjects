#converter números binários

numeroBin = input('Digite um número: ')

decimal = 0

for i in range(len(numeroBin)):
    digito = int(numeroBin[i])
    decimal += digito * (2 ** (len(numeroBin) - 1 - i))
print(f'O número {numeroBin} em decimal é {decimal}')