from random import randint as r

# 1 Dificuldade para focalizar objetos de perto -> Hipermetropia
# 2 Sensação de olho pesado e cansado -> Hipermetropia
# 3 Embaçamento da visão -> Ambos
# 4 Visão turva, baça, distorcida ou desfocada ao longe -> Miopia
# 5 Necessidade de semicerrar os olhos para conseguir ver melhor -> Miopia

tabela_input = [
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 1, 1, 0, 1],
]

# 0 -> Hipermetropia e 1 -> Miopia

saida_esperada = [0, 1, 1, 0, 0, 1]

peso = [0, 0, 0, 0, 0]

for i in range(5):
    peso[i] = r(0, 1)

error = 1

print("Saída esperada:")
for i in range(len(tabela_input)):
    print(tabela_input[i], "->", saida_esperada[i])

input()


def ativacao(sum):
    if sum >= 1:
        return 1
    else:
        return 0


def calculaPeso():
    erro = 0
    for s in range(len(tabela_input)):
        sum = 0
        for k in range(len(peso)):
            sum += tabela_input[s][k] * peso[k]
        print(tabela_input[s], "->", ativacao(sum))

        if ativacao(sum) != saida_esperada[s]:
            erro = 1
            for k in range(len(peso)):
                if saida_esperada[s] == 1:
                    peso[k] += tabela_input[s][k]
                if saida_esperada[s] == 0:
                    if peso[k] != 0:
                        peso[k] -= tabela_input[s][k]
    return erro


iteracao = 1

while error != 0:
    print()
    print("Iteração " + str(iteracao) + ":")
    print("Pesos:", peso)
    print()
    iteracao += 1
    error = calculaPeso()
    print()

print("A rede neural aprendeu!")