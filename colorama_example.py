from colorama import Fore, Back, Style, init
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print('some red text')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

init(autoreset=True)

print(Fore.RED + Back.GREEN + "Hello, world")
print("Hello")
