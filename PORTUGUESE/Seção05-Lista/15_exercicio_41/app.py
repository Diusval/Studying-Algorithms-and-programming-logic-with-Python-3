#Crie duas váriáveis de listas;
#Crie uma terceira lista com todos os elementos das duas listas anteriores;

lista_1 = [1,2,3,4,5]
lista_2 = [5,4,3,2,1]

print(lista_1)
print(lista_2)

lista_3 = []

lista_3.append(lista_1 + lista_2)

print("A junção das duas listas: %s" % lista_3)

#2###########################################################

lista_a = [1,2,3,4,5]
lista_b = [6,7,8,9,10]
lista_c = []

i = 0

while i < len(lista_a):
  lista_c.append(lista_a[i])
  i = i + 1

j = 0

while j < len(lista_b):
  lista_c.append(lista_b[j])
  j = j + 1

print(lista_c)
