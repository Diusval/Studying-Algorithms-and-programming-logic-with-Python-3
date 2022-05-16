#Escreva um programa que receba um número;
#Verifique se o número é maior que 10, se não for imprima uma mensagem avisando que para prosseguir precisa ser maior que 10;
#No primeiro if verifique se o número é menor que 20, e imprima a multiplicação dele por 2;
#Se não imprima o número multiplicado por 5;

numero = int(input("Digite um número: "))

if numero > 10:

  if numero > 20:
    print("Número maior que 20")
    result1 = print(numero * 2)  
  else:
    print("Número menor que 20")
    result2 = print(numero * 5)

else:
  print("para poder prosseguir o número tem que ser maior que 10!")