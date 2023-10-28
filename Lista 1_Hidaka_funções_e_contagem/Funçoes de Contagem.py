#Alterado no github
#Alterado no Vscode
#Questão1 contagem================================
def contar_menor_que_num(lista,num):
    cont=0 
    for i in lista:
        
        if i<num:
            print(i)
            cont+=1
    return cont

# lista=[7,6,5,4,3,6,7,8,20,3,12]

# print(f"\n{contar_menor_que_num(lista,7)}")

#Questão2==============================================
def cont_maior_que_media_dada(lista,media):
    cont=0
    for i in lista:
        if i> media:
            cont+=1
    return cont

# lista=[8, 8.5, 10, 7.5, 3, 5.5, 4, 3.5]

# print(f"\n{cont_maior_que_media_dada(lista,8)}")

#Questão3==================================================
def achar_maior_altura(lista):
    return max(lista)

# lista=[1.7, 1.88, 1.5, 1.32, 1.68, 1.59]
# print(achar_maior_altura(lista))

#questão4===============================================
def calcular_media_notas_pares(lista):
    soma=0
    cont=0
    for i in lista:
        if i%2==0:
            soma+=i
            cont+=1
    return soma/cont

# lista=[5, 4, 8, 9, 10, 12, 4, 3, 7, 4]
# print(calcular_media_notas_pares(lista))

#Questão5==================================================
def freq_sequencia_basesN(lista,seq):
    cont=0
    for i in lista:
        if i==seq:
            cont+=1
    return cont

# lista=["TACG", "GAGC", "ATUC", "TAGC", "GAGC", "AACG", "TGAC"]
# print(freq_sequencia_basesN(lista,"TGAC"))

#questão6===================================================
def numero_de_elementos_até_a_soma(lista, num):
    soma=0
    cont=0
    for i in lista:
        if soma+i>num:
            break
        cont+=1
        soma+=i
    return cont

# lista=[6, 1, 3, 6, 7, 19]
# print(numero_de_elementos_até_a_soma(lista,5))

#Questão7====================================================
def sorteio_nelson(lista):
    pos=0
    cont=0
    for i in lista:
        pos+=1
        if pos == i:
            cont+=1
    return cont

# lista=[5, 4, 8, 9, 10, 12, 4, 3, 7, 4]
# print(sorteio_nelson(lista))

#Questão8==============================================
def contar_conceitos(lista):
    cont_E=0
    cont_B=0
    cont_R=0
    cont_I=0
    for i in lista:
        if i=="E":
            cont_E+=1
        elif i=="B":
            cont_B+=1
        elif i=="R":
            cont_R+=1
        elif i == "I":
            cont_I+=1
    return f'E = {cont_E}, B = {cont_B}, R = {cont_R}, I = {cont_I}'

# lista=["B"]
# print(contar_conceitos(lista))


#Questão9=======================================================
def avaliar_seguranca_lista(lista):
    muito_seguro=0
    seguro=0
    quase_inseguro=0
    inseguro=0
    for i in lista:
        if i == 0:
            muito_seguro+=1
        elif 1<=i<=3:
            seguro+=1
        elif 4<=i<=5:
            quase_inseguro+=1
        else:
            inseguro+=1
    return f""" Muito Seguro: {muito_seguro}\n Seguro: {seguro}\n Quase Inseguro: {quase_inseguro}
 Inseguro: {inseguro}"""

# lista=[1, 5, 6, 7, 3, 2, 2, 1, 0, 0, 0, 0]

# print(avaliar_seguranca_lista(lista))

#Questão10===================================================
def nome_com_Letra_inicial(lista,nome):
    lista_auxiliar=[]
    primeira_letra=nome[0].upper()
    for i in lista:
        if primeira_letra==(i[0].upper()):
            lista_auxiliar.append(i)
    return lista_auxiliar

# lista=["Ramon", "Arnaldo","Raquel", "Pedro", "Rafael"]
# print(nome_com_Letra_inicial(lista,"Regianne"))     

#questão11=================================================
def produtos_na_validade  (lista,num):
    lista_auxiliar=[]
    for i in lista:
        if i >= num:
            lista_auxiliar.append(i)
    return lista_auxiliar  

# lista=[5, 4, 3, 11, 1, 1, 8 ,10, 11, 3, 4, 2, 10]
# print("Produtos na validade:\n",sep=', ',*produtos_na_validade(lista,8) )


#Questão12=========================================
def saldo_positivo(lista_nomes,lista_saldo):
    lista_auxiliar=[]
    for i in range(len(lista_saldo)):
        if 0< lista_saldo[i]:
            lista_auxiliar.append(lista_nomes[i])
    return lista_auxiliar

# lista_nomes=[ "Arnaldo", "Raquel", "Pedro", "Rafael"]
# lista_saldo=[-120, -300, -956, 1200]
# print(saldo_positivo(lista_nomes,lista_saldo)) 


#Questão 13=================================================================
def produtos_na_validade(lista_validade,lista_produtos,num):
    lista_auxiliar=[]
    for item,indice in zip(lista_validade,range(len(lista_validade))):
        
        if item>=num:
            
            lista_auxiliar.append(lista_produtos[indice])
            lista_auxiliar.append(item)
    return lista_auxiliar

# lista_validade=[5, 4, 3, 11, 12, 1]
# lista_produtos=['AA', 'AB', 'BA', 'BB', 'CA', 'AC']
# resultado=produtos_na_validade(lista_validade,lista_produtos,8)


# print('Produtos na validade:') 
# for i in range(0,len(resultado),2):
#     print(resultado[i],":",resultado[i+1])       
        
#Questão14=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--==-=-=-

def filtrar_faixa_etaria(lista_nomes, lista_idades, faixa):
    lista_auxiliar=[]
    for i in range(len(lista_nomes)):
        if min(faixa)<=lista_idades[i]<=max(faixa):
            lista_auxiliar.append(lista_nomes[i])
    return lista_auxiliar

# lista_nomes=['Pedro', 'José', 'Maria', 'Marta', 'Natan', 'Henrique']
# lista_idades=[20, 18, 27, 29, 30, 32]    
# resultado=filtrar_faixa_etaria(lista_nomes,lista_idades,[20,30])

# for i in resultado:
#     print(i)

#Questão15=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def par_e_posiçao_par(lista):
    cont=0
    lista_auxiliar=[]
    for i in lista:
        cont+=1
        if i%2==0 and cont%2==0:
            lista_auxiliar.append(i)
    return lista_auxiliar

# lista=[1, 3, 4, 5, 6, 7, 8, 9 ]
# resultado=par_e_posiçao_par(lista)
# print(f"""Quantidade de números: {len(resultado)}
# Números: {resultado}""")


#Questão16=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def filtrar_nomes(lista, parte_nome):
    lista_auxiliar=[]
    tam_nome=len(parte_nome)
    pesquisa=parte_nome[:tam_nome]
    for i in lista:
        if i[:tam_nome]==pesquisa:  
            lista_auxiliar.append(i)
    return lista_auxiliar

lista=['Boris', 'Samara', 'Sabrina', 'Carlos', 'Samarone']
resultado=filtrar_nomes(lista,'Sa')
for i in resultado:
    print(i)
    
#Questão17=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def verificar_PA(lista):
    cont = lista[1]-lista[0]
    for i in range(len(lista)-1):
        if lista[i+1]-lista[i]!=cont:
            return "NÃO"
    return "SIM"

# lista=[1, 5, 9, 13, 17, 21, 25]
# print(verificar_PA(lista))
        
        

#Questão18=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def distancia_de_harming(lista1,lista2):
    cont=0
    for i in range(len(lista1)):
        if lista1[i]!=lista2[i]:
            cont+=1
    return cont

# lista1=[1, 0, 0, 1, 1, 0, 1, 0] 
# lista2=[1, 1, 1, 1, 1, 1, 1, 1]   
# print(distancia_de_harming(lista1,lista2))   
        
    



