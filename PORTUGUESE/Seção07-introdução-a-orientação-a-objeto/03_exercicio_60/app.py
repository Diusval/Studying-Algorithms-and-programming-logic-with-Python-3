#Crie uma classe Carro com as propriedades de portas, motor, se tem teto solar, marca e preço;
#Crie objetos preenchendo os valores das propriedades;

class Carro:
  def __init__(self, porta, motor, teto_solar, marca, preco):
    self.porta = porta
    self.motor = motor
    self.teto_solar = teto_solar
    self.marca = marca
    self.preco = preco

panamera = Carro(2, 2.0, True, "Porcher", 270.000)

print(panamera.preco)
print(panamera.marca)

tt = Carro(4, 1.0, False, "BMW", 180.00)

print(tt.marca)
print(tt.teto_solar)