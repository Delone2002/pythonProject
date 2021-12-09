#!/usr/bin/python3

import os


print(f'Имя ОС: {os.name}')
print(f'Имя пользователя: {os.getlogin()}')
print(f'Список файлов и каталогов в текущей папке: {os.listdir()}')

