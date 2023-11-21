def ler_datatran2020():
    with open ('./trabalhar com arquivos/datatran2020.csv', 'r', encoding='utf-8') as f:
        data = [linha.split(',') for linha in f]
        colunas = data[0]
        bd = dict()
        for id, coluna in enumerate(colunas):
            bd[coluna] = [item[id] for item in data[1:]]

    return bd








def colunas():
     with open ('./trabalhar com arquivos/datatran2020.csv', 'r', encoding='utf-8') as f:
        data = [linha.split(',') for linha in f]
        print(data[0])
        return data[0]





def questao_01():
    base = ler_datatran2020()
    lista = base['fase_dia']
    valores = set (lista)
    print(valores)




def questao02_():
    base = ler_datatran2020()
    lista = base['fase_dia']
    chaves = set(lista)
    bd = dict()
    for ch in chaves:
        bd[ch] = 0

        for item in lista:
            if item == ch:
                bd[ch] += 1

    print(bd)






def questao_03():
    base = ler_datatran2020()
    lista = base['uf']
    chaves = set(lista)
    bd = dict()
    for ch in chaves:
        bd[ch] = 0

        for item in lista:
            if item == ch:
                bd[ch] += 1

    print(bd)







def questao_04():
    base = ler_datatran2020()
    lista_mortos = base['mortos']
    lista_uf = base['uf']
    cont=0
    for mortos , estado in zip(lista_mortos,lista_uf):
        if estado == "PA":
            cont += int(mortos)

    print(f"O número de mortes no pará foi de :{cont} mortos")





def questao_5():
    base=ler_datatran2020()
    lista_via=base['tipo_pista']
    lista_uf=set(base['uf'])
    
    bd=dict()
    for  estado in lista_uf:
        bd[estado] = 0
        
        for item, uf_atual in zip(lista_via,base['uf']):
            if item == "Dupla" and uf_atual==estado  :
                bd[estado]+=1
                
    for i in range(3):
        print(f'O {i+1}° estado com mais acidentes em via dupla é {max(bd, key = bd.get)} com {max(bd.values())} acidentes')
        del bd[max(bd, key = bd.get)]




def questao_06():
    base=ler_datatran2020()
    cont_acidentes=0
    bd_feridos=base['feridos']
    bd_ilesos=base['ilesos']
    for feridos, ilesos in zip(bd_feridos, bd_ilesos):
        if feridos>ilesos:
            cont_acidentes+=1
    print(f"O número de acidentes em que houve mais feridos do que ilesos é de {cont_acidentes}")




def questao_07():
    estados_norte = [',AM,' , ',PA,', ',MA,', ',AC,', ',RO,', ',TO,', ',AP,']
    with open ('./trabalhar com arquivos/datatran2020.csv', 'r', encoding='utf-8') as acidentes_tot:
        conteudo=acidentes_tot.readlines()
    with open ('./trabalhar com arquivos/datatran2020regiaonorte.csv', 'w', encoding='utf-8') as f:
        f.write(conteudo[0])
        for estado in estados_norte:
            for linha in conteudo:
                if estado in linha:
                    f.write(linha)
                    

                    

def questao_08():
    with open ('./trabalhar com arquivos/datatran2020.csv', 'r', encoding='utf-8') as acidentes_tot:
        conteudo=acidentes_tot.readlines()
    cont=0
    for i in conteudo:
        if 'Não Informado' in i:
            cont+=1
    print(f'Não foram informados {cont} dados em todo registro')
    

print(len(colunas()))
    