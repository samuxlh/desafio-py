lista = list(range(5000000))
count = 0
for x in lista:
  if (lista[x] % 2 == 0 & lista[x] % 49 == 0 & lista[x] % 37):
      count += 1
print(count)