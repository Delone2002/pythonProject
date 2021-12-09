#!/usr/bin/python3

def fibonacci(n):
    '''Число Фибоначчи
    
    n - n-ое число Фибоначчи. Функция принимает n и возвращает данное число.
    
    '''

    if(n == 0):
        return 0
    if(n == 1):
        return 1
    return fibonacci(n - 1)+fibonacci(n - 2)


try:
    n = int(input("Введите номер числа Фибоначчи: "))
except ValueError:
    print("Введено некорректное значение! Вводите целые числа")
if(n >= 0):
    try:
        print(f"Число Фибоначчи = {fibonacci(n)}")
    except RecursionError:
        print("Слишком большое число. Оно сокрыто от вас")
else:
    print("Введено отрицательное число")