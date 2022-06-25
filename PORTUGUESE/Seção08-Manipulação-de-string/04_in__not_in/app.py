frase = "Essa é a frase que queremos achar uma palavra."

print(frase)

if "frase" in frase:
  print("Encontramos a frase.")

print("frase" in frase)

if "segunda-feira" not in frase:
  print("segunda-feira não foi encontrada na frase.")

print("segunda-feira" not in frase)