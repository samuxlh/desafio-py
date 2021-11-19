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

print(lista);
