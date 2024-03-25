print('')
segunda = int(input('Trabalhou segunda?(0 para não, 1 para sim) '))
quarta = int(input('Trabalhou quarta?(0 para não, 1 para sim) '))
sexta = int(input('Trabalhou sexta?(0 para não, 1 para sim) '))
print('')

dias = segunda + quarta + sexta

if dias == 1:
  print('José comprou uma tv de tubo')
elif dias == 2:
  print("José comprou uma tv de 32'")
elif dias == 3:
  print('José comprou uma tv 4k')
else:
  print('José comprou nada :(')