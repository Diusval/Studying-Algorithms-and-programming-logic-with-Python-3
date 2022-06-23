#STARTSWITH: Dá valor TRUE para a primeira palavra da string.
frase = "Testamos o começo da string"

print(frase.startswith("Testamos"))

print(frase.startswith("string"))

if(frase.startswith("Testamos") == True):
  print("Encontramos a palavra!!!")

#ENDSWITH: Dá valor TRUE para a última palavra da string.
print(frase.endswith("string"))

print(frase.endswith("Testamos"))