# from numeros_binarios import *
from numeros_binarios import bi_dec, dec_bi
from os import system

resp = "S"
while resp == "S":
    opcao = input("Deseja converter de BINÁRIO para DECIMAL(BD) ou DECIMAL para BINÁRIO(DB): ").upper()
    system("cls")
    if opcao == "BD":
        try:
            numero = int(input("Digite o número BINÁRIO: "))
            resp = bi_dec(numero)
            print(f"Binário: {numero} | Decimal: {resp}")
            while True:
                resp = input("Deseja continuar(S/N): ").upper()
                if resp == "S":
                    break
                elif resp == "N":
                    break
                else:
                    print("Você digitou algo errado! Tente novamente!")
                    continue
        except ValueError :
            print("Você errou em alguma coisa! Tente novamente!")
            continue
    elif opcao == "DB":
        try:
            numero = int(input("Digite o número DECIMAL: "))
            resp = dec_bi(numero)
            print(f"Binário: {numero} | Decimal: {resp}")
            while True:
                resp = input("Deseja continuar(S/N): ").upper()
                if resp == "S":
                    break
                elif resp == "N":
                    break
                else:
                    print("Você digitou algo errado! Tente novamente!")
                    continue
        except ValueError :
            print("Você errou em alguma coisa! Tente novamente!")
            continue
    if opcao != "BD" and opcao != "DB":
        print("Digite uma opção VÁLIDA!")
        continue