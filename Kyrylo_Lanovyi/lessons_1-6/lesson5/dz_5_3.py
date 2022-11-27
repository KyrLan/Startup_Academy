def my_dict_two(name):
    new_dict = {}
    with open(name, 'r') as d:
        for i in d.read().splitlines():
            key, value = i.split(" - ")
            new_dict.update({key:value})
    return(new_dict)
a = 'IMD_rating.txt'
print(my_dict_two(a))
