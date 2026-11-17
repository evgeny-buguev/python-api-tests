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
animal = input("Введите животное: ").lower()
if animal in animals:
    print(f"звук:{animals[animal]["звук"]},возраст: {animals[animal]["возраст"]}")
    
else:
    print("Такого животного нет в словаре")