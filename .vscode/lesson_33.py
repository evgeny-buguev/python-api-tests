animal_sounds = {
    "кот": "мяу",
    "собака": "гав",
    "лошадь": "иго-го",
    "корова": "му",
    "осёл": "иа"
}
animal = input("Какое животное удалить: ").lower()

if animal in animal_sounds:
    del animal_sounds[animal]
    print(animal_sounds)
else:
    print("Такого животного нет в словаре.")
print("Словарь после удаления:", animal_sounds)