#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в отдельном списке( пример n=4, lst1=[4,-2,1,3] - списко на основе n, а позиции элементов lst2=[3,1].

from random import randint
from random import seed

seed()
N=int(input('введите число '))
lst1=[]
lst2=[]

for i in (0,1):
    lst2.append(randint(0, N))
    
for i in range(N):
    lst1.append(randint(-N, N))

print(f"Для n={N}")    
print(f"lst1={lst1}")
print(f"lst2={lst2}")
print(f"Проиведение эллеметов: {lst1[lst2[0]] * lst1[lst2[1]]}")
