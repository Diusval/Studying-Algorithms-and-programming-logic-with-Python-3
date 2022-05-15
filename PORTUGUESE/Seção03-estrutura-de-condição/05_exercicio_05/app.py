#Escreva um programa que lê dois números;
#depois imprima o maior deles;

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro o número: "))

if n1 > n2:
  print("O primeiro número: %.0f é maior do que %.0f." % (n1, n2))

if n2 > n1:
  print("O segundo número: %.0f é maior do que %.0f." % (n2, n1))

if n1 == n2:
  print("%.0f é igual a %.0f." % (n1, n2))
