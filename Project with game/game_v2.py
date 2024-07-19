"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попытокcore_v3(number: int = 1) -> int:
    """       
    
    count = 0 #счетчик попыток найти число
    predict = np.random.randint(1,101)
    first = 1 #начальная граница
    last = 101 #верхняя граница
    predict_number = (first+last)//2 #задан вариант, от которого начинать предсказание
    #вводим цикл для реализации предсказания
    while number!= predict_number:
        count+=1
        
        if predict_number > number:
            last = predict_number #задаем новую вурхнюю границу, если условие выполняется
        elif predict_number < number: 
            first = predict_number #задаем новую нижнюю границу, если выполняется условие №2
        predict_number =(first+last)//2 #новое предсказание в рамках новых границ 
    return count


print('Run benchmarking for game_core_v3: ', end='')
game_core_v3(25)
