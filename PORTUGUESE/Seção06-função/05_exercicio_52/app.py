#Escreva uma função que recebe um dado em texto;
#Se esse dado tem mais de 20 caracteres, retorne que é um texto longo;
#Se tem menos, retorne que é um texto curto;

def contador(texto):
  r = ""

  if len(texto) > 20:
    print("Tem mais que 20 caracteres esse texto é longo :)")
  
  elif len(texto) < 20:
    print("Tem menos de 20 caracteres esse texto é muito curto :(")

  return r

pri = contador("Olá tudo bem eu me chamo Diusval")
print(pri)

seg = contador("oi")
print(seg)
