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