notas = []
item = ''
i = 0
while i<5:
    n = int(input('Insira a nota do aluno ' + str(i) + ': '))
    notas.append(n);
    i = i + 1

i=0
max1 = 0

while i<5:
    if (notas[i] > max1):
        max1 = notas[i]
        pos = i
    i = i + 1

print('\nA maior nota foi:', max1);
print('Essa nota foi obtida pelo aluno:', pos);