#!/usr/bin/env python3

import os
import sys


player = 'X'


def init_table(size):
    table = []
    row = []
    for i in range(size):
        row.append(' ')
    for j in range(size):
        table.append(row.copy())

    return table


def display(size):
    row_delim = '+'
    for i in range(size):
        row_delim += '-+'
    print(row_delim)
    for row in table:
        print('|', end='')
        for field in row:
            print(field, end='|')
            sys.stdout.flush()
        print()
        print(row_delim)


def validate(size, x, y):
    if x < 0 or x > size - 1:
        print('Error: invalid row number')
        return False

    if y < 0 or y > size - 1:
        print('Error: invalid column number')
        return False

    return True


def flip_player():
    global player
    if player == 'X':
        player = 'O'
    else:
        player = 'X'


def turn(table, x, y):
    if not validate(len(table), x, y):
        return False

    if table[x][y] != ' ':
        print('Error: field is not empty')
        return False

    global player
    table[x][y] = player

    return True


def check_hv(table, player):
    size = len(table)
    for i in range(size):
        flag = True
        for j in range(size):
            flag &= table[i][j] == player
            if not flag:
                break
        if flag:
            return True

        flag = True
        for j in range(size):
            flag &= table[j][i] == player
            if not flag:
                break
        if flag:
            return True

    return False


def check_d(table, player):
    size = len(table)
    flag = True
    for i in range(size):
        flag &= table[i][i] == player
        if not flag:
            break
    if flag:
        return True

    flag = True
    for i in range(size):
        flag &= table[i][size - 1 - i] == player
        if not flag:
            break
    if flag:
        return True

    return False


def check(table, player, turn_count):
    if check_hv(table, player) or check_d(table, player):
        return player

    if turn_count == len(table)**2:
        return 'XO'

    return 'cont'


if __name__ == '__main__':
    size = int(input('size of table = '))
    table = init_table(size)
    display(size)

    turn_count = 0
    state = 'cont'
    while state == 'cont':
        print(f'Player {player}:')
        x = int(input('row = '))
        y = int(input('col = '))
        if turn(table, x - 1, y - 1):
            turn_count += 1
            state = check(table, player, turn_count)
            flip_player()
        display(size)

    if state == 'XO':
        print('Nobody win :(')
    else:
        print(f'Player {state} win!')

    os._exit(0)
