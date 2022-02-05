class Conta:
    # pass
    def __init__(self, numeroConta, titular, saldo, limite):
        self.numeroConta = numeroConta
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        
    def depositar(self, valor):
        valor = int(input('Digite quanto você deseja depositar: '))
        self.saldo+= valor
    
    def sacar(self, valor):
        valor=int(input('Digite quanto quer sacar'))
        self.saldo -= valor

    def verSaldo(self, saldo):
        return saldo