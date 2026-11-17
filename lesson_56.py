import random
secret_number = random.randint(1, 10)
while True:
    try:
        guess = int(input("Угадай число от 1 до 10: "))
        if guess == secret_number:
            print(f"УГАДАЛ!!!{secret_number} БАЛАТЬ! длбач бля")
            break
        elif guess < 1 or guess > 10:
             print("Число должно быть от 1 до 10, балять!")
        elif guess < secret_number:
            print("Маловато, балять!")
        
        else:
            print("Многовато, балять!")
    except ValueError:
            print("Пожалуйста, введите корректное число! БАлять.")
            