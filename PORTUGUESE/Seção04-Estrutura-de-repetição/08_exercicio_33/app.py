#Crie um loop que ixibe os números digitados do usuário na tela;
#O loop deve ser cancelado quando o usuário digitar 0;

x = 0

while x < 1:
  numero = int(input("Digite um número: "))

  print(numero)

  if numero == 0:
    print("Saindo do loop!")
    break 