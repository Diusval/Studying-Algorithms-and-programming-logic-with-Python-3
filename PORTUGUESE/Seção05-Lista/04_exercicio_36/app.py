#Crie uma lista com 5 notas de prova de um aluno;
#Faça um loop que calcule a média das notas;
#Imprima o resultado final;

notas = [10, 7, 6, 8]

print(notas)

i = 0
soma = 0

while i < 4:
  soma = soma + notas[i]
  i = i + 1

media = soma / 5

print("O aluno teve a média %.1f na matéria X." % media)