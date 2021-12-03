#!/usr/bin/python3

import re

def pasw(s=""):
    condition = 0

    if(len(s)>=6):
        condition+=1
    if(re.match("\d+", s) is not None):
        condition+=1
        print(2)
    if(re.match("\D+", s) is not None):
        condition+=1
    sLow = s.lower()
    if(sLow.find("password")==-1):
        condition+=1

    if(condition==4):
        return True
    return False

s = input("Введите пароль: ")
if(pasw(s)):
    print("Введен верный пароль!")
else:
    print("Введен некорректный пароль!")