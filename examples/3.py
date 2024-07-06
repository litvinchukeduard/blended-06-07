import re

'''
Написати функцію, яка буде читати файл та рахувати суму чисел у файлі
'''

def sum_of_numbers_in_file(file_path: str) -> int:
    # file = open(file_path, 'r')

    # file.close()
    pattern = r'[0-9]+'
    numbers_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        # for line in file.readlines():
        for line in file:
            numbers_list += re.findall(pattern, line) # a += b <-> a = a + b
        # '7'
    number_sum = 0
    for number in numbers_list:
        number_sum += int(number)
    return number_sum
    

print(sum_of_numbers_in_file('./examples/3.txt'))

