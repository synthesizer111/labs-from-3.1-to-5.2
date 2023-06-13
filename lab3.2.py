def bracket_check():
    message = input('Введите скобочную последовательность: ')
    count = 0
    for i in message:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
    if count != 0 or message[0] == ')':
        print('Нет')
    else:
        print('Является')
bracket_check()