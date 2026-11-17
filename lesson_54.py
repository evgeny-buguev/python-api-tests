try:
    number = float(input("Enter a number: "))
    devisor = float(input("Enter a divisor: "))
    result = round(number / devisor, 2)
    print(f"The result of dividing {number} by {devisor} is: {result}, балять!!!")
except ValueError:
    print("Please enter a valid number for both inputs., балять.")
except ZeroDivisionError:
    print("Не дели на ноль, балатть, а то деняк не будет!")