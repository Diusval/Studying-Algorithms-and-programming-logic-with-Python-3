#Crie um dicionário com livros que você goste e o número de páginas;
# Imprima estes valores no terminal;

livros= {
  "Pai rico, pai pobre": 278,
  "O segredo da mente milionária": 170,
  "O manual de persuasão do fbi": 580
}

for livro in livros:
  print("O livro %s tem: %d páginas." % (livro, livros[livro]))