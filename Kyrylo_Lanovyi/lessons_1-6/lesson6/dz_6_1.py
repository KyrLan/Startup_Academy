import random

#1 Генеруємо випадкове число від 1 до 100

number = random.randint(1, 100)
#print(number) #Перевірка
#2 Створюємо цикл, що обмежує кількість спроб введення - 6
sproba = 0
while sproba <= 5:
    #3 Створюємо зміну для введення числа з консолі
    n = int(input("Вгадайте число від 1 до 100: "))
    #4  Якщо введене число з консолі  дорівнює заданому - перемога
    if n == number:
        sproba += 1
        print ("Вітаємо Ви вгадали задане число!!!" + f"\nКількість спроб - {sproba}")
        break
    #5 В іншому разі порівнюємо задане число і введене з консолі (більше/менше)
    else:
        #6 Якшо введене число менше - виводимо повідомлення і зменшуємо кількість спроб
        if n < number:
            sproba += 1
            print ("Ваше число менше за задане")
        # 6 Якшо введене число більше - виводимо повідомлення і зменшуємо кількість спроб
        else:
            sproba += 1
            print("Ваше число більше за задане")
    #7 Якщо кількість спроб перевищило 6 - програш
    if sproba == 6:
        print("Кількість спроб вичерпано, Ви програли =(")