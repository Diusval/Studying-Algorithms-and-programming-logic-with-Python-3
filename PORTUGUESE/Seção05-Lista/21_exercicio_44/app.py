#Crie um progrma que busca por um elemento;
#O método de loop precisa ser for;
#Imprima a mensagem com o elemento encontrado;

numeros = [1,2,3,4,5,6,7,8,9,10]

qual_numero_quer_encontra = int(input("Que número deseja buscar de 1 a 10: "))

encontrado = False

for n in numeros:
  if n == qual_numero_quer_encontra:
    print("O número escolido foi o: %d." % n)
    encontrado = True

if encontrado == False:
  print("o número: %d não está disponivel em nossa lista." % qual_numero_quer_encontra)