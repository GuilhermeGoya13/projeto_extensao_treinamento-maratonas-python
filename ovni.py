T = int(input())
for t in range(T):
    linha = input().split(" ")
    a = float(linha[0])
    b = float(linha[1])
    total = float(linha[2])
    if t == T-1:
        print("CABE!" if total >= a + b else "NAO CABE!", end="")
    else:
        print("CABE!" if total >= a + b else "NAO CABE!")