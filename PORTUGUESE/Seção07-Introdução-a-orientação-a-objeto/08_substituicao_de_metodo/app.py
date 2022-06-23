class Pessoa:
  def falar(self):
    print("Olá, tudo bem!")

class Mateus(Pessoa):
  def falar(self):
    print("Olá pessoal, eu sou o Mateus")

class Roberto(Pessoa):
  pass

mateus = Mateus()

mateus.falar()

roberto = Roberto()

roberto.falar()