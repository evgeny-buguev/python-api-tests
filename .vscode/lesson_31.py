animal_sounds ={
    "кот": "мяу",
    "собака": "гав",  
    "лошадь": "иго-го",
    "корова": "му",
    "осел": "иа",
}
new_animal = input("Введите название животного: ").lower()
new_sound = input("Введите звук, который издает животное: ").lower()
animal_sounds[new_animal] = new_sound
print(animal_sounds)