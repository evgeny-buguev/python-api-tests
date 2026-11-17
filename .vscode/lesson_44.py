def make_massage(animal,sound):
    massage = f"{animal} говорит {sound}"
    return massage

animal = input("Введите животное: ")
sound = input("Введите звук: ")
result = make_massage(animal,sound)
print(result)

