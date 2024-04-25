# Conversor de Decimal para Bases Numéricas e vice versa

### O código é simples.
### Primeiro é apresentado os integrantes do grupo. Em seguida, uma mensagem de boas vindas e um pedido para o usuário escolher uma opção e um input para a escolha.

### Após isso, o programa guarda a decisão do usuário na variável escolha.
### Logo, o programa guarda várias funções que serão utilizadas mais tarde. Cada uma das funções segue um padrão lógico.

# Decimal para Binários e Octais.

### As funções de binário e octal seguem a mesma lógica.Primerio se cria a função com o parâmetro decimal, que será o valor escolhido. Depois vem um bloco de decisão, confere-se se o valor é 0, isso retornará 0, então ele mantém a variável 'binário' vazia.

### Um loop é criado para poder fazer a conversão. Primeiro, o loop é iniciado enquanto o valor decimal for maior que 0. Logo é coletado o resto da conta, que será 0 ou 1. Depois, o resto é concatenado à esquerda e somado à variável binário. Depois, o valor decimal é atualizado, sendo dividido por 2. Por último, quando o decimal virar 0, o loop se encerra e a variável binário é retornada. Essa lógica é a mesma aplicada no octal, apenas substituindo o 2 por 8.

## Decimal para Hexadecimal.

### O caso de decimal para hexadecimal é um pouco diferente, já que além de números, se incluí letras. O início do programa é o mesmo. No bloco de repetição é que se inicia as diferenças. É coletado o resto, dessa vez dividido por 16, e em seguida um bloco de decisão, ele confere que o resto é menor que 10, uma vez que 10 = A. Caso ele seja menor que dez, ele é concatenado ao valor, caso contrário, o valor concatenado será um conversor de ASCII, dentro dele, o resto será subtraído a 10 e depois adicionado à ordem 65, que é 'A' em ASCII, por exemplo, se resto for 10, o valor será 65, se for 11, o valor será 66, assim por diante.



# Como usar o conversor.