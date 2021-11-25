#!/usr/bin/python3

print("Введите список чисел через пробел")
l = input().split(" ")

if(len(l)==1):
    print(f"Список отсортирован\n{l}")
else:
    for i in range(0, len(l)):
        if(l[i].isdigit()):
            l[i]=int(l[i])
        else:
            l[i]=float(l[i])
            
    for j in range(len(l), 1, -1):
        for i in range(1, j):
            if(l[i]<l[i-1]):
                tmp=l[i]
                l[i]=l[i-1]
                l[i-1]=tmp
    print(f"Список отсортирован\n{l}")

