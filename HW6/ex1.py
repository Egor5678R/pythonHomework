'''number=input()

def summa(number):                            
    if float(number) < 0:                            
        x=float(x)*(-1)
    num=0

    for i in str(number):
        if i !='.':
            num+=int(i)
    return num

   
print(f'{number} -> {summa(number)}')'''

number = input()
summa = sum(map(int, number.replace('.', '')))
print (summa)