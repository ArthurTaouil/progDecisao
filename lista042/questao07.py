'''
7. Fazer um algoritmo que pergunte 2 números, e ao final, exiba como resposta na tela qual é o maior e qual é
o menor, ou ainda, se ambos são iguais.
'''

n1 = int(input("Insira um número: "))
n2 = int(input("Insira outro número: "))

maior = n1

if (maior < n2):
    maior = n2

menor = n2

if(menor > n1):
    menor = n1

if(menor < maior):
    print(f"{maior} é maior que {menor}")
else:
    print(f"Os dois números inseridos são iguais")