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
        # C:\Users\David Galhego\Desktop\Prog-1\trabalhar com arquivos\datatran2020.csv
        # ./trabalhar com arquivos/datatran2020.csv
    cont=0
    for i in conteudo:
        if 'Não Informado' in i:
            cont+=1
    print(f'Não foram informados {cont} dados em todo registro')
    


def questao_9():
    with open ('./trabalhar com arquivos/datatran2020.csv', 'r', encoding='utf-8') as acidentes_tot:
        # conteudo=acidentes_tot.readlines()
        # del conteudo[0]
        
        data = [linha.split(',') for linha in acidentes_tot]
        
        numero_de_nulos=0
        coluna_max_nulos=0
        
        for coluna in range(len(data[0])):
            cont=0
            for linha in range(len(data)):
                if data[linha][coluna] == 'Não Informado':
                    cont+=1
                    
            if cont > numero_de_nulos:
                numero_de_nulos= cont
                coluna_max_nulos= coluna
       
                        
    print(f"A coluna com mais dados não informados foi a coluna '{data[0][coluna_max_nulos]}' com {numero_de_nulos} dados não informados")
    
    
                
             
def questao_10():
    base= ler_datatran2020()        
    lista=base["feridos"]
    # for i in range(len(lista)):
    #     lista[i]=int(lista[i])
    # print('O maximo é ', max(lista))
    max_feridos=0
    indice_max=0
    for indice,feridos in enumerate(lista):
        feridos=int(feridos)
        if max_feridos<feridos:
            max_feridos=feridos
            indice_max=indice
            
        if 43 == feridos:
            print(feridos, indice)
        
        
            
            
    print(max_feridos)
    print(indice_max)
    print(f'O indice do acidente com mais feridos é {lista.index("44")}')
    print(f'O estado com o acidende com mais ferimentes é {base["uf"][lista.index("44")]}')
    

def questao_11():
    bd=ler_datatran2020()

    estados=set((bd['uf']))
    dic_estados_mortes={}
    dic_estados_media_mortes={}
    dic_estados_media_feridos={}
    dic_estados_media_ilesos={}
    
    
    for uf in estados:
        dic_estados_mortes[uf]=0
        dic_estados_media_feridos[uf]=0
        dic_estados_media_ilesos[uf]=0
        
    for uf in estados:
        
        
        for estado_atual, mortos in zip(bd['uf'], bd['mortos']):
            
            if uf == estado_atual:
                
                mortos=int(mortos)
                dic_estados_mortes[uf]+=mortos
            
        dic_estados_media_mortes[uf]= dic_estados_mortes[uf]/(bd['uf'].count(uf))
        
        
    
    for uf in estados:
        
        
        for estado_atual, feridos in zip(bd['uf'], bd['feridos']):
            
            if uf == estado_atual:
                
                feridos=int(feridos)
                dic_estados_media_feridos[uf]+=feridos
            
        dic_estados_media_feridos[uf]= dic_estados_media_feridos[uf]/(bd['uf'].count(uf))
    
    
    
    for uf in estados:
        
        
        for estado_atual, ilesos in zip(bd['uf'], bd['ilesos']):
            
            if uf == estado_atual:
                
                ilesos=int(ilesos)
                dic_estados_media_ilesos[uf]+=ilesos
            
        dic_estados_media_ilesos[uf]= dic_estados_media_ilesos[uf]/(bd['uf'].count(uf))
    
    
    
        
    print('A média de mortes por estado é a seguinte\n\n')   
    print(dic_estados_media_mortes)
    print('\n\n\nA média de feridos por estado é\n')
    print(dic_estados_media_feridos)
    print('\n\n\nA média de ilesos por estado é\n')
    print(dic_estados_media_ilesos)
    
    
    
    
def questao_12():
    bd=ler_datatran2020()
    estados=set((bd['uf']))
    estados.remove('MG')
    dic_acidentes_via_simples={}
    for estado in estados:
        dic_acidentes_via_simples[estado]=0
    for estado, tipo_via in zip(bd['uf'],bd['tipo_pista']):
        if tipo_via == 'Simples' and estado!='MG':
            dic_acidentes_via_simples[estado]+=1
    print(dic_acidentes_via_simples)
    
    print(f'O estado com mais acidentes em pistas simples é {max(dic_acidentes_via_simples, key = dic_acidentes_via_simples.get)} com {max(dic_acidentes_via_simples.values())} acidentes')
        
        
    
    
def questao_13():
    with open('./trabalhar com arquivos/datatran2020.csv', 'r', encoding='utf-8') as f:
        conteudo=f.readlines()
    conteudo[0]=conteudo[0].replace('data_inversa','data')
    conteudo=[linha.split(',') for linha in conteudo]
    
    for i in range(1,len(conteudo)) :
        teste=conteudo[i][1].split('-')
        teste.reverse()
        conteudo[i][1]=[teste[0],teste[1],teste[2]]
        
    sepador_virgula=','
    for i in range(1,len(conteudo)):
        
        conteudo[i][1]=sepador_virgula.join(conteudo[i][1])
        conteudo[i][1]=conteudo[i][1].replace(",",'-')
    for i in range(len(conteudo)):
        conteudo[i]=sepador_virgula.join(conteudo[i])
    with open('./trabalhar com arquivos/datatran2020_data_normal.csv', 'w', encoding='utf-8') as f:
        for linha in conteudo:
            f.write(linha)
        
            
    
        
        
def questao_14():
    bd=ler_datatran2020()
    dicio_acidentes_semana={}
    dias_semana=set(bd['dia_semana'])
    for dia in dias_semana:
        dicio_acidentes_semana[dia]=0
        
    for dia in bd['dia_semana']:
        dicio_acidentes_semana[dia]+=1
        
    
    total=sum(dicio_acidentes_semana.values())
    for dia in dicio_acidentes_semana:
        dicio_acidentes_semana[dia]=dicio_acidentes_semana[dia]/total
        dicio_acidentes_semana[dia]*=100
        dicio_acidentes_semana[dia]= round(dicio_acidentes_semana[dia],3)
        dicio_acidentes_semana[dia]=str(dicio_acidentes_semana[dia])+'%'
        
    
    print('A frquencia de acidentes por dia da semana é: \n\n\n')
    print(dicio_acidentes_semana)



def questao_15():
    bd=ler_datatran2020()
    
    for indice ,elemento in enumerate(bd['feridos']):
        bd['feridos'][indice]= int(elemento)
        
    bd['feridos'].sort()
    conjunto_feridos=set(bd['feridos'])

    
    dicio_feridos_por_acidente={}
    for i in conjunto_feridos:
        dicio_feridos_por_acidente[i]=0
        
    for elemento in bd['feridos']:
        dicio_feridos_por_acidente[elemento]+=1
    
    
    
    total=sum(dicio_feridos_por_acidente.values())
    cont=0
    for feridos in dicio_feridos_por_acidente:
        dicio_feridos_por_acidente[feridos]=dicio_feridos_por_acidente[feridos]/total
        dicio_feridos_por_acidente[feridos]*=100
        
        cont+=dicio_feridos_por_acidente[feridos]
        
        dicio_feridos_por_acidente[feridos]=cont
        dicio_feridos_por_acidente[feridos]= round(dicio_feridos_por_acidente[feridos],3)
        
        dicio_feridos_por_acidente[feridos]=str(dicio_feridos_por_acidente[feridos])+'%'
        
        
    print('O seguinte dicionário contém a frequencia acumulada de feridos por acidentes:\n\n\n')
    for feridos, quant in zip(dicio_feridos_por_acidente,dicio_feridos_por_acidente.values()):
        print(f'{feridos} : {quant} ')
        


        
    



questao_15()



    