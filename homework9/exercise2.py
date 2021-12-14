#!/usr/bin/python3

import math
import cmath


def equation(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        print("Некорректно введены коэффициенты")
        return

    solutions = dict()

    if(a==0.0):
        if(b==0.0):
            print("Неверно заданное уравнение!\n")
            return
        else:
            print(f"Ваше уравнение: {b}x + {c} = 0\n")
            x = -c/b
            print(f"x = {x}")
            solutions['x1'] = x
            return solutions
    else:
        print(f"Ваше уравнение: {a}x^2 + {b}x + {c} = 0\n")
        D = b*b-4*a*c
        if(D>0):
            x1 = (-b+math.sqrt(D))/(2*a)
            x2 = (-b-math.sqrt(D))/(2*a)
            print(f"x1 = {x1}\nx2 = {x2}")
            solutions['x1'] = x1
            solutions['x2'] = x2
            return solutions
        if(D==0):
            x = -b/(2*a)
            print(f"x = {x}")
            solutions['x1'] = x
            return solutions
        if(D<0):
            a = complex(a, 0)
            b = complex(b, 0)
            c = complex(c, 0)
            x1 = (-b+cmath.sqrt(D))/(2*a)
            x2 = (-b-cmath.sqrt(D))/(2*a)
            print(f"x1 = {x1}\nx2 = {x2}")
            solutions['x1'] = x1
            solutions['x2'] = x2
            return solutions