# 1) Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('text1.txt', "w", encoding='utf-8') as f_obj:
    content = []
    while True:
        line = f'{input("Введите любые данные: ")}\n'
        if line == '\n':
            break
        content.append(line)
    f_obj.writelines(content)
