from random import randint as r

# 1 Teve dificuldade na aprendizagem de leitura -> Dislexia
# 2 Tem dificuldade em soletrar palavras -> Dislexia
# 3 Costuma deixar projetos pela metade -> TDAH
# 4 Frequentemente se distrai com barulhos em volta -> TDAH
# 5 Prefere ler artigos curtos e revistas do que livros extensos -> Dislexia

tabela_input = [
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 1, 1, 0, 1],
]

# 0 -> TDAH e 1 -> Dislexia

saida_esperada = [0, 1, 0, 0, 1, 1]

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

print("Aprendeu!!")

print()
print()

print("Agora responda as perguntas (1 para sim e 0 para não):")

entrada = [0, 0, 0, 0, 0]

print("Teve dificuldade na aprendizagem de leitura?")
entrada[0] = input()

print("Tem dificuldade em soletrar palavras?")
entrada[1] = input()

print("Costuma deixar projetos pela metade?")
entrada[2] = input()

print("Frequentemente se distrai com barulhos em volta?")
entrada[3] = input()

print("Prefere ler artigos curtos e revistas do que livros extensos?")
entrada[4] = input()

soma = 0

for j in range(len(entrada)):
    soma += int(entrada[j]) * peso[j]

if soma == 0:
    print("Você tem TDAH")
else:
    print("Você tem dislexia")
