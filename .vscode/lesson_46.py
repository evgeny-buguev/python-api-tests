def check_age(age):
    if age >= 18:
        return "Продаим алокоголь"
    else:
        return "Продим молоко"

age = float(input("Сколько лет?:    "))
result = check_age(age)
print(result)