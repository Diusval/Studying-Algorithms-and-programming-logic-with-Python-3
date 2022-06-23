#Crie uma classe Pessoa com nome e idade;
#Crie uma classe de Super Herói que herda as caractecísticas básicas de pessoa;
#Crie poderes especiasi para o super héroi;
#Teste as duas classes criando novos objetos;


#Class Pessoa
class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
  
  def falar(self):
    print("Olá galera!")

class Superheroi(Pessoa):
  def __init__(self, nome, idade, super_poder):
    super().__init__(nome, idade)
    self.super_poder = super_poder

  def utilizar_super_poder(self):
    print("O herói %s utilizou o %s" % (self.nome, self.super_poder))

#Pessoa João
joao = Pessoa("João", 21)

joao.falar()

#Super Herói (Pessoa) Diusval
diusval = Superheroi("Diusval", 20, "One For All")

diusval.falar()

diusval.utilizar_super_poder()