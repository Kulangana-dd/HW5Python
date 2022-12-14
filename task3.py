# 3) Создать текстовый файл (не программно), 
# построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). 
# Определить, кто из сотрудников имеет оклад менее 20 тыс., 
# вывести фамилии этих сотрудников. 
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('text3.txt', encoding='utf-8') as f_obj:
    print(f'Зарплата меньше 20000:\n')
    salaries = []
    lines = f_obj.readlines()
    for line in lines:
        name, salary = line.split()
        salaries.append(float(salary))
        if float(salary) < 20000:
            print(line, end='')
    print(f'\nСредняя зарплата: {round(sum(salaries) / len(salaries),2)}') 