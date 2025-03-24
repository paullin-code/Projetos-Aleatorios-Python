alfa = " abcdefghijklmnopqrstuvwxyz"
nums_bi = []
crip = "."
frase = input("Digite uma frase: ")
for letra in frase:
    binario = ""
    base = []
    index = alfa.index(letra)
    while index != 1:
        if index == 0:
            break
        base.append(index % 2)
        index //= 2
    base.append(index)
    base = base[::-1]
    for num in base:
        binario = binario + str(num)
    nums_bi.append(binario)
crip = crip.join(nums_bi)
print(f"Frase Criptografada: {crip}")