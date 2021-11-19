lista = list(range(5000000))
count = 0
for x in lista:
  if (lista[x] % 2 == 0):
    if(lista[x] % 49 == 0):
          if(lista[x] % 37 == 0):
                count = count + 1
print('Existem', count, 'números que satisfazem a condição.')
