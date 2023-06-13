def triangle():
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    if a + b > c and b + c > a and a + c > b:
        print('Можно')
    else:
        print('Нельзя')
triangle()