#Crie um programa que receba a renda do usuario;
#Baseado na renda ele vai liberar um limite para o cartao de credito;
#Se for menos que 2000, 1000 de limite;
#Menos de 4000, 2000 de limite;
#Menos de 6000, 3000 de limite;
#Se for maior que 10000, insira uma mensagem para falar com o gerente;

print("Olá, tudo bem seja bem-vindo ao banco agiota.")
print ("Por favor digite o a sua renda para assim podermos liberar um cartão de crédito com um limide O ;) ")

renda = float(input("Digite a sua renda: "))

if renda <= 2000:
  print("Seu limite é de R$1.000.")
elif renda <= 4000 and renda > 2000:
  print("Seu limite é de R$2.000.")
elif renda <= 6000 and renda > 4000:
  print("Seu limite é de R$3.000.")
elif renda > 10000 and renda < 6000:
  print("Venha conversar com o nosso gerende.")