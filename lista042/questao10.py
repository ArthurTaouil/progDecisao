'''
10. Fazer um algoritmo que pergunte o nome do aluno, e as notas das provas 1 e 2. Deverá ser exibida na tela
como resposta a média do aluno, e se ele está aprovado, reprovado ou em prova final. Estas condições
devem seguir as regras da tabela abaixo
'''

prova1 = float(input("Insira a nota de sua primeira prova: "))
prova2 = float(input("Insira a nota de sua segunda prova: "))
media = (prova1 + prova2) / 2

if (media < 3):
    print(f"Você está reprovado! {media} é a sua média")
elif(media >= 3 and media < 7):
    print(f"Você está de prova final! {media} é a sua média")
elif(media >= 7 and media <= 10):
    print(f"Você está aprovado! {media} é a sua média")
else:
    print("Nota inválida")