delete_animal = input("Введите кого хотите удалить: ").lower()
with open("animals1.txt", "r", encoding="utf-8") as file:
    animals = file.readlines()
found = False
with open("animals1.txt", "w", encoding="utf-8") as file:
    for animal in animals:
        if animal.strip().lower() ==delete_animal:
            found = True
        else:
            file.write(animal)
if found:
    print(f"Животное {delete_animal} удалено")
else:
    print(f"Животное {delete_animal} не найдено.")

with open("animals1.txt", "r", encoding="utf-8") as file:
    updated_animals = file.readlines()
    for animal in updated_animals:
        print(f"{animal.strip()} - это еще живое")