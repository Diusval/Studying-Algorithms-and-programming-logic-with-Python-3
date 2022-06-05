#Soma

def soma(a, b):
  return a + b

#Multiplicação

def multiplicacao(a, b):
  return a * b

#Função com parametro (Eu escolho se quero a soma ou a multiplicação)

def operacao(a, b, funcao):
  resultado = funcao(a, b)
  return resultado

#Exemplos "Soma" "Multiplicação" "Operação"

#Soma

print(soma(4,4))

#Multiplicação

print(multiplicacao(4,4))

#Eu escolendo:

print(operacao(5,5, soma))
print(operacao(5,5, multiplicacao))