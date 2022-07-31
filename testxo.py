#!/usr/bin/env python3

import unittest
import main


class TestXO(unittest.TestCase):

    def test_init_table(self):
        testdata = [1, 3, 42]
        for size in testdata:
            table = main.init_table(size)
            self.assertEqual(size, len(table))
            for i in range(size):
                self.assertEqual(size, len(table[i]))
            for row in table:
                for field in row:
                    self.assertEqual(' ', field)

    def test_check(self):
        testdata = [
            ([[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']], 'X', 0, 'cont'),
            ([['X', 'X', 'X'],
              [' ', ' ', ' '],
              [' ', ' ', ' ']], 'X', 3, 'X'),
            ([[' ', ' ', ' '],
              ['O', 'O', 'O'],
              [' ', ' ', ' ']], 'O', 3, 'O'),
            ([['X', ' ', ' '],
              ['X', ' ', ' '],
              ['X', ' ', ' ']], 'X', 3, 'X'),
            ([[' ', 'X', ' '],
              [' ', 'X', ' '],
              [' ', 'X', ' ']], 'X', 3, 'X'),
            ([[' ', ' ', 'X'],
              [' ', ' ', 'X'],
              [' ', ' ', 'X']], 'X', 3, 'X'),
            ([['X', ' ', ' '],
              [' ', 'X', ' '],
              [' ', ' ', 'X']], 'X', 3, 'X'),
            ([[' ', ' ', 'O'],
              [' ', 'O', ' '],
              ['O', ' ', ' ']], 'O', 3, 'O'),
            ([[' ', ' ', 'O'],
              [' ', 'X', ' '],
              ['O', ' ', ' ']], 'O', 3, 'cont'),
            ([['X', 'O', 'X'],
              ['X', 'X', 'O'],
              ['O', 'X', 'O']], 'O', 9, 'XO'),
        ]
        for table, player, turn_count, result in testdata:
            self.assertEqual(result,
                             main.check(table, player, turn_count),
                             msg=f'case: {table}, {player}')


if __name__ == '__main__':
    unittest.main()
