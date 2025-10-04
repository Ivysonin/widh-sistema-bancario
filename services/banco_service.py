from services.conta_service import Conta
import random


class Banco:
    def __init__(self):
        self.contas = {}


    def gerar_numero_conta(self):
        while True:
            numero = str(random.randint(10000, 99999))
            if numero not in self.contas:
                return numero

    def cadastrar_conta(self, titular, senha):
        numero_conta = self.gerar_numero_conta()
        conta = Conta(numero_conta, titular, senha)
        self.contas[numero_conta] = conta
        return numero_conta

    def autenticar_conta(self, numero_conta, senha):
        conta = self.contas.get(numero_conta)
        if conta and conta.autenticar_senha_conta(senha):
            return conta
        return None

    def transferir(self, conta_origem, senha, conta_destino, valor):
        origem = self.autenticar_conta(conta_origem, senha)
        destino = self.contas.get(conta_destino)
        if not origem or not destino:
            return False
        if origem.sacar(valor):
            destino.depositar(valor)
            origem.registrar_historico("TRANSFERÊNCIA ENVIO", valor, conta_destino)
            destino.registrar_historico("TRANSFERÊNCIA RECEBIDA", valor, conta_origem)
            return True
        return False