a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segund número: '))
c = int(input('Digite o terceiro número: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor digitado foi: {}'.format(menor))

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado foi: {}'.format(maior))
