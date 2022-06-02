#Escreva uma funcao que recebe um dado em texto;
#Se esse dado tem de 20 caracteres, retorne que e um texto longo;
#Se tem menos, retorne que e um texto curto;

def contador(texto):
  r = ""

  if len(texto) > 20:
    print("Tem mais que 20 caracteres esse texto e longo :)")
  
  elif len(texto) < 20:
    print("Tem menos de 20 caracteres esse texto e muito curto :(")

  return r

pri = contador("Ola tudo bem eu me chamo Diusval")
print(pri)

seg = contador("oi")
print(seg)
