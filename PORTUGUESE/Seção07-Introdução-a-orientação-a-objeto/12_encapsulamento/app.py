class Aviao:

  #Encapsulamento usamos _ ou __ para encapsula um objeto.
  __pri_rota = "Dubai"

  __seg_roto = "Nova York"

  def __init__(self, marca):
    self.marca = marca

  def mostrar_rotas_pri_rota(self):
    print("A primeira rota do avião é para %s." % self.__pri_rota)

  def mostrar_rotas_seg_rota(self):
    print("A segunda rota do avião é para %s." % self.__seg_roto)

aviao = Aviao("Bonde do Forro")

print(aviao.marca)

#não ira mostra a primeira rota, pos ele é um dado inalterado encapsulado.
#print(aviao.__pri_rota)

#print(aviao.__seg_rota)

#acessou o dado porque declarei ele num método.
aviao.mostrar_rotas_pri_rota()

aviao.mostrar_rotas_seg_rota()