#crie um programa que recebe o número de rodas que o veículo possui;
#se for mais que 2, imprima uma mensagem para pagar pédágio;
#se for igual a 2, imprima uma mensagem dizendo que pode passar livremente;

rodas = int(input("Digite a quantidade de rodas em seu veículo: "))

if rodas > 2:
  print("Pague o valor de R$102.00 ao pedágio para prosseguir na estrada.")

if rodas == 2:
  print("Pode passar livremente.")