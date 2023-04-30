from datetime import date
from dateutil import relativedelta

birth_year  = int(input("Введите дату вашего рождения: \n год: "))
birth_month = int(input("месяц: " ))
birth_day   = int(input("число: "))

current_date = date.today( )
birth_date = date(birth_year, birth_month, birth_day)
# print("Birth Date: ", birth_date)
# print("Current Date: ", current_date)

age = relativedelta.relativedelta(current_date,birth_date)
print("Ваш возраст: ", age.years)