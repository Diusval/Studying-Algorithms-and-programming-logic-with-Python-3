#Importa módulos.
from palavras import palavras
import random

#Seleciona a palavra.
def selecionar_palavra():
  palavra = random.choice(palavras)
  return palavra.upper()

#Iniciar o jogo
def jogar(palavra):
  #Definir algumas variáveis.
  palavra_a_completar = "_" * len(palavra)
  advinhou = False
  letras_utilizadas = []
  palavras_utilizadas = []
  tentativas = 6

  #Boas Vindas ao jogador
  print("Seja Bem-Vindo ao JOGO DA FORCA!")
  print(exibir_forca(tentativas))
  print("Esta é a palavra: %s" % palavra_a_completar)

  #Enquanto o usuário não advinhar e ainda hover tentativas.
  while not advinhou and tentativas > 0:

    tentativa = input("Digite uma palavra ou letra para continuar: ").upper()

    print(tentativa)

    #TENTATICA DE LETRA ÚNICA.
    #Verificar se a tentativa é uma única letra.
    if len(tentativa) == 1 and tentativa.isalpha():
        #Verificar se a letra já foi utilizada.
        if tentativa in letras_utilizadas:
            print("Você já utilizou está letra antes: %s" % tentativa)
        #Verificar se a tentativa não está na palavra.
        elif tentativa not in palavra:
            print("A letra %s não está na palavra." % tentativa)
            tentativas -= 1
            letras_utilizadas.append(tentativa)
        #Quando a letra está na palavra.
        else:
            print("Você acertou a letra %s está na palavra." % tentativa)
            letras_utilizadas.append(tentativa)
            #Transformar a palavra em uma lista
            palavra_lista = list(palavra_a_completar)

            #Verifica onde pode substituir o underline baseado na letra que foi passada.
            indices = [i for i, letra in enumerate(palavra) if letra == tentativa]
            for indice in indices:
                palavra_lista[indice] = tentativa
            
            palavra_a_completar = "".join(palavra_lista)

            if "_" not in palavra_a_completar:
                advinhou = True
    
    #Tentativa de palavra completa.
    #Quando o usuário tenta advinhar a palavra toda da forca.
    elif len(tentativa) == len(palavra) and tentativa.isalpha():

        #Palavras já utilizadas.
        if tentativa in palavras_utilizadas:
            print("Você já utilizou está palavra %s." % tentativa)
        #Palavra está errada.
        elif tentativa != palavra:
            print("A palavra %s está incorreta." % tentativa)
            tentativa -=1
            palavras_utilizadas.append(tentativa)
        #Acertou a palavra.
        else:
            advinhou = True
            palavra_a_completar = palavra


    #Tentativa inválida.
    else:
        print("Tentativa inválida, tente novamente!")

    #Exibir o status do jogo.
    print(exibir_forca(tentativas))
    print(palavra_a_completar)

  #Finaliza o jogo se o usuário advinhou a palavra ou acabarqam as tentativas. 
  if advinhou:
   print("Parabéns! Você acertou a palavra.")
  else:
   print("Acabaram as tentativas, a palavra era: %s." % palavra)

#Status do Jogo.
def exibir_forca(tentativas):
  estagios = [  # Fim de jogo.
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / \\
                  -
              """,
              # Falta 1 tentativa.
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / 
                  -
              """,
              # Faltam 2 tentativas.
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |      
                  -
              """,
              # Faltam 3 tentativas.
              """
                  --------
                  |      |
                  |      O
                  |     \\|
                  |      |
                  |     
                  -
              """,
              # Faltam 4 tentativas.
              """
                  --------
                  |      |
                  |      O
                  |      |
                  |      |
                  |     
                  -
              """,
              # Faltam 5 tentativas.
              """
                  --------
                  |      |
                  |      O
                  |    
                  |      
                  |     
                  -
              """,
              # Estado inicial.
              """
                  --------
                  |      |
                  |      
                  |    
                  |      
                  |     
                  -
              """
  ]

  return estagios[tentativas]

#Iniciação do jogo e continuar jogando.
def iniciar():
    palavra = selecionar_palavra()
    jogar(palavra)
    #Quando acabar o jogo, verificar se o usuário quer continuar jogando.
    while input("Jogar novamente? (S/N)").upper() == "S":
        palavra = selecionar_palavra()
        jogar(palavra)

iniciar()