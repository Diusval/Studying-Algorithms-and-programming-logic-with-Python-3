#Escreva um programa que lê uma idade e insira ela em uma variavel;
#Verifique por IF se a idade é maior ou igual a 18;
#Se sim, imprima uma mensagem "pode entrar na balada"

idade = int(input("Quantos anos você tem? "))

if idade >= 18:
  print("Pode entrar na balada.")

if idade < 18:
  print("Talvez ano que vem.")