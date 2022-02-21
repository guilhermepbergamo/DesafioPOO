from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca

banco = Banco()

cliente1 = Cliente('Guilherme', 23)
cliente2 = Cliente('Roberval', 51)
cliente3 = Cliente('Maria Aparecida Campos Pinheiro Bergamo', 52)

conta1 = ContaPoupanca(1111, 275498, 0)
conta2 = ContaCorrente(3333, 275497, 0)
conta3 = ContaPoupanca(1122, 275496, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)

banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)

if banco.autenticar(cliente1):
  cliente1.conta.depositar(40)
  cliente1.conta.sacar(20)
else:
  print('Cliente não autenticado.')

print('=-'*30)

if banco.autenticar(cliente2):
  cliente2.conta.depositar(0)
  cliente2.conta.sacar(20)
else:
  print('Cliente não autenticado.')
