l = ["Sofá", "Televisão", "Rádio", "Ar condicionado", "Poltrona"]

i = 0

item_procurado = input("Digite o item que deseja procurar: ")
achou = False

while i < len(l):
  if l[i] == item_procurado:
    print("O item %s, foi encontrado." % item_procurado)
    achou = True
  i = i + 1
  
if achou == False:
  print("O item %s, não foi encontrado em nossa lista." % item_procurado)