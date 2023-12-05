def ler_arquivo(nomearquivo):
    with open (nomearquivo, 'r', encoding='utf-8') as arquivo:
        leitura=[linha.split(',') for linha in arquivo]
        colunas=leitura[0]
        dicio={}
        # print(colunas)
        for indice, coluna in enumerate(colunas):
            dicio[coluna]= [item[indice] for item in leitura[1:]]
        return dicio


#questao01

def questao_01(nomearquivo):
    with open (nomearquivo, 'r', encoding='utf-8') as arquivo:
        leitura=[linha.split(',') for linha in arquivo]
        colunas=leitura[0]
        dicio={}
        # print(colunas)
        for indice, coluna in enumerate(colunas):
            dicio[coluna]= [item[indice] for item in leitura[1:]]

        # print(dicio)

        estados=set(dicio['UF'])
        # print(estados)
        dicio_por_uf={}
        for estado in estados:
            dicio_por_uf[estado]=[]
            for uf, cidade in zip(dicio['UF'], dicio['Cidade\n']):
                if estado == uf:
                    dicio_por_uf[estado].append(cidade)

        


        
        return dicio_por_uf






import re

def questao_02(nomearquivo):
    dicio= ler_arquivo(nomearquivo)
    lista_final=[]
    
    for telefone, cpf in zip(dicio['Telefone'], dicio['CPF']):
        regex_tel= re.compile(r"\(\d{2}\)\s9\d{4}-\d{4}")
        regex_cpf = re.compile(r'\d{3}\.\d{3}\.\d{3}-\d{2}')
     
        if regex_tel.search(telefone) and regex_cpf.search(cpf):
            lista_final.append((telefone, cpf))

    return lista_final
    

print(questao_02('/home/aluno/Área de Trabalho/Prog_1 (David N)/Prova/arquivo.csv'))



def questao_03(nomearquivo):
    dicio=ler_arquivo(nomearquivo)
    estados= set(dicio["UF"])

    with open (nomearquivo, 'r', encoding='utf-8') as arquivo:
        leitura=[linha for linha in arquivo]

    dicio_cont={}
    for estado in estados:
        dicio_cont[estado]=0
        with open('/home/aluno/Área de Trabalho/Prog_1 (David N)/Prova/'+estado+'.cvs', 'w', encoding='utf-8') as novo_arquivo:
            novo_arquivo.write('')

        for linha in leitura:
            with open('/home/aluno/Área de Trabalho/Prog_1 (David N)/Prova/'+estado+'.cvs', 'a', encoding='utf-8') as novo_arquivo:
                if estado in linha:
                    dicio_cont[estado]+=1
                    novo_arquivo.write(linha)

    return dicio_cont

teste =questao_03('/home/aluno/Área de Trabalho/Prog_1 (David N)/Prova/arquivo.csv')

print(teste)