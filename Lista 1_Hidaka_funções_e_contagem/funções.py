# Aula 16/09/2023======================================================
def mapear_inteiro(elemento):

    X1 = str(elemento)
    indice = X1.index('.')
    x3 = int(X1[indice+1:])
    if x3 % 2 == 0:
        return int(elemento)
    else:
        return elemento//1+1


def calcular_tamanho_nomes(lista):
    return [len(item) for item in lista]


def transformar_real_inteiro(lista):
    return [mapear_inteiro(item) for item in lista]


def mapear_3_1(lista1, lista2, lista3):
    return [max(item)+min(item)
            for item in zip(lista1, lista2, lista3)]


def construir_lista_palindromo(lista):
    return [x
            for x, y in zip(lista, lista[::-1])
            if x == y]


def encontrar_maior_string(lista):
    """Dada uma lista de string, faz uma redução para determinar o tamanho da
maior string. Retorna o valor encontrado e o índice correspondente na lista. Se mais de
uma string possuir o maior tamanho, retorna o menor índice."""

    dicionario = {'Valor': '',
                  'Indice': 0,
                  'Tamanho': 0}

    for item in lista:
        if len(item) > len(dicionario['Valor']):
            dicionario['Valor'] = item
            dicionario['Indice'] = lista.index(item)
            dicionario['Tamanho'] = len(item)

    return dicionario

# =====================================================================
# Lista 1 Hidaka


def concatenar_elementos_listas(lista1, lista2):
    """
    Cria uma lista de strings, a partir de 2 listas existentes em que cada elemento da
    lista final vai ser a concatenação dos elementos de mesmo indice das listas do argumento

    Argumento:
    Duas listas de strings

    Retorno:
    Uma lista de strings concatenadas
    """
    lista_auxiliar = []
    for x, y in zip(lista1, lista2):
        lista_auxiliar.append(x+y)
    return lista_auxiliar


def concatenar_elementos_listas_min(lista1, lista2):
    """
    Cria uma lista de strings, a partir de 2 listas existentes em que cada elemento da
    lista final vai ser a concatenação dos elementos de mesmo indice das listas do argumento

    Argumento:
    Duas listas de strings

    Retorno:
    Uma lista de strings concatenadas
    """
    return [x+y for x, y in zip(lista1, lista2)]


# Questão 2===============================================

def lista_primos_maiores(lista):
    """
    Dada uma lista de numeros inteiros, cria uma lista formada pelos menores numeros primos que são maiores que os numeros de mesmo indice
    da lista original

    Argumentos:
    lista de inteiros

    retorno:
    lista de inteiros de numeros primos 

    """
    lista_auxiliar = []
    for item in lista:
        while True:
            item += 1
            cont = 0

            for i in range(1, item+1):
                if item % i == 0:
                    cont += 1
            if cont == 2:
                lista_auxiliar.append(item)
                break
    return lista_auxiliar


def verificar_primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        return True


def calcular_proximo_primo(item):
    while True:
        item += 1
        if verificar_primo(item) == True:
            break
    return item


def lista_primos_maiores_min(lista):
    """
    Dada uma lista de numeros inteiros, cria uma lista formada pelos menores numeros primos que são maiores que os numeros de mesmo indice
    da lista original

    Argumentos:
    lista de inteiros

    retorno:
    lista de inteiros de numeros primos 

    """
    return [calcular_proximo_primo(item) for item in lista]


# questão3=============================================================
def filtrar_string_menor_10(lista):
    """Ao receber uma lista de Strings, retorna uma lista em ordem alfabetica das Strings de tamanho menor que 10
    """
    lista_auxiliar = []
    for item in lista:
        if len(item) <= 10:
            lista_auxiliar.append(item)
    lista_auxiliar.sort()
    return lista_auxiliar


def filtrar_string_menor_10_min(lista):
    """Ao receber uma lista de Strings, retorna uma lista em ordem alfabetica das Strings de tamanho menor que 10
    """
    return sorted([item for item in lista if len(item) <= 10])


# Questão 4========================================================================

def filtrar_inteiros_de_matriz(lista):
    """Recebe uma matriz e retorna a matriz filtrada para apenas elementos do tipo int
    """
    lista_auxiliar_maior = []

    for item in lista:
        lista_auxiliar_maior.append(filtrar_por_tipo(item, int))

    return lista_auxiliar_maior


def filtrar_por_tipo(lista, tipo):
    return [item for item in lista if type(item) == tipo]


def filtrar_inteiros_de_matriz_min(lista):
    """Recebe uma matriz e retorna a matriz filtrada para apenas elementos do tipo int
    """

    return [filtrar_por_tipo(item, int) for item in lista]


# Questão 5========================================================

def filtro_string_tamanho(listaS, listaI):
    """Função que para uma lista de strings e outra de inteiros, faz uma filtragem para que apenas
    as strings de tamanho menor ou igual ao inteiro de mesmo indice da respectiva string.
    """
    lista_auxiliar=[]

    for string, numero in zip(listaS, listaI):
        if len(string)<= numero:
            lista_auxiliar.append(string)
    return lista_auxiliar

def filtro_string_tamanho_min(listaS, listaI):

    """Função que para uma lista de strings e outra de inteiros, faz uma filtragem para que apenas
    as strings de tamanho menor ou igual ao inteiro de mesmo indice da respectiva string.

    Argumentos: listaS (lista de strings)
    listaI (lista de inteiros)
    """
    return [string \
            for string, numero in zip(listaS, listaI)\
            if len(string)<= numero  ]


# Questão 6========================================================
def filtrar_matriz_soma_anterior_maior(listad):
    """filtra as sublistas cuka soma dos elementos é maior que a soma dos elementos da próxima sublista"""
    lista_auxiliar=[]
    for item, indice in zip(listad, range(len(listad))):
       
        if (indice+1)==len(listad):
            
            break
        if sum(item)>sum(listad[indice+1]):
            lista_auxiliar.append(item)
    return lista_auxiliar

def filtrar_matriz_soma_anterior_maior_min(lista):
    return [lista[item] for item in range (len(lista)-1) if sum(lista[item])>sum(lista[item+1])]

# Questão 7========================================================

def descobrir_menor_soma_3listas_mesmo_indice(lista1,lista2,lista3):
    """Dada três lista de números inteiros, faz uma redução para encontrar o
menor número resultante da soma dos elementos de índices correspondentes. Retorna
o valor encontrado.

    """
    menor= lista1[0]+lista2[0]+lista3[0]
    for i in range(len(lista1)):
        if lista1[i]+lista2[i]+lista3[i] < menor:
            menor= lista1[i]+lista2[i]+lista3[i]
    return menor    
  
def descobrir_menor_soma_3listas_mesmo_indice_min(lista1,lista2,lista3):
    """Dada três lista de números inteiros, faz uma redução para encontrar o
menor número resultante da soma dos elementos de índices correspondentes. Retorna
o valor encontrado.
    """
    return descobrir_menor_soma_3listas_mesmo_indice(lista1,lista2,lista3)


# Questão 8========================================================






def soma_listas_Menor_e_Maior_mesmo_indice(lista1,lista2,lista3):
    lista_auxiliar=[]
    for item in range(len(lista1)):
        lista_auxiliar.append(max([lista1[item], lista2[item], lista3[item]])+ 
                              min([lista1[item], lista2[item], lista3[item]]))
    return lista_auxiliar



def filtrar_elementos_reverso_igual(lista):
    lista_auxiliar=[]
    lista_reversa=lista[::-1]
    for item in range(len(lista)):
        if lista[item]==lista_reversa[item]:
            lista_auxiliar.append(lista[item])
    return lista_auxiliar


def maior_string_lista(lista):
    lista_auxiliar=[]
    maior=0
    palavra=''
    cont=-1
    for item in lista:
        
        if len(item)>maior:
            maior=len(item)
            palavra=item
            cont=lista.index(item)
    return f'Palavra: {palavra}, Tamanho: {maior}, Indice: {cont}'


#Questao 9==============================================================
def soma_se_maior(lista):
    """soma os elementos de uma lista se o item de indice seguinte for menor que o elemento de i
    ndice analisado"""
    soma=0
    for indice in range(len(lista)-1):
        if lista[indice]>lista[indice+1]:
            soma+=lista[indice]

    return soma

#questão 10=========================================================
def concatenar_strings(lista):
    string=lista[0]
    for item in lista[1:]:
        string+=' '+item
    return string

#questão11====================================================
def verificar_primo(num):
    if num == 1:
        return False
    for i in range (2,num):
        if num%i==0: 
            return False
    return True

def indice_do_maior_primo(lista):
    indice=-1
    maior=0
    for i in lista:
        if verificar_primo(i) and i>=maior:
            maior = i 
            indice = lista.index(i)
    return indice    

#questão12============================================

def calcular_desvio_padrao(lista):
    media=sum(lista)/len(lista)
    
    soma=0
    for item in lista:
        soma+=(item-media)**2
    desvio=(soma/len(lista))**0.5
    return desvio

#questão13====================================
def buscar_valor(lista,valor):
    buscas=0
    for i in lista:
        buscas+=1
        if i== valor:
            return True, buscas
    return False
    
#questão14===========================================================
def buscar_valor_ordenada(lista,valor):
    buscas=0
    lista_ordenada=sorted(lista)
    print(f"Lista ordenada {lista_ordenada}\nO valor está na lista?")
    for i in lista:
        buscas+=1
        if i== valor:
            return f"{True}, foram necessárias {buscas} buscas"
    return False
        
        
#Questão 15=====================================================

def busca_binaria_numero(lista, num):
    
    comparaçoes=0
    lista_auxiliar=sorted(lista[::])
    
    while True:
        #[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
        comparaçoes+=1
        IndiceMax=len(lista_auxiliar)-1
        IndiceMin=0
        IndiceMedio=int((IndiceMax+IndiceMin)/2)
        
        if len(lista_auxiliar)==0:
                return False, comparaçoes
        
        if lista_auxiliar[IndiceMedio]>num:
            lista_auxiliar=lista_auxiliar[:IndiceMedio]
            
        elif lista_auxiliar[IndiceMedio]<num:
            lista_auxiliar=lista_auxiliar[IndiceMedio+1:]
            
        elif lista_auxiliar[IndiceMedio]==num:
            return True, comparaçoes
        

#questao16=========================================================
def frequencia_em_lista(lista,num):
    freq_num=0
    for i in lista:
        if i == num:
            freq_num+=1
    return freq_num

#questão 17===================================
def gerar_dicionarios_freq(lista):
    lista_auxiliar=[]
    for i in range(1,21):
        dicio={}
        dicio[i]=0
        for item in lista:
            if item == i:
                dicio[i]+=1
        lista_auxiliar.append(dicio)
    return lista_auxiliar

from random import randint
lista=[]
for i in range (1000):
    lista.append(randint(1,20))

print(*gerar_dicionarios_freq(lista), sep="\n")
    
    
