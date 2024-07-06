'''
Написати функцію, яка буде повертати одне слово за раз
'''
from typing import Generator

def yield_word() -> Generator[str, None, None]:
    word_list = ['Hello', 'World', 'Orange', 'Apple']
    for word in word_list:
        yield word

my_generator = yield_word()
print(next(my_generator))
word = next(my_generator)


if word == 'World':
    print('Equals')

print(next(my_generator))
print(next(my_generator))