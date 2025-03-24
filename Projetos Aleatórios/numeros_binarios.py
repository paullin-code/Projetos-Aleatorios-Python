def bi_dec(num_bi):
    decimal = 0
    contador = 0
    num_bi = str(num_bi)[::-1]
    for num in num_bi:
        num = int(num) * 2** contador
        decimal += num
        contador += 1
    return decimal


def dec_bi(num_dec):
    base = []
    binario = ""
    while num_dec != 1:
        if num_dec == 0:
            break
        base.append(num_dec % 2)
        num_dec //= 2
    base.append(num_dec)
    base = base[::-1]
    for num in base:
        binario = binario + str(num)
    return binario