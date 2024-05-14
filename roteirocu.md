# tutorial brabo de conversor pra faculdade atualizado 2.51.69

bom dia a todes, meu nome é ***[nome]***, vou explicar como funciona o código do conversor junto do meu grupo. Na primeira parte, nós colocamos as informações do grupo, como nome e RGM, logo embaixo adicionamos as opções para o usuário escolher, também com um input que receberá o valor desejado.
na segunda parte, começamos com a primeira função, que converte decimal para binário. primeiro, ele confere se o valor inserido é igual a 0, caso ele for, retorna-se 0, se não, ele cria uma variável *binario* que tem um valor vazio. depois, ele inicia um loop enquanto decimal for maior que 0, ele criará uma variável resto que dividirá o decimal por 2 e pegar o seu resto, depois esse valor é adicionado na variavél *binario* do lado esquerdo, e convertido para string, para construir o número da esquerda pra direita. o decimal, então, é dividido por 2 usando o *floor* , isso removerá o digito menos significativo do número decimal, preparando-o para a continuação do loop.

o sistema octal funciona da mesma for, só trocar o 2 por 8 ._.

na terceira, temos a conversão de decimal para hexadecimal, a lógica inicial é a mesma, a questão muda no resto, onde que, se o resto for menor que 10 ele prossegue normalmente, mas se for diferente disso, ele converte o valor para um Unicode (um esquema para conversão de caracteres em códigos ASCII), depois ele pega o valor do resto, subtraí 10 e soma com o Unicode de 'A', então ele adiciona o código a esquerda como os outros.

na quarta parte temos a conversão de binário para decimal. primeiramente, ele iguala duas variáveis (decimal e exponte) a 0, então ele inicia um loop, onde, bit (que é um número apenas), em reversed(binario), que é o número inserido ao contrário. 
depois o bit é convertido para inteiro e multiplicado pela pontencia de 2 sobre o expoente, que ao decorrer do loop aumentará 1.
mais uma vez, o sistema octal é a mesma coisa, só trocar o 2 por 8 ._.

na quinta parte, a conversão de hexadecimal para decimal, no começo é parecido com os demais, porém, na parte do loop, ele confere se o bit é um digito numérico, se for, ele segue a mesma lógica anterior. caso não, ele verifica se é uma letra de A até F, deixa o bit em maiúsculo, então converte para um valor decimal, subtraindo o valor do caractere A mais 10, depois ele multiplica pela potencia de 16 sobre o expoente.

por último, temos o loop de escolha, que deve ser maior que zero e menor que 7. é criada a variavel numero que recebera um valor, depois é criada uma condição caso o usuário queira fechar o programa, se o numero for N o programa encerra.
depois o programa passa um por um grande condicional para mostrar o resultado, tanto a conversão de decimal quanto o contrário são as praticamente as mesmas, primeiro ele confere se é um número, se for, ele cria uma variavel com o nome da base, aplica a função recebendo o número convertido em string, depois ele apresenta o texto com a conversão.