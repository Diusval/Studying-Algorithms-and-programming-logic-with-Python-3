class Pessoa:
  def __init__(self, nome, idade, profissao):
    self.nome = nome
    self.idade = idade
    self.profissao = profissao

  def __str__(self):
    return "O nume do usuário é %s ele tem %d anos e é um %s." % (self.nome,  self.idade, self.profissao)

diusval = Pessoa("Diusval", 20, "Programador")

print(diusval.__str__())