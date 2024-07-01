fib = int(input("введите число"))

a1 = 1
a2 = 1

for i in range (2,fib):
    a1, a2 = a2, a1 + a2
    print(a2)

int(input("Нажмите Enter чтобы закрыть программу"))


