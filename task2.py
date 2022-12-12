# 2) Создать текстовый файл (не программно), 
# сохранить в нем несколько строк, 
# выполнить подсчет количества строк, количества слов в каждой строке.
   

with open('text2.txt', encoding='utf-8') as f_obj:
    for ind, line in enumerate(f_obj.readlines(), 1):
        print(f'{ind} строка - количество слов: {len(line.split())}')
    print(f'Количество строк в файле: {ind}')