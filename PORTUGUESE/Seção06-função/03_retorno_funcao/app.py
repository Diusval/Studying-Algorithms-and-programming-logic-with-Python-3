def saudacao(nome):
  return "Ola %s" % nome

sds = saudacao("Diusval")

print(sds + ". Tudo bem?")

def soma(a, b):
  return a + b

s = soma(5, 7)
d = soma(5, 3)

print(s)

print(s + 5)

print(s + d)

def profissao(nome):

  p = ""

  if nome == "Diusval":
    p = "Programdor"
  else:
    p = "nao identificado"
  
  return p

prof = profissao("Diusval")

print(prof)

prof_m = profissao("Matheus")

print(prof_m)

