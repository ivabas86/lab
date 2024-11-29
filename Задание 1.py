import random
import time
from itertools import count

# map_ = [i for i in range(1, 10)]

VICTORY = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (2, 5, 8),
    (1, 4, 7),
    (0, 4, 8),
    (2, 4, 6)
)
VICTORY_2 = (
    (0, 1, 2, 3),
    (4, 5, 6, 7),
    (8, 9, 10, 11),
    (12,13,14,15),
    (0, 4, 8, 12),
    (1, 5, 9, 13),
    (2, 6, 10, 14),
    (3, 7, 11, 15),
    (12, 9, 6, 13),
    (0, 5, 10, 15)

)
# gen = count(1)
# map_2 = [[next(gen) for _ in range(3)] for _ in range(3)]

# Комбинации выигрышные и нахождение там двух нулей и свободной клетки
# Комбинации проигрышные, нахождение двух X и свободной клетки

f = (int(input('Введите размеры поля (9 или 16 цифр):')))
b = f + 1
map_ = [i for i in range(1, b)]

def print_map():

    if b == 10:
        for i in range(3):
            print(f'| {map_[i * 3]} | {map_[i * 3 + 1]} | {map_[i * 3 + 2]} |')
    if b == 17:
        for i in range(4):
            print(f'|{map_[i * 4]} |{map_[i * 4 + 1]} |{map_[i * 4 + 2]} | {map_[i * 4 + 3]}|')

# def print_map():
#     for i in range(3):
#         print(f'| {map_[i * 3]} | {map_[i * 3 + 1]} | {map_[i * 3 + 2]} |')


# def print_map_2():
#     for el in map_2:
#         print(*el)

def check_number(s):
    try:
        number = int(s)
        if number in map_:
            return number
        else:
            print('Неправильная позиция или место занято!')
    except TypeError:
        print('Вы ввели не число')
    return -1

def proverka_ai (so,sx):
    step = ''
    if b == 10:
        for line in VICTORY:
            O = 0
            X = 0
            for i in range(0, 3):
                if map_[line[i]] == '0':
                    O += 1
                if map_[line[i]] == 'X':
                    X += 1

            if O == so and X == sx:
                for a in range(0, 3):
                    if map_[line[a]] != '0' and map_[line[a]] != 'X':
                        step = map_[line[a]]
                for a in range(0, 3):
                    if map_[line[a]] != '0' and map_[line[a]] != 'X':
                        step = map_[line[a]]
    if b == 17:
        for line in VICTORY_2:
            O = 0
            X = 0
            for i in range(0, 4):
                if map_[line[i]] == '0':
                    O += 1
                if map_[line[i]] == 'X':
                    X += 1

            if O == so and X == sx:
                for a in range(0, 4):
                    if map_[line[a]] != '0' and map_[line[a]] != 'X':
                        step = map_[line[a]]
                for a in range(0, 4):
                    if map_[line[a]] != '0' and map_[line[a]] != 'X':
                        step = map_[line[a]]
    return step

def step_in_map(n, symb):
    ind = map_.index(n)
    map_[ind] = symb

def ai_step():
    data = ''
    if data == '':
        data = proverka_ai(0,2)
    if data == '':
        data = proverka_ai(2,0)
    if data == '':
        data = proverka_ai(1,0)
    if data == '':
        data = proverka_ai(0,1)
    if data == '':
        data = proverka_ai(0,3)
    if data == '':
        data = proverka_ai(3,0)
    return data

    # for el in map_:
    #     if el != 'X' and el != '0':
    #         data = [el]

def get_result():
    s = ''
    if b== 10:
        for line in VICTORY:
            if map_[line[0]] == 'X' and map_[line[1]] == 'X' and map_[line[2]] == 'X':
                s = 'X'
            elif map_[line[0]] == '0' and map_[line[1]] == '0' and map_[line[2]] == '0':
                s = '0'
    if b == 17:
        for line in VICTORY_2:
            if map_[line[0]] == 'X' and map_[line[1]] == 'X' and map_[line[2]] == 'X' and map_[line[3]] == 'X':
                s = 'X'
            elif map_[line[0]] == '0' and map_[line[1]] == '0' and map_[line[2]] == '0' and map_[line[3]] == '0':
                s = '0'
    return s

def game():
    '''
    1. Реализовать выбор с кем играть, чел-комп или чел-чел. Упростить(рефактор) реализацию функции гейм
    2. Сделать умный искусственный интеллект

    :return:
    '''
    name = input('Введи свое имя: ')
    is_human = True
    count_ = 0
    while True:
        count_ += 1
        print_map()
        if is_human:
            s = input(f'{name}, введи номер клетки: ')
            number = check_number(s)
            if number == -1:
                continue
            step_in_map(number, 'X')
            is_human = False
        else:
            print('Ход компьютера!')
            time.sleep(1)
            number = ai_step()
            step_in_map(number, '0')
            is_human = True
        win = get_result()
        if win == 'X':
            print(f'{name} победил!')
            break
        elif win == '0':
            print('Компьютер победил!')
            break
        if b == 10 and count_ == 9:
            print('Ничья!')
            break
        elif b == 17 and count_ == 16:
            print('Ничья!')
            break

game()
