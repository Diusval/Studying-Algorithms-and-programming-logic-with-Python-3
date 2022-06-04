#Escreva uma função que desenha uma escada no terminal;
#Os números de degtaus deve ser informado por parâmetro;
#EX:
#-#
#-##
#-###
#-####

def criar_degrau(degrau):
  i = 1
  while i <= degrau:
    print("#" * i)
    i += 1

criar_degrau(10)