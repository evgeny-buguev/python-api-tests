animals = {
    "кот": {
        "звук": "мяу",
        "возраст": 3
    },
    "собака": {
        "звук": "гав",
        "возраст": 5
    }
}
new_animal = input("Введите животное: ").lower()
new_sound = input("Введите звук: ").lower()
new_age = int(input("введите возраст "))
animals[new_animal] = {
    "звук": new_sound,
    "возраст": new_age
}
print(animals)