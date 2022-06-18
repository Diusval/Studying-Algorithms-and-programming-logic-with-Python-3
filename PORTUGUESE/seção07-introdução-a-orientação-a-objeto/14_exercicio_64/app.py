#Crie uma classe Mamífero com propriedades de mamíferos;
#Herde os detalhes desta classe e crie novas para Cachorro, Gato e outros que quiser;
#Crie objetos destas classes que herdam de Mamífero;
#Exiba as propriedades e métodos na tela;

class Maniferos:
  def __init__(self, patas, orelhas):
    self.patas = patas
    self.orelhas = orelhas
  
  def andar(self):
    print("O manífero andou!")

class Cachorro(Maniferos):
  def __init__(self, patas, orelhas, cor_do_pelo):
    super().__init__(patas, orelhas)
    self.cor_do_pelo = cor_do_pelo

  def latir(self):
    print("Au Au!")

class Gato(Maniferos):
  def __init__(self, patas, orelhas, listras):
    super().__init__(patas, orelhas)
    self.listras = listras

  def miar(self):
    print("Miauuuuu")


#Cachorro
tufao = Cachorro(4, 2, "preto")

tufao.andar()

tufao.latir()

print(tufao.patas)

#Gato
bruce = Gato(4, 2, False)

bruce.andar()

bruce.miar()

print(bruce.listras)