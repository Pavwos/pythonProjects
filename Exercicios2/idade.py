#calcular o tempo de vida

ano = int(input('Digite sua idade atual: '))
mes = int(input('Há quantos meses foi seu aniversário?: '))
dia = int(input('Há quantos dias foi seu aniversário?: '))

total = (ano * 365) + (mes * 30) + dia

print(f'Você tem {total} dias de vida.')