def ler_datatran2020():
    with open ('datatran2020.csv', 'r', encoding='utf-8') as f:
        data = [linha.split(',') for linha in f]
        colunas = data[0]
        bd = dict()
        for id, coluna in enumerate(colunas):
            bd[coluna] = [item[id] for item in data[1:]]

    return bd








def colunas():
     with open ('datatran2020.csv', 'r', encoding='utf-8') as f:
        data = [linha.split(',') for linha in f]
        print(*data[0], sep ="\n")





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









# questao_01()

#colunas()
#base = ler_datatran2020()
#for chave in base:
#    print(base[chave][:3])