# Conversor de Bases Numéricas. Documentação

### O código é simples.
### Primeiro é apresentado os integrantes do grupo. Em seguida, uma mensagem de boas vindas e um pedido para o usuário escolher uma opção e um input para a escolha.

### Após isso, o programa guarda a decisão do usuário na variável escolha.
### Logo, o programa guarda várias funções que serão utilizadas mais tarde. Cada uma das funções segue um padrão lógico.

## Decimal para Binário e Octal.

### As funções de binário e octal seguem a mesma lógica.Primerio se cria a função com o parâmetro decimal, que será o valor escolhido. Depois vem um bloco de decisão, confere-se se o valor é 0, isso retornará 0, então ele mantém a variável 'binário' vazia.

### Um loop é criado para poder fazer a conversão. Primeiro, o loop é iniciado enquanto o valor decimal for maior que 0. Logo é coletado o resto da conta, que será 0 ou 1. Depois, o resto é concatenado à esquerda e somado à variável binário. Depois, o valor decimal é atualizado, sendo dividido por 2. Por último, quando o decimal virar 0, o loop se encerra e a variável binário é retornada. Essa lógica é a mesma aplicada no octal, apenas substituindo o 2 por 8.

## Decimal para Hexadecimal.

### O caso de decimal para hexadecimal é um pouco diferente, já que além de números, se incluí letras. O início do programa é o mesmo. No bloco de repetição é que se inicia as diferenças. É coletado o resto, dessa vez dividido por 16, e em seguida um bloco de decisão, ele confere que o resto é menor que 10, uma vez que 10 = A. Caso ele seja menor que dez, ele é concatenado ao valor, caso contrário, o valor concatenado será um conversor de ASCII, dentro dele, o resto será subtraído a 10 e depois adicionado à ordem 65, que é 'A' em ASCII, por exemplo, se resto for 10, o valor será 65, se for 11, o valor será 66, assim por diante.

## Binário e Octal para Decimal.

### O sistema de conversão Binário e Octal para Decimal são bem parecidos. Primeiro é aberta a função com o parâmetro da base numérica. Em seguida, é armazenado o valor do decimal e do expoente. Um loop é criado, bit, é um número apenas que foi coletado do decimal. O valor em binário é revertido para fazer sentido ao expoente. O loop começa com o decimal sendo adicionado ao valor de um bit multiplicado pelo expoente. Depois o expoente é somado 1 e assim ficará até terminar o valor completo.

## Hexadecimal para Decimal

### O sistema hexadecimal para decimal foi o mais desafiador. O início é o mesmo. Já no bloco de repetição, se cria uma condição para verificar se o bit é um dígito, caso for, ele é concatenado ao decimal. Caso ele for maior ou igual a 'A' e menor ou igual a 'F', ele vai obter o código ASCII do bit, calcular a diferença com o código do A e somar 10, para representar um número entre 10 e 15, depois é multiplicado por 16 que por sua vez, é adicionado um expoente que começa em 0. Em última instância, o programa lança um raise, que é uma exceção, no caso, de um erro onde o caracter inserido é inválido. Por último, o código adiciona mais um ao expoente e retorna o decimal.

## Mostrando a mensagem.

### Primeiro se coleta a escolha do usuário, 0 a 6. Caso seja 0 ou maior que 6, o programa é interrompido. Caso contrário, o programa entra em um bloco de decisão sobre a escolha. Para o primeiro caso (decimal para bin, oct ou hex), dentro desse bloco, existe mais um bloco de decisão para conferir se o que o usuário digitou foi um número (exceto no caso Hexadecimal), caso não, ele mostra uma mensagem de entrada inválida. Se não, ele segue para a mensagem, primeiro ele cria uma variável com o nome da base utilizada e adiciona ela à respectiva função. Dentro da função ele converte o número digitado para um inteiro. Logo é mostrado o valor original e o valor convertido.

### No segundo caso a única diferença é que inves de inteiro, ele é convertido para string.

## Como usar o conversor.

### Escolha qual conversão deseja fazer. Depois escolha o valor que deseja converter. Caso queira sair, digite 'N'.

## Não fazer!!

### O programa não suporta números negativos, números com virgula ou pontos.