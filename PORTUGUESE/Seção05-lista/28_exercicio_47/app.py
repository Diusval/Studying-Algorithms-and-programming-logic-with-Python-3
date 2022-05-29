from math import prod


produto_1 = ["Celular", "Azul", 2000]
produto_2 = ["Computador", "Branco", 7600]
produto_3 = ["moto", "vermelha", 12000]

produtos = [produto_1, produto_2, produto_3]

print(produtos)

for produto in produtos:
  print("O produto encontrado foi o: %s na cor %s e no valor de R$:%.2f." % (produto[0], produto[1], produto[2]) )