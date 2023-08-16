'''
8. Fazer um algoritmo que pergunte 3 números, e ao final, guarde na variável maior o maior destes 3 números
inseridos. O valor da variável maior deverá ser exibido ao final.
'''

n1 = int(input("Insira um número: "))
n2 = int(input("Insira outro número: "))
n3 = int(input("Insira o último númmero: "))

maior = n1

if(maior < n2):
    maior = n2

if(maior < n3):
    maior = n3

print(f"{maior} é o maior dos três números inseridos")