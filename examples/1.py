import re
'''
Написати функцію, яка буде знаходити усі голосні літери в тексті та обʼєднувати їх у один рядок
'''
def find_all_vowels(text: str) -> str:
    vowels = 'aeiou'
    pattern = fr'[{vowels}]' # [aeiou]
    # ''.join()
    return ', '.join(re.findall(pattern, text, re.IGNORECASE))

def find_all_vowels_loop(text: str) -> str:
    vowel_list = list()
    for symbol in text:
        # if symbol == 'a' or symbol == 'e'
        # match symbol:
        #     case 'a':
        if symbol.lower() in 'aeiou':
            vowel_list.append(symbol)
    return ', '.join(vowel_list)



print(find_all_vowels("Hello, worldEEEE!"))
print(find_all_vowels_loop("Hello, worldEEEE!"))
# print(', '.join(['1', '2', '3']))
