# -*- coding: utf-8 -*-
"""
Напишите программу для расчета индекса массы тела (body mass index – 
BMI) человека. Пользователь должен ввести свой рост и вес, после чего вы 
используете одну из приведенных ниже формул для определения индекса.
BMI = вес/рост**2 
"""
weight = int(input('Введите вес: '))
height = int(input('Введите рост: '))

#Ваш код

while weight<=0:
    weight = int(input('Вес не может быть меньше или равен нулю, введите корректные данные'))
    while height<=0:
        height = int(input('Рост не может быть меньше или равен нулю, введите корректные данные'))
        
print("Индекс массы тела равен: ", height/weight**2)

