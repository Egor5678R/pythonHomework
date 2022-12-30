#Задайте последовательность чисел. 
#Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

random.seed()
N=int(input( "Введите длину массива: "))
num=int(input( "Введите диапазон чисел: "))
list = []

for i in range(N):
    list.append(random.randint(0, num))
    
list1 = []
for i in list:
    if list.count(i) == 1:
       list1.append(i) 

UniqueList = []
unique = set(list)
for i in unique:
    UniqueList.append(i)
print(f"Массив: {list} -> Уникальные числа массива: {UniqueList}") 
