idade = int(input("Qual é a sua idade? "))

if idade >= 18:
  print("Você pode entrar na balada.")
  pagamento = input("Como você vai pagar a entrada? ")

  if pagamento == "dinheiro":
    print("A fila do dinheiro é a número 1.")
  else:
    print("A fila do cartão é a número 2.")

else:
  print("Você não pode entrar na balada.")