#Escreva um programa que receba dois números;
#Insira a multiplicação entre eles em uma variável;
#Se for menor ou igual a 100 o resultado insira uma mensagem de que o número é baixo;
#Se não o número é alto;

print("Digite dois números para calcularmos.")

n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo número: "))

mult = n1 * n2

if mult <= 100:
  print("O número é baixo")
  print("%.2f" % mult)
else:
  print("O número é alto")
  print("%.2f" % mult)