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
```

Imprimindo variáveis para saber seus tipos:

```
print( type(idade) )
print( type(altura) )
print( type(nome) )
print( type(Estudando) )
```

Como obter dados do usuário e salvá-los em variáveis

É importante chamar a entrada para uma variável criada, conforme abaixo:

```
#Obtendo dados do usuário e salvando em variáveis

linguagem = input('Qual é a linguagem de programação que você está estudando?')
print('A linguagem que você está estudando é', linguagem)
```


Neste caso, tudo que o usuário digitar neste input será armazenado na variável ‘linguagem’



Operações aritméticos e booleanos

# Operações matemáticas e aritméticas

```
Soma: +
Subtração: -
Multiplicação: *
Divisão: /
Divisão inteira: //
Resto da divisão: %
Potência: **

"""
numero1 = 10
numero2 = 20

print(numero1 + numero2) #a soma deu 200 e não 30 : necessário converter a variável de string para inteira
print(numero1 - numero2)
print(numero1 * numero2)
print(numero1 / numero2)
print(numero1 // numero2)
print(20 % 3)
print(2 ** 3)

#Operadores booleanos

idade1 = 10
idade2 = 15
altura1 = 1.77
altura2 = 1.65
altura3 = altura2

print(idade1 > idade2) #maior
print(idade1 <= idade2) #maior ou igual
print('Phyton' == 'phyton') #igual
print('banana' != 'abacaxi') #diferente
print(altura1 >= altura2) #maior ou igual
print(altura2 > altura3) #maior
```

as duas barras (//) é a divisão inteira, onde é descartada a parte decimal

Resto da divisão:

Se 20/3 dá 6, e o resto da divisão dá 2: 6/3 no caso

Sempre lembrar que operadores booleanos são operadores de comparação.

```
idade1 = 10
idade2 = 15
altura1 = 1.77
altura2 = 1.65
altura3 = altura2

print(idade1 > idade2) #maior
print(idade1 <= idade2) #maior ou igual
print('Phyton' == 'phyton') #igual
print('banana' != 'abacaxi') #diferente
print(altura1 >= altura2) #maior ou igual
print(altura2 > altura3) #maior
```

Quando eu sei que tipo de saída é float ou inteira ou booleana, eu devo informar ao python, senão ele sempre vai tratar a variável como string.


```
#Conversão de tipos

idade = '26'

print(idade, type(idade))

idade_inteira = int(idade) #aqui é o comando que converte a variável para inteira(int)

print(idade_inteira, type(idade_inteira))

# Usando a conversão de variável no input

altura = float( input('Informe a sua altura: '))

print(altura, type(altura))
      
var1 = 12

var2 = 30

var3 = var1 + var2

print(var3)

var3 = var3 * 2

print(var3)

```

Ele retorna informando que o tipo da variável é float.

Estruturas condicionais


Em relação a este fluxograma, imagine o seguinte: 
Queremos criar um código que verifique qual é a idade da pessoa e, com base na idade dela, informa se ela é maior de idade ou se ela não é maior de idade.
Passo 1: obter a idade da pessoa
Passo 2: fazer comparação - a idade é maior ou igual a 18? Ou seja, True, o programa vai imprimir: você é maior de idade! Se não for, ou seja, False, o programa vai imprimir: você é menor de idade!

```
#ESTRUTURAS CONDICIONAIS

idade = 20

if idade >= 18: 
    print('Você é maior de idade!')
else:
    print('Você é menor de idade!')

"""
Imagine que você queira imprimir "Aprovado(a)", caso o estudante tenha uma média superior ou igual a 7, e "Reprovado(a)", caso a média seja inferior a 7

"""

media = float(input('Informe a média do estudante'))

if media >= 7:
    print('Aprovado(a)')
elif media >= 5:        #Função elif equivale a else if no Java
    print('Recuperação')
else:
    print('Reprovado')
```
 
IF: SE
ELSE: DO CONTRÁRIO
ELIF (ELSE IF): QUANDO EU TENHO MAIS UM RESULTADO E CLASSIFICAÇÃO



Laços de repetição (While)

Quando é necessário repetir o mesmo trecho de código até que a condição seja satisfeita.

```
numero_sorteado = 15

numero_escolhido = int(input('Informe um número entre 1 e 20'))

while numero_escolhido != numero_sorteado:
    print('Você errou o número, tente novamente...')
    numero_escolhido = int(input('Informe um número entre 1 e 20:  '))

print('Parabéns, você acertou!')

#Mais um exemplo!

contador = 0

while contador < 5:
    print(contador)

    contador = contador + 1
```

Laços de repetição (For)

```
for variavel in range(10): # Esta variável dentro do range (faixa) de 10 valores
    print(variavel) #O range admite até 3 parâmetros
```

```
soma = 0

#Usando uma variável acumuladora


for i in range(1, 4):
    nota = float(input(f'Informe a sua nota 1 {1}: '))

    soma = soma + nota

print(soma/3)
```










Listas

Toda vez que se trata de lista, eu coloco os valores dentro de colchetes: [  ] 


