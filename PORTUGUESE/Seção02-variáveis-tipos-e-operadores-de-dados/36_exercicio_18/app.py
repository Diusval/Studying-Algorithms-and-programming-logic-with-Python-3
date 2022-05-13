#Crie um proggrama que recebe o saldo de uma cont bancária com R$359,56;
#Depois insira uma nova quantia por meio de input;
#E renova um valor de R$125,98, referente a fatura de cartão de crédito;
#Imprima o valor final da conta após as operações com strin dinâmica;

nome = (input("Digite o seu nome por gentileza: "))

print("Olá %s, seu saldo é de R$359.56" % nome)

deposito = float(input("Por favor digite o valor que deseja depositar em sua conta: "))

valor_final = (359.56 + deposito) - 125.98

print("O valor de 125,98 foi abatido na fatura do seu cartão de crédito, após o deposito realizado.")
print("Valor atualizado na conta %.2f." %valor_final)
