jogo_enu = """ 1 | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9 """
numeros = "123456789"
jogadas = 0
quebrar = "n"
while quebrar != "s":
    repeticao = "n"
    while repeticao != "s":   
        print(jogo_enu)
        jgd_x = input("Jogador X, diga posição válida: ")
        if jgd_x in jogo_enu:
            jogo_enu = jogo_enu.replace(jgd_x, "X")
            repeticao = "s"
            jogadas += 1
        elif jgd_x not in jogo_enu:
            "Essa posição não está mais disponível!"
            continue
        for pos in range(1, 10, +4):
            if jogo_enu[pos] == "X" and jogo_enu[pos + 24] == "X" and jogo_enu[pos + 48] == "X":
                print("Jogador X venceu")
                quebrar = "s"
        for pos in range(1, 50, +24):
            if jogo_enu[pos] == "X" and jogo_enu[pos + 4] == "X" and jogo_enu[pos + 8] == "X":
                print("Jogador X venceu")
                quebrar = "s"
        if (jogo_enu[1] == "X" and jogo_enu[29] == "X" and jogo_enu[57] == "X") or (jogo_enu[9] == "X" and jogo_enu[29] == "X" and jogo_enu[49] == "X"):
            print("Jogador X venceu")
            quebrar = "s"
    if quebrar == "s":
        jogo_normal = jogo_enu
        for pos, num in enumerate(jogo_enu):
            if num in numeros:
                jogo_normal = jogo_normal.replace(num, " ", 1)
        print(jogo_normal)
        break 

    repeticao = "n"
    while repeticao != "s":
        print(jogo_enu)
        jgd_o = input("Jogador O, diga posição válida: ")
        if jgd_o in jogo_enu:
            jogo_enu = jogo_enu.replace(jgd_o, "O")
            repeticao = "s"
        elif jgd_o not in jogo_enu:
            "Essa posição não está mais disponível!"
            continue
        for pos in range(1, 10, +4):
            if jogo_enu[pos] == "O" and jogo_enu[pos + 24] == "O" and jogo_enu[pos + 48] == "O":
                print("Jogador X venceu")
                quebrar = "s"
        for pos in range(1, 50, +24):
            if jogo_enu[pos] == "O" and jogo_enu[pos + 4] == "O" and jogo_enu[pos + 8] == "O":
                print("Jogador O venceu")
                quebrar = "s"
        if (jogo_enu[1] == "O" and jogo_enu[29] == "O" and jogo_enu[57] == "O") or (jogo_enu[9] == "O" and jogo_enu[29] == "O" and jogo_enu[49] == "O"):
            print("Jogador O venceu")
            quebrar = "s"
    if quebrar == "s":
        jogo_normal = jogo_enu
        for pos, num in enumerate(jogo_enu):
            if num in numeros:
                jogo_normal = jogo_normal.replace(num, " ", 1)
        print(jogo_normal)
        break
    


#formas de ganhar

# 1  5  9
# 25 29 33
# 49 53 57

# posicao: 1   numero: 1
# posicao: 5   numero: 2
# posicao: 9   numero: 3
# posicao: 25   numero: 4
# posicao: 29   numero: 5
# posicao: 33   numero: 6
# posicao: 49   numero: 7
# posicao: 53   numero: 8
# posicao: 57   numero: 9