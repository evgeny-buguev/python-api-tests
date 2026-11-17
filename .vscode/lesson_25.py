grades = []

for number in range(1,6):
    grade =float(input(f" оценка {number}: "))
    grades.append(grade)

average = sum(grades) / len (grades)
print(f"Средняя оценка: {average:.1f}")

    
