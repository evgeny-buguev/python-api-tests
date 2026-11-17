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

for animal, info in animals.items():
    print(f"{animal}:звук - {info["звук"]},возраст - {info["возраст"]}")