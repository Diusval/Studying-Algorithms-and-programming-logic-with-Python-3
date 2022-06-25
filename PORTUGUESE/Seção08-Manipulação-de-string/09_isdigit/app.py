frase = "asd"

print(frase.isdigit())

#O isdigit não consegue entender numero Float tem que fazer uma alteração para ele entender, só entende numero Inteiro.
numero = "12345"

print(numero.isdigit())

#conversão para o isdigit entender os números float.
numero2 = "123.5"

print(numero2.replace(".", "").isdigit())