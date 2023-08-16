'''
6) Desenvolver um programa que pergunte dois valores numéricos inteiros e apresente o valor da diferença entre o
maior valor e o menor valor lido.
'''

num1 = int(input("Insira um número: "))
num2 = int(input("Insira outro número: "))

diferenca = num1 - num2

if( num2 > num1 ):
    diferenca = num2 - num1

print(f"A diferença entre o maior e o menor valor é de {diferenca}")