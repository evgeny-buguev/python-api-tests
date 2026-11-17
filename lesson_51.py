try:
    with open("animals11.txt", "r", encoding="utf-8") as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print("The file 'animals11.txt' was not found.")