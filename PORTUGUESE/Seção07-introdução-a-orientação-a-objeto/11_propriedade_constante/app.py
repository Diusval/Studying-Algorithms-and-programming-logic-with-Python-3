class Carro:

  #Constante
  rodas = 4

  def __init__(self, marca):
    self.marca = marca
  
ferrari = Carro("FERRARI")

print(ferrari.marca)

print(ferrari.rodas)