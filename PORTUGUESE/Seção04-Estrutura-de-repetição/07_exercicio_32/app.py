#Escreva um loop while que vai de 20 a 0;
#Quando encontrar o número 5 cancele o loop;
#Imprima os números na tela;

n = 20

while n >= 0:
  print(n)
  if n == 5:
    break
  n = n - 1

print("Pós loop")