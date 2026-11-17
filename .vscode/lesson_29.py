animals = ["КОТ", "СОБАКА", "ЛОШАДЬ", "КОРОВА", "СВИНЬЯ"]
search_animals = input("Введите название животного для поиска: ").upper().replace(","," ").split()
for search_animal in search_animals:
    if search_animal in animals:
        print(f"Животное '{search_animal}' найдено в списке.")
    else:
        print(f"Животное '{search_animal}' не найдено в списке.")
