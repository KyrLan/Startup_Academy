n = int(input("Ведіть число: "))

def rec(x):
    if x != 0:
        print(x)
        rec(x-1)
rec(n)
