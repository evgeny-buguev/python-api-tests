animals = ["кот", "собака", "лошадь", "корова", "свинья"]



search_animals = input("Введите животных через запятую: ").split(",")

for search_animal in search_animals:
    search_animal = search_animal.strip()

    if search_animal in animals:
        print(f"Животное {search_animal} найдено в списке.")
    else:
        print(f"Животное {search_animal} не найдено в списке.")