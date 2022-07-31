#!/usr/bin/env python3

import unittest
import main


class TestXO(unittest.TestCase):

    def test_check(self):
        testdata = [
            ([[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']], 'X', 'cont'),
            ([['X', 'X', 'X'],
              [' ', ' ', ' '],
              [' ', ' ', ' ']], 'X', 'X'),
            ([[' ', ' ', ' '],
              ['O', 'O', 'O'],
              [' ', ' ', ' ']], 'O', 'O'),
            ([['X', ' ', ' '],
              ['X', ' ', ' '],
              ['X', ' ', ' ']], 'X', 'X'),
            ([[' ', 'X', ' '],
              [' ', 'X', ' '],
              [' ', 'X', ' ']], 'X', 'X'),
            ([[' ', ' ', 'X'],
              [' ', ' ', 'X'],
              [' ', ' ', 'X']], 'X', 'X'),
            ([['X', ' ', ' '],
              [' ', 'X', ' '],
              [' ', ' ', 'X']], 'X', 'X'),
            ([[' ', ' ', 'O'],
              [' ', 'O', ' '],
              ['O', ' ', ' ']], 'O', 'O'),
            ([[' ', ' ', 'O'],
              [' ', 'X', ' '],
              ['O', ' ', ' ']], 'O', 'cont'),
        ]
        for table, player, result in testdata:  # 123
            self.assertEqual(main.check(table, player),
                             result,
                             msg=f'case: {table}, {player}')


if __name__ == '__main__':
    unittest.main()
