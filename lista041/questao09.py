'''
9) Desenvolver um programa que pergunte um número e exiba a informação de que ele é positivo, negativo ou
nulo.
'''

num = int(input("Insira um número: "))

if ( num < 0 ):
    print("O valor inserido é negativo")
elif ( num == 0 ):
    print("O valor inserido é nulo")
else:
    print("O valor inserido é positivo")