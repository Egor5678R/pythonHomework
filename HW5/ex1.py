#Напишите программу, удаляющую из текста все слова, содержащие ""абв.

text = str(input("Введите текст: "))

def delWords(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = delWords(text)
print(text)