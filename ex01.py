myList = list(range(5000000))
count = 0
for x in myList:
  if (myList[x] % 2 == 0):
    if(myList[x] % 49 == 0):
          if(myList[x] % 37 == 0):
                count = count + 1
print('Existem', count, 'números que satisfazem a condição.')
