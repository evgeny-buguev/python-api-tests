first = float(input("Введите первую оценку: "))
second = float(input("Введите вторую оценку: "))
average = (first+ second)/2
print(f" Средняя оценка:{average:.1f}") 
if average >=70:
    print("Нормэ")
else:
    print("Плохо")