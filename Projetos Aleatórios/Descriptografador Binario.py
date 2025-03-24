alfa = " abcdefghijklmnopqrstuvwxyz"
crip = input("Digite o código: ")
crip = crip.split(".")
num_desc = []
frase = ""
decimal = 0
contador = 0
for num_bi in crip:
    num_bi = num_bi[::-1]
    for num in num_bi:
        num = int(num) * 2** contador
        decimal += num
        contador += 1
    num_desc.append(decimal)
    decimal = 0
    contador = 0
for num in num_desc:
    frase = frase + alfa[num]
print(f"Frase Descriptografada: {frase}")