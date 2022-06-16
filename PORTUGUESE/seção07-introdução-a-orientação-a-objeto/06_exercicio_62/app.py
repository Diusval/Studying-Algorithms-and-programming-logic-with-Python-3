#Crie um sistema que simule um banco, a classe deve ter um método de saque, depósito e tranferencia;
#Propriedades nome do proprietário da conta, saldo e quais você mais procura;
#Realizar saques, depósito e tranferência entre contas;

class Banco:
  def __init__(self, nome, saldo):
    self.nome = nome
    self.saldo = saldo
  
#Método para depositar dinheiro
  def deposito(self, valor):
    self.saldo += valor

#Método para sacar dinheiro  
  def saque(self, valor):
    self.saldo -= valor

#Método para transferir dinheiro
  def transferencia(self, outra_conta, valor):
    self.saldo -= valor
    outra_conta.saldo += valor

conta_diusval = Banco("Diusval", 1000)

#Nome da conta do usuário
print(conta_diusval.nome)

#valor na conta do usuário
print(conta_diusval.saldo)

#Deposito na conta do usuário
conta_diusval.deposito(1000)

print(conta_diusval.saldo)

#Saque na conta do usuário
conta_diusval.saque(500)

print(conta_diusval.saldo)

#conta do agiota
conta_agiota = Banco("Douglinhas", 90000)

#Nome da conta do usuário
print(conta_agiota.nome)

#valor na conta do usuário
print(conta_agiota.saldo)

#Trânsferencia Bancaria
conta_diusval.transferencia(conta_agiota, 200)
print(conta_agiota.saldo)

#valor na conta
print(conta_diusval.saldo)