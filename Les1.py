a = input("ВВедите число 1 ")
b = input("ВВедите число  2 ")
try:
    print("Результат:", int(a)/int(b))
except ValueError:
    print("Вводите только числа")
except TypeError:
    print("На ноль делить нельзя")
finally:
    print("Конструкция сработала!")





