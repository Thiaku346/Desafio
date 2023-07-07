import os

menu = f'''
    -----MENU-----

    [d] depositar
    [s] sacar
    [e] extrato
    [q] sair

    --------------
'''
continuar = f'''
    Continuar com a operação

    [1] Sim
    [2] Não
'''
saque = 0
saque1 = 0
saque2 = 0

deposito = 0
saldo = 2000
vezes_saque = 3

while True:

    print(menu)
    opcao = input("Digite a opcão: ")

    if opcao == "d" or opcao == "s" or opcao == "e" or opcao == "q":
#=========================deposito====================================
        if opcao == "d":
            
            deposito = float(input("Digite o valor de deposito: "))
            saldo = saldo + deposito
            os.system('cls') or None
            print(f"Deposito de R$ {deposito:.2f} realizado com sucesso!")

#==========================saque======================================
        elif opcao == "s":
            if vezes_saque > 0:
                
                if vezes_saque == 3:
                    saque = float(input("Digite o valor do saque: "))
                
                elif vezes_saque == 2:
                    saque1 = float(input("Digite o valor do saque: "))
                
                elif vezes_saque == 1:
                    saque2 = float(input("Digite o valor do saque: "))

                if saque > 500:
                    os.system('cls') or None
                    print("Saque indisponivel para valores acima de R$ 500,00")
                elif saque > saldo:
                    os.system('cls') or None
                    print("Saldo insuficiente!")
                else:
                    saldo = saldo - saque
                    vezes_saque = vezes_saque - 1
                    os.system('cls') or None
                    print(f"Saque de R$ {saque:.2f} realizado com sucesso!")
            else:
                os.system('cls') or None
                print("Limite de saque atingido, tente novamente mais tarde!")

#=========================extrato==================================
        elif opcao == "e":
            os.system('cls') or None

            if vezes_saque == 3:

                extract = f'''
            =========Extrato da Conta=========
            
            Saques:

                Saque de R$ {saque:.2f}.
            
            Depositos:

                Deposito de R$ {deposito:.2f}.
            
            Saldo Total:

                Saldo R$ {saldo:.2f}.
            ==================================
                '''
                print(extract)

            elif vezes_saque == 2:
                os.system('cls') or None
        
                extract = f'''
            =========Extrato da Conta=========
            
            Saques:

                Saque de R$ {saque:.2f}.
            
            Depositos:

                Deposito de R$ {deposito:.2f}.
            
            Saldo Total:

                Saldo R$ {saldo:.2f}.
            ==================================
                '''
                print(extract)
            
            elif vezes_saque == 1:
                os.system('cls') or None
        
                extract = f'''
            =========Extrato_da_Conta=========
            
            Saques:

                Saque de R$ {saque:.2f}.
                Saque de R$ {saque1:.2f}.
            
            Depositos:

                Deposito de R$ {deposito:.2f}.
            
            Saldo Total:

                Saldo R$ {saldo:.2f}.
            ==================================
                '''
                print(extract)
            
            elif vezes_saque == 0:
                os.system('cls') or None
        
                extract = f'''
            =========Extrato da Conta=========
            
            Saques:

                Saque de R$ {saque:.2f}.
                Saque de R$ {saque1:.2f}.
                Saque de R$ {saque2:.2f}.
            
            Depositos:

                Deposito de R$ {deposito:.2f}.
            
            Saldo Total:

                Saldo R$ {saldo:.2f}.
            ==================================
                '''
                print(extract)
#===================Sair======================================
        elif opcao == "q":
            os.system('cls') or None
            print("Saindo ...")

            break
#=======================continuar=============================
        if opcao != "q":
            print(continuar)
            opcao2 = input("Digite a opcão: ")

            if opcao2 == "1":
                os.system('cls') or None
                continue
            else:
                os.system('cls') or None
                print("Saindo...")
                break
    else:
        os.system('cls') or None
        print("Opcão não encontrada,tente novamente!")