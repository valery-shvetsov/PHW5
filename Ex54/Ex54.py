# 4-Создайте два списка — один с названиями языков программирования, другой — с их нумерацией.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера 
# и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая (обязательно используйте tuple unpacking) — которая отфильтрует этот список следующим 
# образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, 
# то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. 
# Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным 
# списком

from typing import List

def list_of_tuples (programming_language=None, numbers=None):
    '''
    Формирование списка кортежей (НАЗВАНИЕ ЯЗЫКА, номер)
    Аргументы:
    programming_language-языки
    numbers-номера
    Пока заданы внутри функции
    Результат tuples-список кортежей
    '''
    if programming_language is None:
        programming_language=['python','pascal','basic', 'c#','c++', 'java']
    if numbers is None:
       numbers=[1,2,3,4,5,6] 
       language=list(map(str.upper,programming_language))
       tuples=list(zip(numbers,language))
       return tuples

def code_values_sum (cort_item: str):
    '''
    Вычисление суммы кодов 
    Аргумент cort_item
    cort_item-строка с названием языка
    Результат sum_values-сумма кодов
    '''
    sum_values=0
    for i in cort_item:
        sum_values+=ord(i)
    return sum_values

def code_values_selection(data:list):
    '''
    Выбор суммы кодов 
    Аргумент data-список кортежей (НАЗВАНИЕ ЯЗЫКА, сумма кодов)
    Результаты:
    data-список выбранных кортежей
    elem_ord_sum-сумма кодов выбранных языков
    '''
    data=[(code_values_sum(data[i][1]),data[i][1]) for i in range(1,len(data)) 
            if not code_values_sum (data[i][1])%data[i][0]]
    elem_ord_sum=0
    for i in data:
        elem_ord_sum+=i[0]
    return data, elem_ord_sum

print()
data_list=list_of_tuples() 
result=code_values_selection(data_list)
print(f'Список {result[0]}\n')
print('Сумма кодов',result[1])
