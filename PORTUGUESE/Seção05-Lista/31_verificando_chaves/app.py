dicionario = {
  "nome": "Diusval",
  "idade": 20,
  "estudando": "Python"
}

print(dicionario)

print("nome" in dicionario)
print("sobrenome" in dicionario)

if "nome" in dicionario:
  print("O seu nome é %s" % dicionario["nome"])

if "sobrenome" in dicionario:
  print("O seu sobrenome é: %s" % dicionario["sobrenome"])