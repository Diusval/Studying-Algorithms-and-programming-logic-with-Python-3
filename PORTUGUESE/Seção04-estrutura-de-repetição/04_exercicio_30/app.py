#Crie um loop while em que o fim e determinado pelo numero que o usuario insere no sistema;
#Imprima os numeros com print;

numero_fim = int(input("Digite um numero para o loop poder acabar: "))

numero = 0
while numero <= numero_fim:
  print(numero)
  numero = numero + 1