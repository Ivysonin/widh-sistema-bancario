import hashlib


class Conta:
    def __init__(self, numero, titular, senha):
        self.numero = numero
        self.titular = titular
        self.senha_hash = hashlib.sha256(senha.encode()).hexdigest()
        self.saldo = 0.0
        self.historico = []

    def autenticar_senha_conta(self, senha):
        return self.senha_hash == hashlib.sha256(senha.encode()).hexdigest()

    def registrar_historico(self, tipo, valor, destino=None):
        self.historico.append({
            "tipo": tipo,
            "valor": valor,
            "destino": destino,
            "saldo_att": self.saldo
        })

    def depositar(self, valor):
        if valor <= 0:
            return False
        self.saldo += valor
        self.registrar_historico("DEPÓSITO", valor)
        return True

    def sacar(self, valor):
        if valor <= 0 or valor > self.saldo:
            return False
        self.saldo -= valor
        self.registrar_historico("SAQUE", valor)
        return True

    def exibir_saldo(self):
        return self.saldo