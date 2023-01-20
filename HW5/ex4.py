#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('file4.txt', 'r') as data:
    text = data.read()

def compressionRle(ss):
    strCompression = ''
    prevChar = ''
    count = 1
    for char in ss:
        if char != prevChar:
            if prevChar:
                strCompression += str(count) + prevChar
            count = 1
            prevChar = char
        else:
            count += 1
    return strCompression

            
strCompression = compressionRle(text)
print(strCompression)

with open('file5.txt', 'r') as data:
    text2 = data.read()

def recoveryRle(ss:str):
    count = ''
    strRecovery = ''
    for char in ss:
        if char.isdigit():
            count += char 
        else:
            strRecovery += char * int(count)
            count = ''
    return strRecovery

strRecovery = recoveryRle(text2)
print(strRecovery)