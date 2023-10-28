
def listar_cadastros(cadastros):
    if len(cadastros)==0:
        print("\n\nLista Vazia\n\n")
    for i in cadastros:
        print("===============================")
        print("Nome: ",i['Nome'])
        print("Nascimento: ",i['Nascimento'])
        print("Sexo: ",i['Sexo'])
        print("CPF: ",i['CPF'])
        print("RG: ",i['RG'])
       
       
       
        
        
def preencher_cadastro():
        print("\n\n")
        dicio={"Nome":input("Digite seu nome: "),
            "Nascimento":input('Digite seu ano de nascimento: '),
            "Sexo":input("Digite EM MAIÚSCULO F  (para feminino) ou M (masculino) para sexo biológico: " ), 
            "CPF":input("Digite seu CPF (Apenas os números): "),
            "RG":input("Digite o número de seu RG: ")}
        
        if dicio["Nome"]=='':
            
            raise Exception("Erro! Você precisa digitar seu Nome")
        
        
        elif  not dicio["Nascimento"].isdigit():
            
            raise Exception("Erro! O ano de nascimento é inválido")
        
        elif len(dicio["Nascimento"])!=4 or int(dicio["Nascimento"])>2023:
            
            raise Exception("Erro! O ano de nascimento é impossível")
        
        
        
        elif dicio["Sexo"] !='F' and dicio["Sexo"]!='M':
            
            raise Exception("Erro! O Sexo biológico é inválido")
        
        elif len(dicio["CPF"])!=11:
            
            raise Exception("Erro! Tamanho de CPF Inválido")
        
        elif  not dicio["CPF"].isdigit():
            
            raise Exception("Erro! O CPF é inválido ")
        
        elif len(dicio["RG"])!=7:
            
            raise Exception("Erro! Tamanho de RG Inválido")
        
        elif  not dicio["RG"].isdigit():
            
            raise Exception("Erro! O RG é inválido ")
        
        else:
            return dicio





        
def cadastrar(cadastros):
    try:
        cadastro=preencher_cadastro()
        
    except Exception as e:
        print(e)
        return "erro"
        
    else:
        cadastros.append(cadastro)
        print("\nCadastro Realizado com Sucesso\n")
            




cadastros=[]

while True:
    opcao=input("""
    Digite o número de sua escolha:
    1 - Cadastrar Perfil
    2 - Listar Cadastros
    Digite outra coisa para encerrar o programa
    Opcao: """)
    print("============================")
    if opcao == "1":
        while True: 
            erro=cadastrar(cadastros)
            if erro=='erro':
                escolha=input("Deseja tentar Cadastrar Novamente? [S/N]: ")
                if escolha=="S":
                    continue
                else:
                    break
                
            else:
                break
                
            
    elif opcao == '2':
        listar_cadastros(cadastros)
        continue
    
    else:
        break
    

print("Programa Encerrado")
            
        
    