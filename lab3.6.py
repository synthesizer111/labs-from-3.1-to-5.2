dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11,
'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
'x': 24, 'y': 25, 'z': 26, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22,
'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

def swap_elem(array, index):
    array[index], array[index + 1] = array[index + 1], array[index]
    return array

def sum_past_elements(number, first_list, second_list):
    if number == 0:
        return True
    number -= 1
    if first_list[number] == second_list[number]:
        if sum_past_elements(number, first_list, second_list):
            return True
    else:
        return False

def compare_value(word_index, symbol_index, array):
    if dictionary[array[word_index][symbol_index]] > dictionary[array[word_index + 1][symbol_index]]:
        return True
    else:
        return False

start_string = input("Введите строку ")

list_for_check = start_string.split()

for _ in list_for_check:
    for word_index in range(len(list_for_check) - 1):
        length_word = len(list_for_check[word_index])
        if len(list_for_check[word_index]) != len(list_for_check[word_index + 1]):
            length_word = min(len(list_for_check[word_index]), len(list_for_check[word_index + 1]))
        for symbol_index in range(length_word):
            if symbol_index == 0 and compare_value(word_index, symbol_index, list_for_check):
                list_for_check = swap_elem(list_for_check, word_index)
            elif symbol_index != 0 and compare_value(word_index, symbol_index, list_for_check) and \
                    sum_past_elements(symbol_index, list_for_check[word_index], list_for_check[word_index + 1]):
                list_for_check = swap_elem(list_for_check, word_index)
for word in list_for_check:
    print(word, end=' ')
