animals = {
    "кот": {
        "звук": "мяу",
        "возраст": 3
    },
    "собака": {
        "звук": "гав",
        "возраст": 5
    }
}

while True:
    command = input("Команда — показать или выход: ").lower()

    if command == "показать":
        for animal, info in animals.items():
            print(f"{animal}: звук — {info['звук']}, возраст — {info['возраст']}")

    elif command == "выход":
        break

    else:
        print("Неизвестная команда")