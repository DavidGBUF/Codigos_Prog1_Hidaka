import funções as f
from random import randint 

# lista1=[1.2, 5, 7, 1, 9.9, 2.3]
# lista2=[0.8,1, 2, 0.5, 0.1, 0.7]
# lista3=[1,3,5,0.7,5,2]

# listaK=[1,4,6,8,9,10,12,14,15,16]
# lista=['barata', 'tamanduar', 'paralelepipedo', 'aranha','sexo']

# listateste=[1,2,3,7,3,8,2,7,9,3,3,2,1]
# print(f.soma_listas_Menor_e_Maior_mesmo_indice(lista1, lista2, lista3))
# lista_primos=[]
# cont=1
# while True:
#     if f.verificar_primo(cont):
#         lista_primos.append(cont)
#     cont+=1
#     if len(lista_primos)==25:
#         break
 
# print(f.busca_binaria_numero(lista_primos, 55))

lista=[]
for i in range (1000):
    lista.append(randint(1,20))
    print(randint(1,20))
    
print(f.gerar_dicionarios_freq(lista))
cont=0
   
    
    