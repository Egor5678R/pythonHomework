from random import randint 

def randomNumbers():
    N = int(input("Введите длину списка: "))
    return [randint(1, 10) for i in range(N)]