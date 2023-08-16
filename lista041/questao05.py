'''
5) Desenvolver um programa que pergunte 4 notas escolares de um aluno e exiba mensagem informando que o
aluno foi aprovado se a média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma
mensagem informando essa condição. Apresentar junto com a mensagem de aprovação ou reprovação o valor
da média obtida pelo aluno.
'''

nota1 = float(input("Qual é a sua nota do primeiro bimestre? "))
nota2 = float(input("Qual é a sua nota do segundo bimestre? "))
nota3 = float(input("Qual é a sua nota do terceiro bimestre? "))
nota4 = float(input("Qual é a sua nota do quarto bimestre? "))

media = ( nota1 + nota2 + nota3 + nota4 ) / 4

if ( media >= 5 ):
    print(f"Você foi aprovado! Sua média: {media}")
else:
    print(f"Infelizmente, você não foi aprovado. Sua média: {media}")