def pal(n):
    m = list(n)
    k = []
    for i in list(m):
        k.insert(0, i)
    return (m == k)

p = pal('випив')
print(p)