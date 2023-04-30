birth_year  = int(input("Введите дату вашего рождения: \n год: "))
birth_month = int(input("месяц: " ))
birth_day   = int(input("число: "))

# current date
today_day = 30
today_month = 4
today_year = 2023

age_year = today_year - birth_year

if today_month < birth_month:
    age_year = age_year - 1
elif today_month == birth_month:
    if today_day < birth_day:
        age_year = age_year - 1

print("Ваш возраст:", age_year)
