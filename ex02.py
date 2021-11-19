import numpy

lista = list(range(10))
i = 0
aux = 0
for i in lista:
    fatorial = 0
    aux = 0
    if (lista[i] % 2 == 0):
        while (aux <= i):
            fatorial *= aux
            aux += 1
        lista[i] = ((3^i) + 7*(fatorial));
    else:
        lista[i] = ((2^i) + 4*(numpy.log(i)))

listaAux = lista.copy()
listaAux.sort()

i=0
while i<10:
    if lista[i] == listaAux[9]:
        pos = i;
    i = i + 1

print('Posição do maior item do vetor é:', pos)
print('A média dos valores da lista foi:', round(numpy.mean(lista), 2))