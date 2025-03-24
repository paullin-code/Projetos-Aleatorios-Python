import os

os.system("cls")
boneco = """_
 |
 O
/|\\
/ \\
"""
palavra = input("Digite uma palavra para ser adivinhada: ").upper()
os.system("cls")
resultado = palavra
contagem_erros = 6
letras_salvas = ""
sem_espaco = ""
for numero, letra in enumerate(palavra):
    resultado = resultado.replace(letra, str(numero), 1)
while sem_espaco != palavra:
    if contagem_erros == 15:
        print(f"Voçe perdeu a palavra era {palavra.upper()}")
        break
    letra_dig = input("Digite uma letra: ").upper()
    if letra_dig in sem_espaco:
        print("Você digitou essa letra!")
        print(boneco[:contagem_erros:])
        print(letras_salvas)
        continue
    for num,letra in enumerate(palavra):
        if letra_dig == letra: 
            resultado = resultado.replace(str(num), f"{letra_dig} ")
            letras_salvas = resultado 
            for num in range(len(palavra)):
                letras_salvas = letras_salvas.replace(str(num), "_ ")
        elif letra_dig not in palavra:
            if contagem_erros == 7:
                contagem_erros += 2
            elif contagem_erros == 11:
                contagem_erros += 3
            else:                  
                contagem_erros += 1
            print("Essa letra não esta na palavra!")
            if contagem_erros == 12:
                contagem_erros = 15
            break
    if letras_salvas != None:
        print(boneco[:contagem_erros:])
        print(letras_salvas)
        sem_espaco = resultado.replace(" ", "")
if sem_espaco == palavra:
    print("Você venceu!!!")
# print(boneco[:7:]) # cabeça
# print(boneco[:9:]) # braço um
# print(boneco[:10:]) # corpo
# print(boneco[:11:]) # braço dois
# print(boneco[:13:]) # perna um
# print(boneco[:15:]) # perna dois