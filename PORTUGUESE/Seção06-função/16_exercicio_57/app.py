#Crie uma função que recebe uma sequência de parâmetros numéricos
#Multiplique todos eles e exiba o valor no terrminal;

def mult_todos(*numeros):
  resultados = 1
  for num in numeros:
    resultados = resultados * num
  return resultados

print(mult_todos(2,2))

a = mult_todos(2,4,8)
print(a)