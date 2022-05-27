#Buscando elemento dentro de uma lista;

lista = []

i = 0

while i <= 10:
  lista.append(i)
  i = i + 1
print(lista)

j = 0

while j < len(lista):
  if lista[j] == 4:
    print("Encontrado!")
  j = j + 1
