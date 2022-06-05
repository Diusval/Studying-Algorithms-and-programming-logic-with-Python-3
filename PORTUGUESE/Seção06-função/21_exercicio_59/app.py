#Crie um programa que gera um número de 1 a 10;
#peça para o usuário adivinhar o número;
#e identifique se ele acertou ou não;

import random

numero = int(input("Digite um número de 1 a 10: "))

sorteio = random.randint(1,10)

if numero == sorteio:
  print("Parabéns você ganhou!!!")
else:
  print("Não foi dessa vez.")
  print("O número que você escoleu foi o %d e o sorteado foi %d." % (numero, sorteio))
