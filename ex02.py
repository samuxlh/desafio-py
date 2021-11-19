import numpy

myList = list(range(10))
i = 0
aux = 0
for i in myList:
    f = 0
    aux = 0
    if (myList[i] % 2 == 0):
        while (aux <= i):
            f *= aux
            aux += 1
        myList[i] = ((3^i) + 7*(f));
    else:
        myList[i] = ((2^i) + 4*(numpy.log(i)))

myListAux = myList.copy()
myListAux.sort()

i=0
while i<10:
    if myList[i] == myListAux[9]:
        pos = i;
    i = i + 1

print('Posição do maior item do vetor é:', pos)
print('A média dos valores da lista foi:', round(numpy.mean(myList), 2))