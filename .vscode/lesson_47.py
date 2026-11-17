animal = input("Введите животное: ")
with open("animals1.txt", "a", encoding="utf-8") as file:
    file.write(animal + "\n")
print(f"Животное {animal} добавлено в файл animals1.txt")
print("Содержимое файла animals1.txt:")
with open("animals1.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)