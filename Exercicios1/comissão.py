#calcular a comissão de uma venda

comissao = float(input('Qual o valor do produto vendido? '))
porcentagem = float(input('Quanto de porcetagem você recebe por venda? '))

print(f'Você receberá {comissao*(porcentagem/100)} de comissão')