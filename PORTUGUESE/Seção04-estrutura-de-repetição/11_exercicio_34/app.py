#Crie um loop que detecta se um número é primo ou não;
#Número primo é o número que é dividido apenas por ele mesmo e o número 1;

numero = int(input("Digite um número: "))

divisoes = 0

contador = numero

while contador > 0:
  if numero % contador == 0:
    divisoes = divisoes + 1

  contador = contador - 1

if divisoes == 2:
  print("O numero %d é primo" % numero)
else:
  print("O número %d não é primo" % numero)