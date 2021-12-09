#!/usr/bin/python3

def encodeList(list):
    '''Кодирование списка'''

    for i in range(len(list)):
        list[i] = list[i].encode('utf-8')

def decodeList(list):
    '''Декодирование списка'''

    for i in range(len(list)):
        list[i] = list[i].decode('utf-8')

s = input("Введите строки через пробел\n").split()
if(len(s) == 0):
    print('Вы ничего не ввели')
else:
    encodeList(s)
    print(f'Закодированный список\n{s}')
    decodeList(s)
    print(f'Раскодированный спсиок\n{s}')