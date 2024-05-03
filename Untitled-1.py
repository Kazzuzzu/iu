# -*- coding: utf-8 -*-


menu = '''


[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=>'''

nao = "EXTRATO"
saldo = 0
limite = 2000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opção = input(menu)
    
    if opção == "d":
        valor = float(input("Informe o valor a ser depósitado: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$  {valor:.2f}\n"
        
        else:
            print("Operação falou! O valor é invalido.")
    
    elif opção == "s":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo.")
            
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite.")
        
        elif excedeu_saques:
            print("Operação falhou! Numero de saques maximo ultrapassado")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            
        else:
            print("Operação falhou! Ovalor não é valido.")
    
    elif opção == "e":
        print("\n======== EXTRATO =========")
        print("Não foram realizadas moventações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("============================")
    
    elif opção == "q":
        break
        
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        
        
print("Obrigado por utilizar o nosso sistema!")