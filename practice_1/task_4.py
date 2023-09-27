# -*- coding: utf-8 -*-
"""
Разработайте программу, запрашивающую у  пользователя целое четырехзначное число и подсчитывающую сумму составляющих его цифр. Например, если пользователь введет число 3141,
 программа должна вывести 
следующий результат: 3 + 1 + 4 + 1 = 9

@author: Savant
"""

four_digit_number = input('Введите четырехзначное число: ')
acc = 0 #переменная для суммы цифр
while len(four_digit_number)!= 4:
    print(four_digit_number)
    four_digit_number = input('Неверный ввод, введите повторно: ')
    
for item in four_digit_number:
    acc += int(item)
    
print(acc)
    


