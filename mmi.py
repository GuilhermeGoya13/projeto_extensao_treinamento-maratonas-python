T = int(input())
for t in range(T):
    linha = input().split(" ")
    for i in range(len(linha)):
        if i == 0:
            maior = menor = int(linha[i])
        if menor > int(linha[i]):
            menor = int(linha[i])
        if maior < int(linha[i]):
            maior = int(linha[i])
    print(menor, maior)
    soma = sum([int(e) for e in linha])
    if t == T-1:
        print("S" if soma == int(linha[0]) * len(linha) else "N", end="")
    else:
        print("S" if soma == int(linha[0]) * len(linha) else "N")