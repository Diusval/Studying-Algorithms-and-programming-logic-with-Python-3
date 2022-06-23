#Crie um programa que verifique o menor valor de uma lista;

lista = [88, 45, 578, 2, 9]

menor_valor = lista[0]

for n in lista:
  if n < menor_valor:
    menor_valor = n

print(menor_valor)