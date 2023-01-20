'''Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. 
Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом"" '''

from random import randint


mode = int(input("Выберите режим: \n 1.Человек vs Человек \n 2.Человек vs Лёгкий бот \n 3.Человек vs Сложный бот \n"))

def quantityEntry(name):
    x = int(
        input(f"{name}, введите количество конфет от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, такого колличества не существует: "))
    return x

def hardBot(value):
    count = randint(1, 29)
    while value-count <= 28 and value > 29:
        count = randint(1, 29)
    return count

def printResult(name, count, counter, value):
    print(
        f"{name} взял {count}, теперь у него {counter}. \nОсталось на столе {value} конфет.")


player1 = input("Введите имя первого игрока: ")
if mode == 1:
    player2 = input("Введите имя второго игрока: ")
else:
    player2 = "Bot"
value = int(input("Введите количество конфет на столе: "))
queue = randint(0, 2)  
if queue:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0
counter2 = 0

while value > 28:
    if queue:
        count = quantityEntry(player1)
        counter1 += count
        value -= count
        queue = False
        printResult(player1, count, counter1, value)
    else:
        if mode == 2:
            count = randint(1, 29)
        elif mode == 3:
            count = hardBot(value)
        counter2 += count
        value -= count
        queue = True
        printResult(player2, count, counter2, value)

if queue:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")