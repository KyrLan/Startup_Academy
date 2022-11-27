def dict_united(*args):
    sum_dict = {}
    for i in args:
        sum_dict.update(i)
    print(sum_dict)


a = {"Зима": [12, 1, 2], "Весна": [3, 4, 5],}
b = {"Літо": [6, 7, 8], "Осінь": [9, 10, 11]}
dict_united(a, b)


