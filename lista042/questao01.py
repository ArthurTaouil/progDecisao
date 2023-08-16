'''
1. Fazer um algoritmo que peça um número, e ao final, informe se o número digitado está acima de 1000 ou
abaixo de 1000.
'''

num = int(input("Insira um número: "))

resposta = ("O número que você inseriu é menor ou igual a 1000", "O número que você inseriu é maior que 1000")[num > 1000]

print(resposta)