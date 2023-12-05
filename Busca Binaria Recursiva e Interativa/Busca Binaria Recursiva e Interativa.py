import timeit


def busca_binaria_recursiva(lista, numero):
    lista_ordenada=sorted(lista[::])
    
    indice_max=len(lista_ordenada)-1
    indice_min=0
    indice_medio= (indice_max+indice_min)//2        
    if len(lista_ordenada)<=0:
        
        return f"O número {numero} não está na lista"
            
    if lista_ordenada[indice_medio] == numero:
        
        return f"O número {numero} está na lista"
            
    if lista_ordenada[indice_medio]>numero:
        
        return busca_binaria_recursiva(lista_ordenada[indice_min:indice_medio], numero)
        
    if lista_ordenada[indice_medio]<numero:
        
        return busca_binaria_recursiva(lista_ordenada[indice_medio+1:indice_max+1], numero)
        



lista=[1 for i in range(10000*1)]


def resultado_busca():
    return busca_binaria_recursiva(lista, 0)

tempo = timeit.timeit(resultado_busca, number=5)/5

print(f'O tempo medio de execução foi de {tempo:.3f} segundos')
        
        
        
        
        
        
        
        

# import timeit

# def busca_binaria_interativa(lista, num):
    
#     comparaçoes=0
#     lista_auxiliar=sorted(lista[::])
    
#     while True:
        
#         comparaçoes+=1
#         IndiceMax=len(lista_auxiliar)-1
#         IndiceMin=0
#         IndiceMedio=int((IndiceMax+IndiceMin)/2)
        
#         if len(lista_auxiliar)==0:
#                 return False, comparaçoes
        
#         if lista_auxiliar[IndiceMedio]>num:
#             lista_auxiliar=lista_auxiliar[:IndiceMedio]
            
#         elif lista_auxiliar[IndiceMedio]<num:
#             lista_auxiliar=lista_auxiliar[IndiceMedio+1:]
            
#         elif lista_auxiliar[IndiceMedio]==num:
#             return True, comparaçoes
 
 
 
          
# lista=[1 for i in range(10000000*1)]


# def resultado_busca():
#     return busca_binaria_interativa(lista, 0) 

# tempo = timeit.timeit(resultado_busca, number=7)/7
# print(f'O tempo de execução foi de {tempo:.3f}')
    
    
    