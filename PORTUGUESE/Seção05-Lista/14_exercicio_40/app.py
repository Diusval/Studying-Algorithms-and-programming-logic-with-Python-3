#Crie uma lista com 5 elementos de forma dinâmica;
#Ou seja, cada elemento deve ser inserido pelo usuário;

lista = []

i = 0

n = 1

while i < 5:
  numero = int(input("Digite o %d° número: " % n))
  lista.append(numero)
  n = n + 1
  i = i + 1

print("Os números foram adicionados a lista: %s." % lista)

#####################################################################

lista2 = []

i = 0

while i < 5:
  elemento = input("Digite um elemento: ")
  lista2.append(elemento)
  i = i + 1

print("Os elementos adicionados a lista foram: %s." % lista2)

