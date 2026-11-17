animal_sounds = {
    "кот": "мяу",
    "собака": "гав",
    "лошадь": "иго-го",
    "корова": "му",
    "осёл": "иа"
}

animal = input("Введите название животного: ").lower()
if animal in animal_sounds:
    new_sound = input(f"Введите новый звук для животного: ").lower()
    animal_sounds[animal] = new_sound
    print(animal_sounds)
else:
    print("Животное не найдено в списке.")
