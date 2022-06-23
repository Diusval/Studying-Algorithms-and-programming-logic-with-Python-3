#crie uma função que retorna se um numero é maior ou menor que 10;
#O número deve ser passado como parametro;

def comparacao(comp):

  r = ""

  if comp > 10:
    print("O número %d, é maior que 10!" % comp)
  elif comp == 10:
    print("O número é 10!")
  else:
    print("O número %d, é menor que 10!" %comp)

  return r

result_1 = comparacao(11)
print(result_1)

result_2 = comparacao(2)
print(result_2)

result_3 = comparacao(10)
print(result_3)
