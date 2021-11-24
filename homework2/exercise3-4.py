#!/usr/bin/python3

import math
import cmath

a = float(input("Введите коэффициент а: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

if(a==0.0):
    if(b==0.0):
        print("Неверно заданное уравнение!\n")
    else:
        print(f"Ваше уравнение: {b}x+{c}=0\n")
        x = -c/b
        print(f"x = {x}")
else:
    print(f"Ваше уравнение: {a}x^2+{b}x+{c}=0\n")
    D = b*b-4*a*c
    if(D>0):
        x1 = (-b+math.sqrt(D))/(2*a)
        x2 = (-b-math.sqrt(D))/(2*a)
        print(f"x1 = {x1}\nx2 = {x2}")
    if(D==0):
        x = -b/(2*a)
        print(f"x = {x}")
    if(D<0):
        a = complex(a, 0)
        b = complex(b, 0)
        c = complex(c, 0)
        x1 = (-b+cmath.sqrt(D))/(2*a)
        x2 = (-b-cmath.sqrt(D))/(2*a)
        print(f"x1 = {x1}\nx2 = {x2}")