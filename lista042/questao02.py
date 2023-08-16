'''
2. Fazer um algoritmo que peça um número, e ao final, informe se o número está abaixo de 1000, entre 1000 e
5000, ou acima de 5000.
'''

num = int(input("Insira um número: "))

if ( num < 1000 ):
    print("O número que você inseriu é menor que 1000")
elif ( num >= 1000 and num < 5000):
    print("O número que você inseriu está entre 1000 e 5000")
else:
    print("O número que você] inseriu é maior que 5000")