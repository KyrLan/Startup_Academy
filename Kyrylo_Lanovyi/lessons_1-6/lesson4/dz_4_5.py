def letter_count(n):
    count_dict = {}
    for i in n:
        if i not in count_dict:
            count_dict[i] = 0
        count_dict[i] += 1
    #print(count_dict)
    print(max(count_dict, key = count_dict.get))

letter_count('бууууатуааааааат')