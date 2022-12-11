# 1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.

# Пример:
# Пугать ты галок пугай => заданная строка "пугай" => Пугать ты галок

def removing_words(text_def:str, word_def:str) ->str:
    '''
    Из текста text_def вырезает слова, содержащие текст word_def
    возвращает строку result_def 
    '''
    result_def=[]
    for i in text_def.split():
        if word_def not in i:
            result_def.append(i)
    result_def=' '.join(result_def)
    return result_def


print()
text=input('Введите исходный текст : ')
#text='пугать ты галок пугай'
word=input('Введите текст, слова с которым надо вырезать из исходного текста : ')
result=removing_words(text,word)
print('Вариант с def : ',result)
list_result=[i for i in text.split() if word not in i]
print('Вариант с list comprehension : ',' '.join(list_result))