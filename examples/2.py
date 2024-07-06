'''
Потрібно написати функцію, яка буде знаходити усі зайві відступи у тексті та прибирати їх
'''

'  Hello world,    your captian speaking!   '

import re


def remove_spaces(string):
    pattern = r'\s+'
    result = re.sub(pattern, ' ', string).strip()
    return result


some_words = ('     Потрібно     написати  функцію, яка буде знаходити '
              'усі      зайві відступи у       тексті та прибирати їх    ')
print(remove_spaces(some_words))