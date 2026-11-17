# Спрашиваем, какое животное нужно заменить
old_animal = input("Введите животное, которое хотите заменить: ").strip().lower()

# Спрашиваем, какое новое животное нужно записать
new_animal = input("Введите новое животное: ").strip().lower()

# Открываем файл для чтения
with open("animals1.txt", "r", encoding="utf-8") as file:
    # Читаем все строки файла в список animals
    animals = file.readlines()

# Пока считаем, что старое животное не найдено
found = False

# Открываем тот же файл для полной перезаписи
with open("animals1.txt", "w", encoding="utf-8") as file:
    # По очереди берём каждую старую строку из списка
    for animal in animals:
        # Убираем пробелы и перенос строки, переводим текст в нижний регистр
        clean_animal = animal.strip().lower()

        # Проверяем, нужно ли заменить это животное
        if clean_animal == old_animal:
            # Записываем новое животное вместо старого
            file.write(new_animal + "\n")

            # Запоминаем, что замена действительно произошла
            found = True
        else:
            # Если это другое животное, возвращаем старую строку в файл
            file.write(animal)

# Проверяем, произошла ли замена
if found:
    # Сообщаем об успешной замене
    print(f"Животное {old_animal} заменено на {new_animal}.")
else:
    # Сообщаем, что старого животного в файле не было
    print(f"Животное {old_animal} не найдено.")
print ("Содержимое файла animals1.txt после замены:")
with open("animals1.txt", "r", encoding="utf-8") as file:   
    read_content = file.read()
    print(read_content)  # Отк
#рываем файл для чтения и выводим его содержимое    