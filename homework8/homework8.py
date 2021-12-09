#!/usr/bin/python3


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        pass

    def eat(self, a):
        '''Скушает, все, что угодно. Расстроится, если ничего не передано в функцию.'''

        if(a is None):
            print("Ррррррр")
            return '\a'
        else:
            return 0


class Mammal(Animal):
    def __init__(self, name, age, sex):
        super().__init__(name, age)
        self.sex = sex

    def giveMilk(self):
        '''Дать молоко'''

        if(self.age > 5 and self.sex == 'W'):
            return 'milk'
        else:
            return 'What are you doing?'


class Human(Mammal):
    def __init__(self, name, age, sex, money):
        super().__init__(name, age, sex)
        self.money = money

    def marry(self, bride):
        '''Пожениться
        
        Функция принимает объект типа Human и возвращает результат помолвки.

        '''

        if(self.sex == 'M' and bride.sex == 'W'):
            print(f'Объявляем {self.name} и {bride.name} мужем и женой!')
        else:
            print(f'Жениться может только мужчина и только на женщине!')


class Student(Human):
    def __init__(self, name, age, sex, money, homework):
        super().__init__(name, age, sex, money)
        self.homework = homework
    
    def __eq__(self, other):
        return (self.homework == other.homework)

    def __lt__(self, other):
        return (self.homework < other.homework)

    def __gt__(self, other):
        return (self.homework > other.homework)

    def __ne__(self, other):
        return (self.homework != other.homework)

    def __le__(self, other):
        return (self.homework <= other.homework)

    def __ge__(self, other):
        return (self.homework >= other.homework)


s1 = Student("Alexander", 19, 'M', 0, 18)
s2 = Student("Andrey", 19, 'W', 200, 1)

print(s1.eat('Бризолька'))
s2.sleep()
print(s1.giveMilk())
s2.sleep()
try:
    print(s1.marry(s2))
    s1.marry(2)
except AttributeError:
    print('Нельзя жениться на нечеловеке!')
print(s1 < s2)
