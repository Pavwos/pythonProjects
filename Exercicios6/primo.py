num = int(input('Digite um número: '))

if num >= 1:
  for i in range(2, (num // 2)+1):
    if(num % i) == 0:
      print('Não é primo')
      break 
  else:
    print('É primo')