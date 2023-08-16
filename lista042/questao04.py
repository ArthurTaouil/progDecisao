'''
4. Fazer um algoritmo que peça um número de 1 a 7, e ao final, informe o dia da semana (por extenso)
correspondente ao número que foi inserido. Informar também a mensagem “número inválido” quando o
número inserido não corresponder à um dia da semana.
'''

num = int(input("Insira um número de 1 a 7: "))

if ( num == 1 ):
    print("O dia da semana correspondente ao número inserido é domingo")
elif ( num == 2 ):
    print("O dia da semana correspondente ao número inserido é segunda-feira")
elif ( num == 3 ):
    print("O dia da semana correspondente ao número inserido é terça-feira")
elif ( num == 4 ):
    print("O dia da semana correspondente ao número inserido é quarta-feira")
elif ( num == 5 ):
    print("O dia da semana correspondente ao número inserido é quinta-feira")
elif ( num == 6 ):
    print("O dia da semana correspondente ao número inserido é sexta-feira")
elif ( num == 7 ):
    print("O dia da semana correspondente ao número inserido é sábado")
else:
    print("O número que você inseriu não está entre 1 a 7")