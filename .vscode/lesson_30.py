animal_sounds ={
    "кот": "мяу",
    "собака": "гав",  
    "лошадь": "иго-го",
    "корова": "му",
    "осел": "иа",
}
animal=input("Введите название животного: ").lower()
if animal in animal_sounds:
    print(animal_sounds[animal])
else:
    print("Животное не найдено в списке.")