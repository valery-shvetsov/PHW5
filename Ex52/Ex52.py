# 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

def game_with_man(sweet_def,limit_drf):
    '''
    Игра с человеком
    Аргументы 
    sweet_def-целое число количество конфет
    limit_drf-целое число лимит изъятия конфет за 1 ход
    Результат - строка имя победителя 
    '''
    sweet_1=0
    sweet_2=0
    sweet_result=0
    while sweet_result<=sweet_def:
        sweet_1=Input_int('Сколько конфет забирает Игрок 1? ')
        if sweet_1>limit_drf:
            print(f'Вы не можете взять более {limit_drf} конфет')
            winner_def='Начните игру заново'
            break
        sweet_result=sweet_result+sweet_1
        print(f'Игрок 1 забрал {sweet_1} осталось {sweet_def-sweet_result}')
        if sweet_result>=sweet_def:
            winner_def='Игрок 1'
            break
        else:
            sweet_2=Input_int('Сколько конфет забирает Игрок 2? ')
            if sweet_2>limit_drf:
                print(f'Вы не можете взять более {limit_drf} конфет')
                winner_def='Начните игру заново'
                break
        sweet_result=sweet_result+sweet_2
        print(f'Игрок 2 забрал {sweet_2} осталось {sweet_def-sweet_result}')
        if sweet_result>=sweet_def:
            winner_def='Игрок 2'
            break
    return winner_def
    

def game_with_intern(sweet_def,limit_drf):
    '''
    Игра со стажером
    Аргументы 
    sweet_def-целое число количество конфет
    limit_drf-целое число лимит изъятия конфет за 1 ход
    Результат - строка имя победителя 
    '''
    sweet_1=0
    sweet_2=0
    sweet_result=0
    while sweet_result<=sweet_def:
        sweet_1=Input_int('Сколько конфет забираете Вы? ')
        if sweet_1>limit_drf:
            print(f'Вы не можете взять более {limit_drf} конфет')
            winner_def='Начните игру заново'
            break
        sweet_result=sweet_result+sweet_1
        print(f'Вы забрали {sweet_1} осталось {sweet_def-sweet_result}')
        if sweet_result>=sweet_def:
            winner_def='Игрок'
            break
        else:
            sweet_2=random.randint(1,limit_drf)            
        sweet_result=sweet_result+sweet_2
        print(f'Cтажер забрал {sweet_2} осталось {sweet_def-sweet_result}')
        if sweet_result>=sweet_def:
            winner_def='Стажер'
            break
    return winner_def


def game_with_master(sweet_def,limit_drf):
    '''
    Игра с мастером
    Аргументы 
    sweet_def-целое число количество конфет
    limit_drf-целое число лимит изъятия конфет за 1 ход
    Результат - строка имя победителя 
    '''
    sweet_1=0
    sweet_2=0
    sweet_result=0
    while sweet_result<=sweet_def:
        sweet_1=Input_int('Сколько конфет забираете Вы? ')
        if sweet_1>limit_drf:
            print(f'Вы не можете взять более {limit_drf} конфет')
            winner_def='Начните игру заново'
            break
        sweet_result=sweet_result+sweet_1
        print(f'Вы забрали {sweet_1} осталось {sweet_def-sweet_result}')
        if sweet_result>=sweet_def:
            winner_def='Игрок'
            break
        remains_sweet=sweet_def-sweet_result
        sweet_2=remains_sweet-(remains_sweet//(limit_drf+1)*(limit_drf+1))
        if sweet_2==0:
             sweet_2=1
        sweet_result=sweet_result+sweet_2
        remains_sweet=sweet_def-sweet_result
        print(f'Мастер забрал {sweet_2} осталось {remains_sweet}')
        if sweet_result>=sweet_def:
            winner_def='Мастер'
            break
    return winner_def

def Input_int(input_string):
    '''
    Ввод числа с пояснением
    '''
    while True:
        try:
            num=int(input(input_string))
            return num
        except ValueError:
            print('Введено не число. Давайте попробуем еще раз')

print()
sweet=Input_int('Введите количество конфет : ')
print('Введите максимальное количество конфет,')
limit=Input_int('которое можно удалить за 1 ход : ')

print('С кем вы хотите сыграть? ')
print('1-другой игрок')
print('2-бот-стажер')
print('3-бот-мастер')
opponent=input('Выберите вашего противника : ')
if opponent=='1':
    winner=game_with_man(sweet,limit)
if opponent=='2':
    winner=game_with_intern(sweet,limit)
if opponent=='3':
        winner=game_with_master(sweet,limit)
print('Победил ', winner)
