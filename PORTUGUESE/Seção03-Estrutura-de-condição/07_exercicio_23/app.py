#Crie um programa com a variável salario;
#se for maior que 1800 imprima uma mensagem de que é necessário pagar imposto de renda;
#se não imprima uma mensagem que não precisa pagar IR

salario = float(input("Digite o seu salário: "))

if salario > 1800:
  print("Seu salário é R$%0.2f, é necessário pagar imposto de renda." % (salario))
else:
  print("Seu salário é igual ou menor que R$1800.00 não é necessário pagar imposto de renda.")