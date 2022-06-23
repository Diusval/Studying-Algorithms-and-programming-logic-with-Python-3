#Crie um programa que receba a categoria, em valor numerico, de um produto;
#Se for 1: exiba que e uma bolsa;
#Se for 2: exiba que e um tenis;
#se for 3: exiba que e uma mochila;
#Caso nao seja nenhum do valores, exiba que a categoria nao foi encontrada;

print("Parabéns! Você acaba de ganhar um brinde! Escolha um de nossos brindes.")
print("Digite 1 para Bolsa")
print("Digite 2 para Tênis")
print("Digite 3 para Mochila")

produto = int(input("Digite o numero do BRINDE desejado: "))

if produto == 1:
  print("Brinde, bolsa confirmado!")
elif produto == 2:
  print("Brinde, tênis confirmado!")
elif produto == 3:
  print("Brinde, mochila confirmado!")
else:
  print("Esse brinde não foi encontrado no seu carrinho :(")