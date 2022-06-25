frase = "Eu quero encontrar o tubarão."

print(frase.find("peixe"))

if frase.find("peixe") >= 0:
  print("Encontrei o peixe.")

print(frase.find("tubarão"))

if frase.find("tubarão") == -1:
  print("O tubarão não foi encontrado.")
else:
  print("Há um tubarão")