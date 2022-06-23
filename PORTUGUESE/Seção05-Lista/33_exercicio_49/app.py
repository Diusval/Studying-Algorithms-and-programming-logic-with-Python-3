#Crie um dicionário chamado carro com os seguintes valores;
#pneus: 4,
#portas: 4,
#motor: 1,
#janelas: 4,
#Adicione a chave teto solar com valor: 1;
#Delete motor e janela, imprima o dicionário novamente;

carro = {
  "pneus": 4,
  "portas": 4, 
  "motor": 1,
  "janelas": 4
}

print(carro)

carro["teto solar"] = 1

print(carro)

del carro["motor"]
del carro["janelas"]

print(carro)