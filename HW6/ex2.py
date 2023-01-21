'''from random import randint

summa=0
N=int(input("Введите длину списка: "))
list=[0]*N

for i in range(N):
    list[i]=randint(1,10)
for i in range(1,len(list),2):
    summa+=list[i]
    
print(f"{list} -> сумма нечётных элементов: {summa}") '''

import randomNumbers as lg

list = lg.randomNumbers()
summa = sum(list[item] for item in range(1, len(list), 2))
nums = str([list[item] for item in range(1, len(list), 2)]).strip('[]')
print(f"{list} -> сумма нечётных элементов: {summa}")
