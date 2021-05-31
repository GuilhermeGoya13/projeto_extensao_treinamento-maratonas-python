n1 = int(input())
simboloA = input()
n2 = int(input())
simboloB = input()
n3 = int(input())
total = 0
c = 0
if simboloB in "/*" and simboloA in "+-":
    if simboloB == "/":
        if n3 == 0:
            print("erro", end="")
            quit()
        else:
            total = n2 // n3
    elif simboloB == "*":
        total = n2 * n3
    if simboloA == "+":
        total += n1
    elif simboloA == "-":
        total = n1 - total
else:
    if simboloA == "/":
        if n2 == 0:
            print("erro", end="")
            quit()
        else:
            total = n1 // n2
    elif simboloA == "*":
        total = n1 * n2
    if simboloA == "+":
        total = n1 + n2
    elif simboloA == "-":
        total = n1 - n2
    elif simboloA == "*":
        total = n1 * n2
    if simboloB == "+":
        total += n3
    elif simboloB == "-":
        total -= n3
    elif simboloB == "*":
        total *= n3
    elif simboloB == "/":
        if n3 == 0:
            print("erro", end="")
            quit()
        else:
            total //= n3
print(total, end="")