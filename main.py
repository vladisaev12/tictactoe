#!/usr/bin/env python3

import os
# import sys
import tkinter as tk
from tkinter import messagebox
# import threading


# def display(size):
#     row_delim = '+'
#     for i in range(size):
#         row_delim += '-+'
#     print(row_delim)
#     for row in table:
#         print('|', end='')
#         for field in row:
#             print(field, end='|')
#             sys.stdout.flush()
#         print()
#         print(row_delim)


class Game:

    def __init__(self, size):
        self.table = self.init_table(size)
        self.player = 'X'
        self.turn_count = 0
        self.state = 'cont'

    def init_table(self, size):
        table = []
        row = []
        for i in range(size):
            row.append(' ')
        for j in range(size):
            table.append(row.copy())

        return table

    def validate(self, size, x, y):
        if x < 0 or x > size - 1:
            print('Error: invalid row number')
            return False

        if y < 0 or y > size - 1:
            print('Error: invalid column number')
            return False

        return True

    def flip_player(self):
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def turn(self, table, x, y):
        if not self.validate(len(table), x, y):
            return False

        if table[x][y] != ' ':
            print('Error: field is not empty')
            return False

        table[x][y] = self.player

        return True

    def check_hv(self, table, player):
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

    def check_d(self, table, player):
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

    def check(self, table, player, turn_count):
        if self.check_hv(table, player) or self.check_d(table, player):
            return player

        if turn_count == len(table)**2:
            return 'XO'

        return 'cont'


class App:

    def __init__(self):
        self.init_window()

    def init_window(self):
        window = tk.Tk()
        window.title('tictactoe')
        window.attributes('-type', 'dialog')

        scale = tk.Scale(master=window, from_=3, to=10, orient=tk.HORIZONTAL)
        scale.pack()
        button = tk.Button(master=window, text="Start")
        button['command'] = lambda window=window, scale=scale, button=button: (
            self.init_game(window, scale, button)
        )
        button.pack()

        window.mainloop()

    def init_game(self, window, scale, button):
        size = scale.get()
        scale.destroy()
        button.destroy()

        self.game = Game(size)

        for i in range(size):
            window.columnconfigure(i, weight=1, minsize=50)
            window.rowconfigure(i, weight=1, minsize=50)

            for j in range(size):
                button = tk.Button(master=window, text=" ")
                button['command'] = lambda button=button, i=i, j=j: (
                    self.on_clicked(button, i, j)
                )
                button.grid(row=i, column=j, sticky='nswe')

    def on_clicked(self, button, x, y):
        print(f'on_clicked: x={x} y={y}')

        if self.game.state != 'cont':
            return

        if self.game.turn(self.game.table, x, y):
            button['text'] = self.game.player
            self.game.turn_count += 1
            state = self.game.check(
                self.game.table,
                self.game.player,
                self.game.turn_count
            )
            self.game.flip_player()

        if state == 'XO':
            print('Nobody win :(')
            messagebox.showinfo('The End', 'Nobody win :(')
            os._exit(0)
        elif state != 'cont':
            print(f'Player {state} win!')
            messagebox.showinfo('The End', f'Player {state} win!')
            os._exit(0)


if __name__ == '__main__':
    app = App()

#    size = int(input('size of table = '))
#    table = init_table(size)
#    display(size)
#    init_window(size)
#    thr = threading.Thread(target=init_window,args=[size],daemon=True)
#    thr.start()
#    while state == 'cont':
#        print(f'Player {player}:')
#        x = int(input('row = '))
#        y = int(input('col = '))
#        if turn(table, x - 1, y - 1):
#            turn_count += 1
#            state = check(table, player, turn_count)
#            flip_player()
#        display(size)
#
#    if state == 'XO':
#        print('Nobody win :(')
#    else:
#        print(f'Player {state} win!')
#
    os._exit(0)
