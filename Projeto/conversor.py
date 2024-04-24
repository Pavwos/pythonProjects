print('------Integrantes do grupo-------')
print('Nome: João da Silva, RGM: 6969420')
print('Nome: Maria da Sila, RGM: 6969696')
print('Nome: Jorge da Sila, RGM: 4206942')
print('Nome: Maira da Sila, RGM: 4204206')
print('------Integrantes do grupo-------')
print('')
print('Seja bem vindo ao nosso sistema de conversão de bases.')
print('Por favor, escolha uma opção: ')
print('1 - Converter Decimal para Binário')
print('2 - Converter Decimal para Hex')
print('3 - Converter Decimal para Octal')
print('4 - Converter Binário para Decimal')
print('5 - Converter Hex para Decimal')
print('6 - Converter Octa para Decimal')
print('0 - Parar')
escolha = int(input('Digite a opção: '))


# Decimal para Binário
def dec_to_bin(decimal):
    if decimal == 0:
        return '0'
    binario = ''
    while decimal > 0:
        resto = decimal % 2
        binario = str(resto) + binario
        decimal = decimal // 2
    return binario


# Decimal para Octal
def dec_to_oct(decimal):
    if decimal == 0:
        return '0'
    octal = ''
    while decimal > 0:
        resto = decimal % 8
        octal = str(resto) + octal
        decimal = decimal // 8
    return octal


# Decimal para Hexadecimal
def dec_to_hex(decimal):
    if decimal == 0:
        return '0'
    hexadecimal = ''
    while decimal > 0:
        resto = decimal % 16
        if resto < 10:
            hexadecimal = str(resto) + hexadecimal
        else:
            hexadecimal = chr(resto - 10 + ord('A')) + hexadecimal
        decimal = decimal // 16
    return hexadecimal


# Binário para Decimal
def bin_to_dec(binario):
    decimal = 0
    expoente = 0
    for bit in reversed(binario):
        decimal += int(bit) * (2**expoente)
        expoente += 1
    return decimal


# Hexadecimal para Decimal
def hex_to_dec(hexadecimal):
    decimal = 0
    expoente = 0
    for bit in reversed(hexadecimal):
        if bit.isdigit():
            decimal += int(bit) * (16**expoente)
        else:
            decimal += (ord(bit.upper()) - ord('A') + 10) * (16**expoente)
        expoente += 1
    return decimal


# Octal para Decimal
def oct_to_dec(octal):
    decimal = 0
    expoente = 0
    for bit in reversed(octal):
        decimal += int(bit) * (8**expoente)
        expoente += 1
    return decimal


while escolha > 0:
    numero = input('Digite o número que deseja converter: ')

    if escolha == 1:
        print('-----Decimal para Binário-----')
        binario = dec_to_bin(numero)
        print(f'O valor {numero} em binário é: {binario}')
        print('-----Decimal para Binário-----')
    elif escolha == 2:
        print('-----Decimal para Hexadecimal-----')
        hexadecimal = dec_to_hex(numero)
        print(f'O valor {numero} em hexadecimal é: {hexadecimal}')
        print('-----Decimal para Hexadecimal-----')
    elif escolha == 3:
        print('-----Decimal para Octal-----')
        octal = dec_to_oct(numero)
        print(f'O valor {numero} em octal é: {octal}')
        print('-----Decimal para Octal-----')
    elif escolha == 4:
        print('-----Binário para Decimal-----')
        decimal = bin_to_dec(str(numero))
        print(f'O valor {numero} em decimal é: {decimal}')
        print('-----Binário para Decimal-----')
    elif escolha == 5:
        print('-----Hexadecimal para Decimal-----')
        decimal = hex_to_dec(str(numero))
        print(f'O valor {numero} em decimal é: {decimal}')
        print('-----Hexadecimal para Decimal-----')
    elif escolha == 6:
        print('-----Octal para Decimal-----')
        decimal = oct_to_dec(str(numero))
        print(f'O valor {numero} em decimal é: {decimal}')
        print('-----Octal para Decimal-----')