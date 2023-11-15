def menu():
    return int(input("""
    [1] Para Cadastrar
    [2] Para Listar
    [3] Buscar por nome
    [*] Digite qualquer outra coisa para encerrar
    Sua opção: """))



def cadastrar():

    nome= input("Digite o nome: ")
    telefone= input("Digite o numero de telefone: ")
    email = input("Digite o e-mail: ")
    with open('./trabalhar com arquivos/BD_Cadastro.txt', 'a', encoding="utf-8") as f:
        f.write(f"\n{nome},{telefone} ,{email}")
        

def formatar(linha):
    import re
    return re.sub("," , "\t\t\t", linha)

def listar():
    with open('./trabalhar com arquivos/BD_Cadastro.txt', 'r',encoding="utf-8") as f:
        lista = [formatar(linha) for linha in f]
        print(*lista)


def buscar_por_nome():
    busca = input("Digite a busca: ")
    with open('./trabalhar com arquivos/BD_Cadastro.txt', "r", encoding= "utf-8") as f:
        lista = [formatar(linha) for linha in f if linha.upper().startswith(busca.upper())]
        print(*lista)



def main():
    while True:
        print("\n")
        Op = menu()

        if Op == 1:
            print("\n")
            cadastrar()

        elif Op == 2:
            print("\n")
            listar()

        elif Op == 3:
            buscar_por_nome()

        else: 
            break     

main()       







