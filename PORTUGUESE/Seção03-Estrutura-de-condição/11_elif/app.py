nome = input("Digite o seu nome: ")

if nome == "Diusval":
  print("Ola, voce e um admin!")

  if 5 > 10:
    print("testando")
  elif 10 < 5:
    print("caiu aqui!")
    
elif nome == "Luiza":
  print("Ola, voce e a produtora de conteudo!")
else:
  print("voce e um usuario comum!")


  numero = int(input("Digite um numero: "))

  if numero > 0 and numero <= 5:
    print("Maior que 0.")
  elif numero > 5 and numero <= 10:
    print("Maior que 5.")
  elif numero > 10 and numero <= 20:
    print("Maior que 10.")
  elif numero > 20:
    print("Maior que 20.")
  else:
    print("Numero negativo.")
