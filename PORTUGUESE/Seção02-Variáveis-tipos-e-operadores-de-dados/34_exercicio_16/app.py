#Faça um programa receber um valor como salário;
#E outro como porcentagem de almento;
#Exiba o valor total após o aumento do interpretador;

salario = float(input("Digite o valor do empregado: "))
aumento = int(input("Digite a porcentagem em aumento: "))

novo_salario = salario + (salario * (aumento/100))

print("O salário atualizado é de %.2f" % (novo_salario))