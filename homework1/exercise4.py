#!/usr/bin/python3

import math


r = input("Enter the radius: ")

if r.replace('.', '0').isdigit():
    if r.isdigit():
        r=int(r)
        print("Area = "+f"{math.pi * r*r}")
    else:
        r=float(r)
        print("Area = "+f"{math.pi * r*r}")
else:
    print("The entered characters arn't numbers!")
