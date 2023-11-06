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


#Questão 3=================================

# msg='nina2'
# if len(msg)>=10 and\
#     re.search(r"[\d]",msg) and \
#     re.search(r"[A-Z]",msg) and\
#     re.search(r"[a-z]",msg) and\
#     len(re.findall(r"[!@#$%&*+=]",msg))>=3:
#         print("MUito forte")
        
# elif len(msg)>=8 and\
#     re.search(r"[\d]",msg) and \
#     re.search(r"[A-Z]",msg) and\
#     re.search(r"[a-z]",msg) and\
#     re.search(r"[!@#$%&*+=]",msg):
#         print("Forte")
        
# elif len(msg)>=6 and\
#     re.search(r"[\d]",msg) and \
#     re.search(r"[A-Z]",msg) and\
#     re.search(r"[a-z]",msg):
#         print("Média")
        
# elif len(msg)>=6:
#         print("Fraca")
# else:
#     print("SENHA INVALIDA")
        
        
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




#Questão7============================
msg='David R$Galhego de Nazare'
regex= re.compile(r"\bR\$\w*")

print(regex.findall(msg))
