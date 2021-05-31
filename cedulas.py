valor = int(input())
a = valor // 100
valor -= 100 * a
b = valor // 50
valor -= 50 * b
c = valor // 20
valor -= 20 * c
d = valor // 10
valor -= 10 * d
e = valor // 5
valor -= 5 * e
f = valor // 2
valor -= 2 * f
g = valor // 1
print(
    "{} nota(s) de R$ 100\n{} nota(s) de R$ 50\n{} nota(s) de R$ 20\n{} nota(s) de R$ 10\n{} nota(s) de R$ 5\n{} nota(s) de R$ 2\n{} nota(s) de R$ 1".format(
        a, b, c, d, e, f, g), end="")