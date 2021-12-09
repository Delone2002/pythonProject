#!/usr/bin/python3

import re


try:
    
    with open('Input.txt') as file:
        text = file.read()
        text = text.split()

        if(len(text) < 3):
            print('Данных недостаточно')
        elif(len(text) > 3):
            print('Слишком много данных!')
        else:
            alcohol = [int(text[0]) // 2, int(text[1]) // 6, int(text[2])]
            if(min(alcohol) >= 0):
                molecule = str(min(alcohol)) + '\n'
                file2 = open('Output.txt', 'w')
                file2.write(molecule)
                file2.close()
            else:
                print('Отрицательные числа недопустимы!')

except ValueError:
    print('Вы ввели не целые числа!')
except FileNotFoundError:
    print("Не удалось найти файл!")
