#Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)

from random import randint
from random import seed


seed()
a=int()
r=int(input(" 1.Числа от 0 до 9 \n 2.Числа от 10 до 200 с шагом 10 \n"))
List=[0,1,2,3,4,5,6,7,8,9]
list=[10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]

if r==1:
    for i in range(len(List)):
        a=List[i]
        List.pop(i)
        List.insert(randint(0,9),a)
    print(List)

elif r==2:
    for i in range(len(list)):
        a=list[i]
        list.pop(i)
        list.insert(randint(10,200),a)
    print(list)
