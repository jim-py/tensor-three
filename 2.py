x, y = 0, 0
print('''---Инструкция---
Команда состоит из двух слов:
Первое слово одна из четырёх букв - wasd
(w - вверх, a - влево, s - вниз, d - вправо)
Второе слово - длина шага числом.
Пример - "w 15"
Для выхода команда - exit
''')
while True:
    step = input("Введите команду: ").split()
    if step[1].isdigit():
        if step[0] == 'w':
            y += int(step[1])
        elif step[0] == 'a':
            x -= int(step[1])
        elif step[0] == 's':
            y -= int(step[1])
        elif step[0] == 'd':
            x += int(step[1])
        elif step[0] == 'exit':
            break
        else:
            print("Команда неверна")
    else:
        print("Команда неверна")
    print(f'[{x}, {y}]')
