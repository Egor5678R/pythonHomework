#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

k=abs(int(input()))
list=[]
list1=[]

def Fibonachi(n):
    if n<-2:
        return Fibonachi(n+2)-Fibonachi(n+1)
    elif n==-2:
        return -1
    elif n==-1:
        return 1
    elif n==0:
        return 0
    elif n in (1,2):
        return 1
    return Fibonachi(n-1)+Fibonachi(n-2)

def Negafibonachi(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        a, b = 1, -1
        for i in range(2, n):
            a,b=b,a-b
        return b


for i in range(-k, k+1):
    list.append(Fibonachi(i))

for i in range(1,k+1):
    list1.insert(0,Negafibonachi(i))
               

print(f"для k={k} список будет выглядеть так: {list} (Фибоначчи)")
print(f"для k={k} список будет выглядеть так: {list1} (Негафибоначчи)")
