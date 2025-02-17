num = 0

int_0_25 = 0
int_26_50 = 0
int_51_75 = 0
int_76_100 = 0

while (num >= 0):
    num = int(input("Insira um número: "))

    if (num >= 0 and num <= 25):
        int_0_25 += 1

    if (num >= 26 and num <= 50):
        int_26_50 += 1

    if (num >= 51 and num <= 75):
        int_51_75 += 1

    if (num >= 76 and num <= 100):
        int_76_100 += 1

print("[00,25]:", int_0_25)
print("[26,50]:", int_26_50)
print("[51,75]:", int_51_75)
print("[76,100]:", int_76_100)
