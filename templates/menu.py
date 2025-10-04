from services.banco_service import Banco
from time import sleep


def menu():
    banco = Banco()

    while True:
        print("\n-=-= BANCO PYTHON -=-=")
        print("1 - Criar conta")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Transferir")
        print("5 - Consultar saldo")
        print("6 - Extrato")
        print("7 - Sair")
        opcao = input("Escolha: ")

        match opcao:
            case "1":
                nome = input("Nome do titular: ")
                senha = input("Senha: ")
                num = banco.cadastrar_conta(nome, senha)
                print(f"Conta criada! Número: {num}")
                sleep(2)

            case "2":
                num = input("Número da conta: ")
                senha = input("Senha: ")
                valor = float(input("Valor do depósito: "))
                conta = banco.autenticar_conta(num, senha)

                if conta and conta.depositar(valor):
                    print("Depósito realizado.")
                else:
                    print("Falha para depósitar.")
                sleep(2)

            case "3":
                num = input("Número da conta: ")
                senha = input("Senha: ")
                valor = float(input("Valor do saque: "))
                conta = banco.autenticar_conta(num, senha)

                if conta and conta.sacar(valor):
                    print("Saque realizado.")
                else:
                    print("Verifique o seu saldo e as informações que estão sendo passadas!")
                sleep(2)

            case "4":
                origem = input("Conta de origem: ")
                senha = input("Senha da origem: ")
                destino = input("Conta de destino: ")
                valor = float(input("Valor da transferência: "))

                if banco.transferir(origem, senha, destino, valor):
                    print("Transferência concluída.")
                else:
                    print("Falha na transferência.")
                sleep(2)

            case "5":
                num = input("Número da conta: ")
                senha = input("Senha: ")
                conta = banco.autenticar_conta(num, senha)
                print(f'\nSaldo atual: {conta.exibir_saldo()}')
                sleep(2)
            
            case "6":
                num = input("Número da conta: ")
                senha = input("Senha: ")
                conta = banco.autenticar_conta(num, senha)
                
                if conta:
                    print(f"\nSaldo: R${conta.saldo:.2f}")
                    print("\nHistórico:")
                    for historico in conta.historico:
                        print('\n-=-=-=-=')
                        print(f'Tipo: {historico["tipo"]}')
                        print(f'Valor: {historico["valor"]}')
                        print('Nenhum registro!' if historico["destino"] == None else f'Destino: {historico["destino"]}')
                        print(f'Saldo atual: {historico["saldo_att"]}')
                    sleep(4)
                else:
                    print("Informações inválidas!")
                    sleep(2)

            case "7":
                print("Saindo...")
                sleep(2)
                break

            case _:
                print("\nOpção inválida.")
                sleep(2)