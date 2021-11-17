#!/usr/bin/python3

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

a = input("Enter the first number: ");
b = input("Enter the second number: ");
if not (a.replace('.', '0').isdigit() and b.replace('.', '0').isdigit()):
    print("The entered characters arn't numbers!")
else:
    if b!='0':
        if isint(a) and isint(b):
            a = int(a)
            b = int(b)
            print(f"Addition = {a+b}\nSubtraction = {a-b}\nMultiplication = {a*b}\nDivision = {a/b}\nExponentiation = {a**b}\nModulo = {a%b}\nInteger division = {a//b}")
        else:
            a = float(a)
            b = float(b)
            print(f"Addition = {a+b}\nSubtraction = {a-b}\nMultiplication = {a*b}\nDivision = {a/b}\nExponentiation = {a**b}\nModulo = {a%b}\nInteger division = {a//b}")
    else:
        print("Division by zero!")