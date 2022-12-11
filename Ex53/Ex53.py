# 3- Создайте программу для игры в ""Крестики-нолики"". Для определения победы вам может 
# пригодиться функция filter. Проверяйте победу после каждого хода, фильтруя столбцы, строки и 
# диагонали по знаку хода

def playing_field (coordinates:list):
    '''
    Формирование игрового поля
    Аргумент-список с содержанием ячеек поля
    Результат-графическое представление поля
    '''
    print('_____')
    print(f'{coordinates[0]} {coordinates[1]} {coordinates[2]}')
    print(f'{coordinates[3]} {coordinates[4]} {coordinates[5]}')
    print(f'{coordinates[6]} {coordinates[7]} {coordinates[8]}')
    print('_____')

def game(players_list, turns_list):
    '''
    Игровая логика
    Аргументы
    players_list-список Имен игроков
    turns_list-список с содержанием ячеек поля
    Результат- формирование новых списков для playing_field
    и вывод поля после каждого ввода символов X и 0
    '''
    pl=players_list[0]
    for i in range(len(turns_list)-1):
        new_turns=10
        while new_turns>9 or turns_list[new_turns-1] in ('X','0'):
            new_turns=input_int(f'{pl[1]} выберите ячейку для хода ')
            if new_turns>9 or turns_list[new_turns-1] in ('X','0'):
                print('Поставить знак сюда нельзя\n')
        if pl==players_list[0]:
            turns_list[new_turns-1]='X'
            playing_field(turns_list)
            if i>=4:
                check_for_victory (turns_list,players_list[0])
            pl=players_list[1]
        else:
            turns_list[new_turns-1]='0'
            playing_field(turns_list)
            if i>=4:
                check_for_victory (turns_list,players_list[1])
            pl=players_list[0]

def check_for_victory (turns_list,players_list):
    '''
    Проверка на выигрыш
    Аргументы
    players_list-список имен игроков
    turns_list-список с содержанием ячеек поля
    Результат- вывод имени победителя
    '''
    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for each in win_coord:
       if turns_list[each[0]] == turns_list[each[1]] == turns_list[each[2]]:
          return exit (print (f' Победил {players_list [1]}'))
    return False

def input_int(input_string):
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
turn=[1,2,3,4,5,6,7,8,9]
player1='Игрок 1'
player2='Игрок 2'
players=[[1,player1],[2,player2]]
playing_field(turn)
game(players,turn)