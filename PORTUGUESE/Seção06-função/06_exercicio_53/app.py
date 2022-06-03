#Escreva uma função que receba uma lista de números;
#A função deve retornar apensas os números pares da lista;

def retorna_lista_par(lista):

  nova_lista = []

  for numero in lista:
    if numero % 2 == 0:
      nova_lista.append(numero)

  return nova_lista

lista_1 = [1,2,3,4,5,6,7,8,9,10]

lista_par = retorna_lista_par(lista_1)
print(lista_par)

lista_par_2 = [ 1,2,3,1,596,18,5,97,45,21,63,5,49,78,5,45,92,21,22,]

lista_par_2 = retorna_lista_par(lista_par_2)
print(lista_par_2)
