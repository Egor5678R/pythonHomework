'''from random import randint

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
        i+=1'''

from math import ceil
import randomNumbers as lg

list1 = lg.randomNumbers()
print(f"{list1} -> {list([a * b for a, b in zip(list1[0 : ceil(len(list1) / 2)],list1[:: - 1])])}")
