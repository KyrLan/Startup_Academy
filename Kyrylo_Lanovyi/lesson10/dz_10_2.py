import sys
def unic(my_list):
    unic_list = []
    try:
        for i in my_list:
            if i not in unic_list:
                unic_list.append(int(i))
    except ValueError as ex1:
        print(f"Помилка {ex1}: Список містить невірний тип даних", file=sys.stderr)
    except Exception:
        print("Невідома помилка", file = sys.stderr)

    if len(my_list) == len(unic_list):
        print('Всі значення списку є унікальними')
    else:
        print('Список містить повторювані значення')


test_list = [1, "a", 3, 4, 55, 55, 66, 78]

unic(test_list)