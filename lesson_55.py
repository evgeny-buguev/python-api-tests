try:
    number = float(input("Enter a number: "))
    divisor = float(input("Enter a divisor: "))
    result = number / divisor
except ValueError:
    print("Ты пиздец, введи нормальные числа!")
except ZeroDivisionError:
    print("Не дели на ноль, балатть, а то деняк не будет!")
else:
    print(f"The result of dividing {number} by {divisor} is: {result}, балять!!!")
finally:
    # Сообщаем, что попытка вычисления закончена
    print("Программа закончила работу, балатть!")