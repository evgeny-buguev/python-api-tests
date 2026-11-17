try:
    age=int(input("Please enter your age: "))
    print("Ваш восраст через 100 лет будет: ", age+100, "и тебя уже не будет на этом свете, так что не парься!")
except ValueError:
    print("Вы ввели не число. Пожалуйста, введите число. ЗАЕБАЛ!")