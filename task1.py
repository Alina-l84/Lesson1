from datetime import date
today = date.today( )
try:
    person1_birth_year  = int(input("Введите дату рождения первого человека: \n год: "))
    person1_birth_month = int(input("номер месяца: " ))
    person1_birth_day   = int(input("день: "))
    person2_birth_year  = int(input("Введите дату рождения второго человека: \n год: "))
    person2_birth_month = int(input("номер месяца: " ))
    person2_birth_day   = int(input("день: "))
except ValueError:
    print("Вводите только числа")

person1_age = today.year - person1_birth_year - ((today.month, today.day) < (person1_birth_month, person1_birth_day))
person2_age = today.year - person2_birth_year - ((today.month, today.day) < (person2_birth_month, person2_birth_day))

if person2_age < person1_age:
    print("Первый человек старше")
else:
    print("Второй человек старше")