search_animal = input("Какое животное найти: ").lower()
with open("animals1.txt", "r", encoding="utf-8") as file:
    for animal in file:
        animal = animal.strip().lower()
        if animal == search_animal:
            print(f"Животное {search_animal} найдено!")
            break
    else:
        print(f"Животное {search_animal} не найдено.")