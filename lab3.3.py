def months(s, t):
    if t == 'ru':
        if s == 1:
            print("Январь")
        elif s == 2:
            print("Февраль")
        elif s == 3:
            print("Март")
        elif s == 4:
            print("Апрель")
        elif s == 5:
            print("Май")
        elif s == 6:
            print("Июнь")
        elif s == 7:
            print("Июль")
        elif s == 8:
            print("Август")
        elif s == 9:
            print("Сентябрь")
        elif s == 10:
            print("Октябрь")
        elif s == 11:
            print("Ноябрь")
        elif s == 12:
            print("Декабрь")
    elif t == 'en':
        if s == 1:
            print("January")
        elif s == 2:
            print("February")
        elif s == 3:
            print("March")
        elif s == 4:
            print("April")
        elif s == 5:
            print("May")
        elif s == 6:
            print("June")
        elif s == 7:
            print("July")
        elif s == 8:
            print("August")
        elif s == 9:
            print("September")
        elif s == 10:
            print("October")
        elif s == 11:
            print("November")
        elif s == 12:
            print("December")
    else:
        print("Неправильный номер")
month = int(input("Введите номер месяца: "))
lang = input("Введите язык: ")
months(month, lang)
