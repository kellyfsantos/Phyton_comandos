# Phyton_comandos
Anotações sobre o curso Phyton do Zero ministrado na plataforma Ada Tech
Python do zero

Comandos básicos do Python:

print = saída
input = entrada

```
print('Hello World!')
print('Seja bem-vindo ao curso de Phyton do code tank')
input('Qual é a linguagem de programação que você está estudando?')
```


No caso do Python, para criar uma variável não é preciso descrever de qual tipo de variável se trata, porque o Python possui o chamado “tipagem dinâmica”

Relembrando:



No caso da variável booleana, as palavras ‘True’ e ‘False ’devem ser escritas com a primeira letra maiúscula. No Python existe o ‘Case Sentitive’.

Criando variáveis:

```
# Criando variáveis
idade = '26'
print(idade)
nome = 'Kelly Ferreira' 

#Variável int: números inteiros sem partes decimais
idade = 36

#Variável float: números reais com partes decimais
altura = 1.58

#Variável str: dados textuais (string)
nome = 'Kelly Ferreira'

#Variável bool: valores lógicos (True ou False)
Estudando = True

print( type(idade) )
print( type(altura) )
print( type(nome) )
print( type(Estudando) )

#Obtendo dados do usuário e salvando em variáveis

linguagem = input('Qual é a linguagem de programação que você está estudando?')
print('A linguagem que você está estudando é', linguagem)
```

Imprimindo variáveis para saber seus tipos:




Como obter dados do usuário e salvá-los em variáveis

É importante chamar a entrada para uma variável criada, conforme abaixo:



Neste caso, tudo que o usuário digitar neste input será armazenado na variável ‘linguagem’



Operações aritméticos e booleanos



as duas barras (//) é a divisão inteira, onde é descartada a parte decimal

Resto da divisão:

Se 20/3 dá 6, e o resto da divisão dá 2: 6/3 no caso

Sempre lembrar que operadores booleanos são operadores de comparação.







Quando eu sei que tipo de saída é float ou inteira ou booleana, eu devo informar ao python, senão ele sempre vai tratar a variável como string.




Ele retorna informando que o tipo da variável é float.

Estruturas condicionais


Em relação a este fluxograma, imagine o seguinte: 
Queremos criar um código que verifique qual é a idade da pessoa e, com base na idade dela, informa se ela é maior de idade ou se ela não é maior de idade.
Passo 1: obter a idade da pessoa
Passo 2: fazer comparação - a idade é maior ou igual a 18? Ou seja, True, o programa vai imprimir: você é maior de idade! Se não for, ou seja, False, o programa vai imprimir: você é menor de idade!

 
IF: SE
ELSE: DO CONTRÁRIO
ELIF (ELSE IF): QUANDO EU TENHO MAIS UM RESULTADO E CLASSIFICAÇÃO



Laços de repetição (While)

Quando é necessário repetir o mesmo trecho de código até que a condição seja satisfeita.






Laços de repetição (For)








Listas

Toda vez que se trata de lista, eu coloco os valores dentro de colchetes: [  ] 


