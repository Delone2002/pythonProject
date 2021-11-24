#!/usr/bin/python3

print("Вы находитесь в (0.0;0.0). Куда вы хотите двигаться?\n")
support = "P.S. Вводите через пробел направление движения (влево, вправо, вверх, вниз) и число позиций"
s = input().split(" ")
if(len(s)>2):
    print("Введено слишком много параметров!\n"+support)
elif(len(s)<2):
    print("Введено слишком мало параметров\n"+support)
else:
    direction = s[0]
    position = float(s[1])
    if(direction=="вверх"):
        print(f"Новая позиция - (0.0;{position})")
    elif(direction=="вниз"):
        print(f"Новая позиция - (0.0;{-position})")
    elif(direction=="вправо"):
        print(f"Новая позиция - ({position};0.0)")
    elif(direction=="влево"):
        print(f"Новая позиция - ({-position};0.0)")
    else:
        print("Направление введено некорректно!\n"+support)