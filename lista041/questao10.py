'''
10) Desenvolver um programa que pergunte dois números inteiros, e apresente como resultado se o segundo
número informado é ou não um divisor do primeiro número informado
'''

num1 = int(input("Insira um número: "))
num2 = int(input("Insira outro número: "))

resto = num1 % num2

if( resto == 0 ):
    print("O segundo valor inserido é um divisor do primeiro valor")
else:
    print("O segundo valor inserido não é um divisor do primeiro valor")