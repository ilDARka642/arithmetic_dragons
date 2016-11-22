# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def generate_random_enemy_dragon():
    RandomEnemyType = choice(dragon_types)
    enemy = RandomEnemyType()
    return enemy

def generate_random_enemy_troll():
    RandomEnemyType = choice(troll_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy_dragon() for i in range(enemy_number)]
    return enemy_list

def generate_troll_list(enemy_number):
    enemy_list = [generate_random_enemy_troll() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        answer=int(answer)
        self.__answer = answer

    def check_answer(self, answer):
        answer=int(answer)
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 100
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest

class RedDragon(Dragon):
    def __init__(self):
        self._health=200
        self._attack=100
        self._color='красный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest

class BlackDragon(Dragon):
    def __init__(self):
        self._health=200
        self._attack=100
        self._color='черный'
    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest





class Troll(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer

    def check_prostota(self,n):
        for i in range(2,n//2):
            if (n%i)==0:
                return 'No'
        return 'Yes'

    def multiply(self,n):
        s=''
        i=2
        while n>1:
            if n%i==0:
                s=s+str(i)+', '
                while n%i==0:
                    n=n//i
            i+=1
        s=s[:len(s)-2]
        return s



class BlackTroll(Troll):
    def __init__(self):
        self._health=200
        self._attack=1
        self._color='Фиг угадаешь'
    def question(self):
        self.__quest = 'Угадай число от 1 до 5'
        self.set_answer(str(randint(1,5)))
        return self.__quest

class GreenTroll(Troll):
    def __init__(self):
        self._health=200
        self._attack=100
        self._color='Средний'
    def question(self):
        x = randint(1,100)
        self.__quest = 'число '+str(x)+' простое?'
        self.set_answer(self.check_prostota(x))
        return self.__quest

class RedTroll(Troll):

    def __init__(self):
        self._health=200
        self._attack=100
        self._color='Сложный'
    def question(self):
        x = randint(2,100)
        self.__quest = 'Напиши все простые сомножители числа ' + str(x) + ' через запятую в порядке возрастания'
        self.set_answer(self.multiply(x))
        return self.__quest

dragon_types = [GreenDragon, RedDragon, BlackDragon]
troll_types = [GreenTroll, BlackTroll,RedTroll]

#FIXME здесь также должны быть описаны классы RedDragon и BlackDragon
# красный дракон учит вычитанию, а чёрный -- умножению.