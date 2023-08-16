'''
2) Desenvolver um programa que permita ao aluno responder qual a capital do Brasil. O programa deverá exibir se
a resposta está certa ou errada.
'''

capital = input("Qual é a capital do Brasil? ")
resposta = "brasília"

if ( capital == "brasília" or "brasilia" ):
    print("Sua resposta está correta!")
else:
    print("Sua resposta está incorreta!")