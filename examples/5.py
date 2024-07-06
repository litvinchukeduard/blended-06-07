import re

def numbers_match():
    with open("File1.py") as file1:
        with open("File2.py") as file2:
            numbers_list1 = []
            numbers_list2 = []
            pattern = r"[0-9]+"
            for line in file1:
                numbers_list1 += re.findall(pattern, line)
            for line in file2:
                numbers_list2 += re.findall(pattern, line)
            for number in numbers_list1:
                if number in numbers_list2:
                    print(number)

numbers_match()