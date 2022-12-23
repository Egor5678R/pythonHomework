#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#Пример:

#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]
from random import randint

N=int(input("Введите длину списка: "))
list=[0]*N
list1=[]

for i in range(N):
    list[i]=randint(1,9)

for i in range(len(list)):
    while i < len(list)/2 and N>len(list)/2:
        N=N - 1
        a=list[i]*list[N]
        list1.append(a)
        i+=1


print(f"{list} -> {list1}")

    