'''
11) Desenvolver um programa que pergunte um número inteiro de 3 algarismos e apresente como resultado
somente o algarismo das centenas.
'''

num = int(input("Informe um número que possua 3 digitos: "))

if (num >= 100 and num <= 999 ):
    centenas = num // 100
    print(f"O algarismo das centenas de {num} e {centenas}")
else:
    print(f"O valor informado não possui 3 algarismos")