#Escreva uma função que recebe uma lista de números;
#Calcule a média dos números da lista;

def calc_media(lista):
  media = 0
  soma = 0

  for n in lista:
    #soma = soma + n
    soma += n

  media = soma / len(lista)

  return media

notas = [9,8,7,3]

media_prova = calc_media(notas)
print(notas)
print(media_prova)

numeros = [2,15,748,54,12,25,12,16,145]

media_numeros = calc_media(numeros)
print(numeros)
print(media_numeros)
