secret_number = 8
guess = 0

while guess != secret_number:
    guess = int(input("Угадай число от 1 до 10: "))

    if guess < 1 or guess > 10:
        print("Введи число от 1 до 10")
    elif guess < secret_number:
        print("Мало")
    elif guess > secret_number:
        print("Много")
    else:
        print("Угадал!")
        