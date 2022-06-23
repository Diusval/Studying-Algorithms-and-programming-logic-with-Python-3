#Crie uma lista com número de 1 a 10;
#Percorra a lista com um loop;
#Quando encontrar o elemento 4 remova-o;
#Exiba a nova lista por print;

lista = []

i = 0

while i <= 10:
  lista.append(i)
  i = i + 1

print(lista)

j = 0

while j < len(lista):
  if lista[j] == 4:
    del lista[j]
  j = j + 1

print(lista)
