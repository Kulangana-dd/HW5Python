# 5) Создать (программно) текстовый файл, 
# записать в него программно набор чисел, разделенных пробелами. 
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


import random

with open('text5.txt', 'w', encoding='utf-8') as file_obj:
    numbers = 0
    sum_numbers = 0
    while numbers <= 10:
        numbers += 1
        random_number = random.randint(1, 5)
        sum_numbers += random_number
        print(f'{random_number} ', end='', file=file_obj)

print(f'Сумма чисел: {sum_numbers}')