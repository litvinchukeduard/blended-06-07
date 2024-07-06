import sys
from pathlib import Path
from colorama import Fore, Back, Style, init

init(autoreset=True)

def print_directory(folder_path: str, tab_size: int = 0) -> None: # '/Documents/Repositories'
    path = Path(folder_path)
    tab_str = tab_size * '\t'
    for element in path.iterdir():
        element_name = element.name
        if element.is_dir():
            print(Fore.GREEN + f'{tab_str}📦 {element_name}')
            print_directory(element.as_posix(), tab_size + 1)
        else:
            print(Fore.BLUE + f'{tab_str}📜 {element_name}')


# [x for x in p.iterdir() if x.is_dir()]
# . - поточна папка
# .. - папка на рівень вище




if len(sys.argv) > 1:
    file_path = sys.argv[1]
    print_directory(file_path)

# print(type('hello !123 ' * 3))
# my_str = 'hello !123 ' * 3
# print(my_str)