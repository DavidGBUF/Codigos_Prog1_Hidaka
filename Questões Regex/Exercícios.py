import re

#Questão 1==================================================================
# msg = 'AAAAAAAAA'
# regex= re.compile(r"A+")

# if len(msg)%2==0 and\
#     regex.fullmatch(msg):
#         print(f"A mensagem {msg} tem tamanho par e é formada apenas por 'A'")
#         print(regex.fullmatch(msg))
        
# elif len(msg)%2!=0:
#     print("O tamanho da mensagem não é par")
    
# else:
#     print("A msg não é formada apenas por 'A' ")


# #Questão2==============================================
# msg= "@...men%sag*em d3 t e#st)e"
# regex= re.compile(r"[^A-Za-z\s]+")
# saida = regex.sub("", msg)
# print(saida)


#
 
 
 
# #Questão4========================================
# msg="mensagem de texte (91) 98118-1134 e esse teste 98118-1143" 
# regex = re.compile(r"(\(\d{2}\)\s?)?\d{5}-?\d{4}")
#         #            

# numeros=[]

    
     
# for i in regex.finditer(msg):
#     numeros.append(i.group())
    
# print(numeros)
        
#Questão5==================================================
# msg='1000011'
# regex= re.compile(r"[1 0]+")
# if regex.fullmatch(msg) and len(re.findall(r"1", msg))>=3:
#     print("sucesso")



# #Questão6==========================================
# msg='10101010101010'
# regex= re.compile(r"[1 0]+")

# if regex.fullmatch(msg) and not re.search(r"11", msg):
#     print("sucesso")




# #Questão7============================
# msg='A manutenção custa R$60, a retirada do aparelho R$485, eu só tenho R$300'
# regex= re.compile(r"R\$\w*")

# for item in regex.finditer(msg):
#     print(item)
#     print(item.span())



# #Questão8============================================
# def verificar_expressão(expressao):
    

#     regex= re.compile(r'^\s*\d+(\s*[\+\-\*\/]\s*\d+)*$')
#     resultado= regex.match(expressao) 
#     return resultado is not None


# print(verificar_expressão('15+165+156+154-4585*142*18/8458/5'))
# #Questão9==============================
# msg="""A chuva não mata, mas molha. O amor não se vê, sente. A amizade não se compra, constrói.
# E pessoas como você não se esquecem, guarda-se no fundo do coração."""
# regex = re.compile(r"[A-Z]\w*")
# for item in regex.finditer(msg):
#     print(item)
#     print(item.span())



# #Questão10==================================
# msg="ACTGATG"

# saida = re.fullmatch(r"[ATCG]+", msg) and\
#     len(re.findall(r"AC", msg))>=2 and\
#         len(re.findall(r"TG",msg ))>=2
        
# if saida:
#     print('A string passou no teste')
# else:
#     print('A string não atende a uma ou mais das caracteristicas ')
    




#Questão 3===================================================================
def verificar_muito_forte(msg):
    if len(msg)>=10 and\
    re.search(r"[\d]",msg) and \
    re.search(r"[A-Z]",msg) and\
    re.search(r"[a-z]",msg) and\
    re.search(r".*[^A-Z a-z \d].*[^A-Z a-z \d].*[^A-Z a-z \d].*",msg):
        return True



#============================================================================

def verificar_forte(msg):
    if len(msg)>=8 and\
     re.search(r"[\d]",msg) and \
     re.search(r"[A-Z]",msg) and\
     re.search(r"[a-z]",msg) and\
     re.search(r"[!@#$%&*+=]",msg):
        return True




#============================================================================


def verificar_moderada(msg):
    if len(msg)>=6 and\
     re.search(r"[\d]",msg) and \
     re.search(r"[A-Z]",msg) and\
     re.search(r"[a-z]",msg):
        return True



#============================================================================

def verificar_fraca(msg):
    if len(msg)>=6:
        return True


msg='liseuwdeug!@!!@!@gheu13427463'    


#============================================================================



print(f"A senha é {msg} e:")
if verificar_muito_forte(msg):
    print("A senha é muito forte")

elif verificar_forte(msg):
    print("A senha é forte")


elif verificar_moderada(msg):
    print("A senha é moderada")


elif verificar_fraca(msg):
    print("A senha é fraca")

else:
    print("A senha é inválida")



#Questão extra=========================================

msg='(91) 98118-1134'
regex = re.compile(r'\(\d{2}\)\s9\d{4}-\d{4}')

print(f"O número é {msg} ")

if regex.fullmatch(msg):
    print("Mascara?: Ok!")
    print(re.sub(r"[^\d]", '', msg))
