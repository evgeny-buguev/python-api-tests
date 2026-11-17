while True:
    try:
        age = int(input("Enter your age, балять: "))
        break
    except ValueError:
        print("Please enter a valid number for your age., балять.")
print("Your age in 100 years will be: ", age + 100, "and you won't be around anymore, so don't worry about it! БАЛАТЬ")