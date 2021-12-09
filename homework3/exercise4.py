#!/usr/bin/python3

import random


limit = 300
weight = 0
inventory = {}

message = 'Для добавления предметов напишите "добавить' 
+ '(название предмета)".\nДля удаления предмета из инв'
+ 'ентаря напишите "достать (название предмета)"\nВвед'
+                             'ите "стоп", чтобы выйти'

while(1):
    if(len(inventory) == 0):
        weight = 0
        print("Инвентарь пуст\n" + message)
    else:
        print(f"Общий вес = {weight} Инвентарь: {inventory}")

    s = list(input().split(" "))
    if(len(s) != 2):
        if(len(s) == 1 and s[0] == 'стоп'):
            break
        print("Ошибка ввода!\n" + message)
    else:
        if(s[0] == 'добавить'):
            if(weight >= limit):
                print(f"Инвентарь переполнен! Общий вес - {weight} кг")
            else:
                inventory[s[1]]=random.randint(1, 20)
                weight += inventory[s[1]]
                print(f"Добавлен предмет {s[1]} с весом {inventory[s[1]]} кг")
        elif(s[0] == 'достать'):
            if(inventory.get(s[1]) is None):
                print("Такого предмета нет в инвентаре!")
            else:
                if(weight == 0):
                    print("Инвентарь пуст\n" + message)
                else:
                    delweight = inventory.pop(s[1])
                    weight -= delweight
                    print(f"Удален предмет {s[1]} с весом {delweight} кг")
print(f"Общий вес = {weight} Инвентарь: {inventory}\nПока!")
