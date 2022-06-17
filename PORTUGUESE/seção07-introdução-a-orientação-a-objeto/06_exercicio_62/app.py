#Crie um sistema que simule um banco, a classe deve ter um método de saque, depósito e tranferencia;
#Propriedades nome do proprietário da conta, saldo e quais você mais procura;
#Realizar saques, depósito e tranferência entre contas;

class Banco:
  def __init__(self, nome, saldo):
    self.nome = nome
    self.saldo = saldo

  #Saque da conta
  def saque(self, valor):
    self.saldo -= valor
  
  #Deposito da conta
  def deposito(self, valor):
    self.saldo += valor
  
  #Transferencia de dinheiro para outra conta
  def tranferncia_bancaria(self, outra_conta, valor):
    self.saldo -= valor
    outra_conta.saldo += valor
  
  #Transferencia via PIX
  def tranferncia_pix(self, outra_conta, valor):
    self.saldo -= valor
    outra_conta.saldo += valor

#Contas Bancárias

#Conta do Diusval
conta_diusval = Banco("Diusval", 15000)

#Conta da Luiza
conta_luiza = Banco("Luiza", 8000)

#Conta do Frank
conta_frank = Banco("Frank", 6000)

#Conta do Agiota
conta_agiota = Banco("Agiota", 158000)

#Nomes e valores de cada conta

print("Contas Bancário do Banco QUERO MAIS DINHEIRO com o valor do saldo.")

#Diusval
print(conta_diusval.nome)

print(conta_diusval.saldo)

#Luiza
print(conta_luiza.nome)

print(conta_luiza.saldo)

#Frank
print(conta_frank.nome)

print(conta_frank.saldo)

#Agiota
print(conta_agiota.nome)

print(conta_agiota.saldo)

#Depositando dinheiro nas conta

print("Contas Bancário do Banco QUERO MAIS DINHEIRO com o valor do saldo atualizado após o deposito.")

#Deposito na conta do Diusval
conta_diusval.deposito(5000)
#Valor atualizado da conta
print(conta_diusval.nome)

print(conta_diusval.saldo)

#Deposito na conta da Luiza
conta_luiza.deposito(7000)
#Valor atualizado da conta
print(conta_luiza.nome)

print(conta_luiza.saldo)

#Deposito na conta do Frank
conta_frank.deposito(2500)
#Valor atualizado da conta
print(conta_frank.nome)

print(conta_frank.saldo)

#Deposido na conta do Agiota
conta_agiota.deposito(1500)
#Valor atualizado da conta
print(conta_agiota.nome)

print(conta_agiota.saldo)

#Saque dinheiro nas conta

print("Contas Bancário do Banco QUERO MAIS DINHEIRO com o valor do saldo atualizado após o saque.")

#Saque na conta do Diusval
conta_diusval.saque(2000)
#Valor atualizado da conta
print(conta_diusval.nome)

print(conta_diusval.saldo)

#Saque na conta da Luiza
conta_luiza.saque(350)
#Valor atualizado da conta
print(conta_luiza.nome)

print(conta_luiza.saldo)

#Saque na conta do Frank
conta_frank.saque(2500)
#Valor atualizado da conta
print(conta_frank.nome)

print(conta_frank.saldo)

#Saque na conta do Agiota
conta_agiota.saque(112000)
#Valor atualizado da conta
print(conta_agiota.nome)

print(conta_agiota.saldo)

#Transferencia Bancária e via PIX

print("Contas Bancário do Banco QUERO MAIS DINHEIRO com o valor do saldo atualizado após as Transferências.")

#transferencia na conta do Diusval
conta_diusval.tranferncia_pix(conta_luiza, 1500)
#Valor atualizado da conta
print(conta_diusval.nome)

print(conta_diusval.saldo)

#transferencia na conta do Luiza
conta_luiza.tranferncia_bancaria(conta_diusval, 500)
#Valor atualizado da conta
print(conta_luiza.nome)

print(conta_luiza.saldo)

#transferencia na conta do Frank
conta_frank.tranferncia_pix(conta_diusval, 2000)
#Valor atualizado da conta
print(conta_frank.nome)

print(conta_frank.saldo)

#transferencia na conta do Agiota
conta_agiota.tranferncia_bancaria(conta_frank, 5000)
#Valor atualizado da conta
print(conta_agiota.nome)

print(conta_agiota.saldo)
