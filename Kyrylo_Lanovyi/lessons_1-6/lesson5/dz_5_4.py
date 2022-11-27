import os
def derect():
    l = os.listdir()
    print(l)
    m = 0
    n = 0
    for i in l:
        a = i.split()
        sym = "|"
        if sym not in i:
            m += 1
        else:
            n += 1
    print (f"Кількість каталогів - {n}")
    print(f"Кількість файлів - {m}")

derect()


