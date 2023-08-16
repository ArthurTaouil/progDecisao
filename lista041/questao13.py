'''
Desenvolver um programa que pergunte 3 valores (variáveis a, b e c) e ao final apresente-os dispostos em ordem
crescente.
'''

a = int(input("Informe um valor para a: "))
b = int(input("Informe um valor para b: "))
c = int(input("Informe um valor para c: "))

# 1- a tem que ser menor que b

if ( a > b ):
    aux = a
    a = b
    b = aux

# garantido ate aqui que entre a e b, o menor esta em a

if ( a > c ):
    aux = a
    a = c
    c = aux

# garantido ate aqui que entre a e c menor dos 3
# agora  é necessario garantir que b seja menor que c

if ( b > c ):
    aux = b
    b = c
    c = aux

print(f"Ordem crescente: {a}, {b}, {c}.")