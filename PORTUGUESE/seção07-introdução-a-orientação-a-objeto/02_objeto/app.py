class Pessoa:
  def __init__(self, nome, idade, profissao):
    self.nome = nome
    self.idade = idade
    self.profissao = profissao

diusval = Pessoa("Diusval", 20, "Programador")

print(diusval)

print(type(diusval))

print(diusval.nome)
print(diusval.idade)
print(diusval.profissao)

if diusval.nome == "Diusval":
  print("O nome é Diusval!")

nome = diusval.nome

print(nome)
