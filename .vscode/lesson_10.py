import os

if os.path.exists("animals.txt"):
    with open("animals.txt", "r", encoding="utf-8") as file:
        animals = file.read().splitlines()
else:
    animals = ["кот", "собака"]

new_animal = input("Какое животное добавить? ")
animals.append(new_animal)

with open("animals.txt", "w", encoding="utf-8") as file:
    for animal in animals:
        file.write(animal + "\n")

for animal in animals:
    print(animal)