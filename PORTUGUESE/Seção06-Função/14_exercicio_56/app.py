#Crie uma função que recebe outra como parâmetro;
#A que vai receber parâmetros deve receber um nome, uma idade e uma profissão;
#A função de argumento deve apresentar estes dados em uma string dinâmica;

#Reune os dados.
def reune_dados(nome, idade, profissao, funcao):
  apresentacao = funcao(nome, idade, profissao)
  return apresentacao

#Ira apresentar os dados.
def apresenta_dados(nome, idade, profissao):
  frase = "O nome do usuário(a) é %s e ele(a) tem %d anos de idade e sua profissão é %s." % (nome, idade, profissao)
  return frase

#Forma resumida de printar os dados.
print(reune_dados("Diusval", 20, "Programdor", apresenta_dados))

#Forma com variavel de printar os dados.
apresentacao = reune_dados("Luiza", 22, "Artista", apresenta_dados)
print(apresentacao)