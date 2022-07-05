import pdb
pdb.set_trace()


L = [[2,4,1],[1,2,3,4,5,6,7,8],[100,250,43]]

Max = [max(x) for x in L ]

print(Max)

def es_primo(x):
    listaprimos=[]
    lista = [x]
    for i in lista:
        primos = True
        for j in range(2,i):
            if i == j:
                break
            elif i%j==0:
                primos = False
            else:
                continue
        if primos == True:
            listaprimos.append(i)

    return listaprimos




numeros = [3,4,8,5,5,22,13]

valor = list(filter(es_primo, numeros))

print(valor)