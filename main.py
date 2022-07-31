#!/usr/bin/env python3

import os
import sys


table = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

player = 'X'


def display():
    row_delim = '+-+-+-+'
    print(row_delim)
    for row in table:
        print('|', end='')
        for field in row:
            print(field, end='|')
            sys.stdout.flush()
        print()
        print(row_delim)


def validate(x, y):
    if x < 0 or x > 2:
        print('Error: invalid row number')
        return False

    if y < 0 or y > 2:
        print('Error: invalid column number')
        return False

    return True


def flip_player():
    global player
    if player == 'X':
        player = 'O'
    else:
        player = 'X'


def turn(x, y):
    if not validate(x, y):
        return False

    if table[x][y] != ' ':
        print('Error: field is not empty')
        return False

    global player
    table[x][y] = player

    return True


def check(table, player):
    for i in range(3):
        flag = True
        for j in range(3):
            flag &= table[i][j] == player
            if not flag:
                break
        if flag:
            return player

    flag = True
    for j in range(3):
        flag &= table[j][i] == player
        if not flag:
            break
    if flag:
        return player

    flag = True
    for i in range(3):
        flag &= table[i][i] == player
        if not flag:
            break
    if flag:
        return player

    flag = True
    for i in range(3):
        flag &= table[i][2 - i] == player
        if not flag:
            break
    if flag:
        return player

    # TODO: XO?

    return 'cont'


if __name__ == '__main__':
    display()

    state = 'cont'
    while state == 'cont':
        print(f'Player {player}:')
        x = int(input('row = '))
        y = int(input('col = '))
        if turn(x - 1, y - 1):
            state = check(table, player)
            flip_player()
        display()

    if state == 'XO':
        print('Nobody win :(')
    else:
        print(f'Player {state} win!')

    os._exit(0)
