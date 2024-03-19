import os
import sys
import colorama
from colorama import Fore, Style
from pathlib import Path

def print_directory_contents(path):
    for root, directories, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(Fore.BLUE + '{}{}/'.format(indent, os.path.basename(root)) + Style.RESET_ALL)
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(Fore.GREEN + '{}{}'.format(subindent, f) + Style.RESET_ALL)

if __name__ == '__main__':
    colorama.init()
    if len(sys.argv) != 2:
        print("Використання: python hw03.py <шлях до директорії>")
    else:
        directory_path = sys.argv[1]
        if not os.path.exists(directory_path):
            print("Вказаний шлях не існує.")
        elif not os.path.isdir(directory_path):
            print("Вказаний шлях не є директорією.")
        else:
            print_directory_contents(directory_path)


