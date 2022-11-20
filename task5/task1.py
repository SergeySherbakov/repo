# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input("Введите текст через пробел:\n")
print(f"Исходный текст: {text}")
text = text.split()
for i in range(len(text)):
    if 'абв' in text[i]:
        if not text[i].isidentifier():
            text[i] = text[i][-1]
        else:
            text[i] = ''
text = ' '.join(text)
print(f"Результат: {text}")
