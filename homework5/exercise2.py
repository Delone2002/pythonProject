#!/usr/bin/python3

def sum(list=['']):
    '''Суммирование
    
    Функция суммируется все числа, переданные ей.

    '''

    print(list)
    sum = 0
    if(list == ['']):
        return sum
    for i in range(len(list)) :
        sum += list[i]
    return sum

try:
    numbers = input("Введите числа через пробел: ")
    numbers = numbers.split(" ")
    print(numbers)

    if(len(numbers) != 0 and numbers[0] != ''):
        for i in range(len(numbers)):
            numbers[i] = float(numbers[i])
    print(f"Сумма = {sum(numbers)}")
except ValueError:
    print("Введено некорректное значение!")
