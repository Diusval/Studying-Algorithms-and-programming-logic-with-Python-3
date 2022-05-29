from re import X


lista = [13, 55, 87, 12, 1, 7, 43]

maior_valor = 0

for n in lista:
  if n > maior_valor:
    maior_valor = n

print(maior_valor)