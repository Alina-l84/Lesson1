from datetime import date
today = date.today( )
birth_year  = int(input("Введите дату вашего рождения: \n год: "))
birth_month = int(input("месяц: " ))
birth_day   = int(input("число: "))
age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
print("Ваш возраст: ", age)

