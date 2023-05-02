try:
    number = int(input("Введите трехзначное число: "))
    if 100<number<1000:
        sum = int(str(number)[0]) + int(str(number)[1]) + int(str(number)[2])
        print("Сумма цифр:", sum)
        mult = int(str(number)[0]) * int(str(number)[1]) * int(str(number)[2])
        print("Произведение цифр:",mult)
    else:
        print("Вы ввели не трехзначное число")
except ValueError:
    print("Вы ввели не числа, а символы")


