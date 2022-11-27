def month_number(n):
    time_dict = {"Зима": [12, 1, 2], "Весна": [3, 4, 5],
                 "Літо": [6, 7, 8], "Осінь": [9, 10, 11]}
    for time, month in time_dict.items():
        for num in month:
            if num == n:
                print(f"Вказаний місяць відноситься до пори року - {time}")


month_number(12)