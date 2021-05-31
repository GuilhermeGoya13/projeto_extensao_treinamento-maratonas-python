entrada = input().split(" ")
a = int(entrada[0])
b = int(entrada[1])
if a > 0 and b > 0:
    print("R1", end="")
elif a > 0 and b < 0:
    print("R4", end="")
elif a < 0 and b > 0:
    print("R2", end="")
elif a < 0 and b < 0:
    print("R3", end="")
else:
    print("NO ALVO!", end="")