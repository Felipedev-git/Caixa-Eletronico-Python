sistema = {'FELIPE' : '1234', 
           'ADMIN' : '0000'}
saldo = 1000
extrato = []

while True:
    user = input('Digite seu login: ').upper()
    senha = input('Digite sua senha: ')

    if user not in sistema:
        print('Usuario não existe! ')
        continue
    elif senha == sistema[user]:
        print('Seja bem-vindo! ')
        break
    else:
        print('Acesso negado! ')
        continue
while True:
    print('=== MENU === \n1. Ver Saldo \n2. Depositar \n3. Sacar \n4. Ver Extrato \n5. Sair')

    selecao = input('Selecione como gostaria de prosseguir: ')
    if selecao == '1':
        print(f'Seu saldo é R${saldo:.2f}! ')
        continue
    elif selecao == '2':
        deposito = float(input('Quanto gostaria de depositar: '))
        saldo = deposito + saldo
        extrato.append(f"Depósito: + R$ {deposito:.2f}")
        print(f'Seu saldo atual é de R${saldo:.2f}')
        continue
    elif selecao == '3':
        saque = float(input('Selecione a quantidade: '))
        if saque > saldo:
            print('Saldo insuficiente: ')
            continue
        saldo = saldo - saque
        extrato.append(f"Saque: - R$ {saque:.2f}")
        print(f'Seu saldo atual é R${saldo:.2f}! ')
        continue
    elif selecao == '4':
        for i in range(len(extrato)):
            print(f'{extrato[i]}')
        print("---------------------------------")
        print(f"Saldo Atual: R$ {saldo:.2f}")
        print("=================================")
    elif selecao == '5':
        print('Obrigado por utilizar! ')
        break
    else:
        print('Selecione uma opção valida. ')
        continue
   