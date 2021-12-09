#!/usr/bin/python3

import os


def xor(text, key):
    '''XOR кодирование и декодирование
    
    Функция принимает текст, к которому будет применен
    алгоритм XOR, и ключ.

    '''

    s=''
    for i in range(len(text)):
        if(isinstance(text[i], str)):
            text[i] = ord(text[i]) ^ ord(key[i % len(key)])
            ss = str(text[i])
            s += ss
        else:
            text[i] = chr(text[i] ^ ord(key[i % len(key)]))
            s += text[i]
    return s

key = list(input("Введите ключ: "))

try:

    with open('xor.txt') as file:
        text = list(file.read())
        with open('result.txt', 'a') as file2:
            os.system(r' >result.txt')
            file2.write('Закодированное сообщение: ' + xor(text, key))
            file2.write('\nРаскодированное сообщение: ' + xor(text, key) + '\n')
            
except FileNotFoundError:
    print("Файл не найден")
except ZeroDivisionError:
    print("Вы не ввели ключа!")
