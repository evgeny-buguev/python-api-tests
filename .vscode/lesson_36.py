animal_sounds = {
    "кот": "мяу",
    "собака": "гав",
    "корова": "му"
}
animal = input("Введите животное: ").lower()
print(animal_sounds.get(animal, "Такого животного нет в словаре"))