#########convertendo string para inteiro###########

numero_texto = input("Digite um valor: ")

print(numero_texto)

numero = int(numero_texto)

novo_numero = 10 + numero

print(novo_numero)

novo_numero = int(input("Digite mais um número: "))

print (numero + novo_numero)

#########convertendo string para float###########

novo_float = float(input("Digite o que você tem de dinheiro na carteira: "))

print("O valor na carteira é de %.2f" % novo_float)