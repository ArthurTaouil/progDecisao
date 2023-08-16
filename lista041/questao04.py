'''
4) Desenvolver um programa que pergunte um valor numérico inteiro e faça a exibição desse valor caso seja
divisível por 4 e 5. Não sendo divisível por 4 e 5, o programa deverá exibir a mensagem “Valor não é divisível por
4 e 5”.
'''

num = int(input("Insira um valor número inteiro: "))

resto4 = num % 4
resto5 = num % 5

if( resto4 == 0 and resto5 == 0 ):
    print("O valor inserido é divisível por 4 e 5")
else:
    print("O valor inserido não é divisível por 4 e 5")