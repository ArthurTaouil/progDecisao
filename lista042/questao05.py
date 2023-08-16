'''
5. Fazer um algoritmo que pergunte a sigla de um estado brasileiro (UF -> Unidade Federativa), e ao final,
informe na tela se o estado inserido está ou não na região Sudeste.
'''

sigla = input("Informe uma sigla de um estado do Brasil: ")

if ( sigla == "RJ", "SP", "MG", "ES"):
    print(f"{sigla} é a sigla de um estado da Região Sudeste")
else:
    print(f"{sigla} não é a sigla um estado da Região Sudeste")