a = int(input("Insira 1º número: "))
b = int(input("Insira 2º número: "))
c = int(input("Insira 3º número: "))

if (a < b and a < c):  # a ... ...
    if (b < c):  # a b c
        print(a, "", b, "", c)
    else:  # a c b
        print(a, "", c, "", b)

if (b < a and b < c):  # b ... ...
    if (a < c):  # b a c
        print(b, "", a, "", c)
    else:  # b c a
        print(b, "", c, "", a)

if (c < a and c < b):  # c ... ...
    if (a < b):  # c a b
        print(c, "", a, "", b)
    else:  # c b a
        print(c, "", b, "", a)
