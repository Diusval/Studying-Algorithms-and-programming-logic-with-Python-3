#crie uma funcao que retorna se um numero e maior ou menor que 10;
#O numero deve ser passado como parametro;

def comparacao(comp):

  r = ""

  if comp > 10:
    print("O numero %d, e maior que 10!" % comp)
  elif comp == 10:
    print("O numero e 10!")
  else:
    print("O numero %d, e menor que 10!" %comp)

  return r

result_1 = comparacao(11)
print(result_1)

result_2 = comparacao(2)
print(result_2)

result_3 = comparacao(10)
print(result_3)