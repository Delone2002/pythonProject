#!/usr/bin/python3

support = "P.S. Вводите через пробел направление движения (влево, вправо, вверх, вниз) и число позиций"

currentPosition = [0.0, 0.0]
while(1):
    print(f"Вы находитесь в ({currentPosition[0]};{currentPosition[1]}). Куда вы хотите двигаться?\n")
    print('Для остановки движения напишите "стоп"\n')
    s = input().split(" ")
    if(len(s) > 2):
        print("Введено слишком много параметров!\n" + support)
    elif(len(s) == 1 and s[0] == "стоп"):
        break
    elif(len(s) == 2):
        direction = s[0]
        position = float(s[1])
        if(direction == "вверх"):
            currentPosition[1] += position
        elif(direction == "вниз"):
            currentPosition[1] -= position
        elif(direction == "вправо"):
            currentPosition[0] += position
        elif(direction == "влево"):
            currentPosition[0] -= position
        else:
            print("Направление введено некорректно!\n" + support)
    else:
        print("Введено слишком мало параметров\n" + support)
print(f"Движение окончено. Вы находитесь в ({currentPosition[0]};{currentPosition[1]}).")
    