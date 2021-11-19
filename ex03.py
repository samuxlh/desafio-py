arr = []
i = 0
while i<5:
    n = int(input('Insira a nota do aluno ' + str(i) + ': '))
    arr.append(n);
    i = i + 1

i=0
max1 = 0

while i<5:
    if (arr[i] > max1):
        max1 = arr[i]
        pos = i
    i = i + 1

print('\nA maior nota foi:', max1);
print('Essa nota foi obtida pelo aluno:', pos);