poupanca = 500

saque = float(input("Quanto deseja sacar: "))

if saque <= poupanca:
  print("Você sacou R$%.2f." % saque)
else:
  print("Você não tem saldo para sacar R$%.2f." % saque)
  print("Sua poupança tem no momento R$%.2f." % poupanca)