#Crie uma lista com alguns itens;
#Peça dois itens ao usuário;
#Identifique qual foi encontrado primeiro na lista;

lista_carro = ["Porta", "Pneu", "Estepe", "Maçaneta", "Janela", "Chave", "Motor", "Marcha"]

item_1 = input("O que deseja procurar primeiro: ")
item_2 = input("O que deseja procurar depois: ")

i = 0

while i < len(lista_carro):
  if lista_carro[i] == item_1:
    print("O primeiro objeto %s foi encontrado antes." % item_1)
    break
  elif lista_carro[i] == item_2:
    print("O segunto objeto %s foi encontrado antes." % item_2)
    break
  i = i + 1
