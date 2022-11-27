def my_dict(dict, name):
    with open(name, 'w') as d:
        for key, value in dict.items():
            d.write(str(key) + " - " + str(value) + "\n")


a = {'Сяйво': 8.4, 'Початок': 8.7, 'Джокер': 8.3}
b = 'IMD_rating.txt'
my_dict(a, b)