import unittest
import tictactoe


class MyTestCase(unittest.TestCase):
    def test_space_marked(self):
        board = tictactoe.Board()

        board.mark_square(0, 'X')
        self.assertEqual(board.boardArr[0], "X")
        board.mark_square(1, 'X')
        self.assertEqual(board.boardArr[1], "X")
        board.mark_square(2, 'X')
        self.assertEqual(board.boardArr[2], "X")
        board.mark_square(3, 'X')
        self.assertEqual(board.boardArr[3], "X")
        board.mark_square(4, 'X')
        self.assertEqual(board.boardArr[4], "X")
        board.mark_square(5, 'X')
        self.assertEqual(board.boardArr[5], "X")
        board.mark_square(6, 'X')
        self.assertEqual(board.boardArr[6], "X")
        board.mark_square(7, 'X')
        self.assertEqual(board.boardArr[7], "X")
        board.mark_square(8, 'X')
        self.assertEqual(board.boardArr[8], "X")

    def test_has_no_winner(self):
        test_board = tictactoe.Board()
        player = 'X'
        self.assertFalse(test_board.has_winner(player))
    
    def test_has_winner(self):
        player = 'X'

        winner_board = tictactoe.Board()
        winner_board.boardArr[0] = 'X'
        winner_board.boardArr[1] = 'X'
        winner_board.boardArr[2] = 'X'
        self.assertTrue(winner_board.has_winner(player))

        col_board = tictactoe.Board()
        col_board.boardArr[0] = 'X'
        col_board.boardArr[3] = 'X'
        col_board.boardArr[6] = 'X'
        self.assertTrue(col_board.has_winner(player))

        diag_board = tictactoe.Board()
        diag_board.boardArr[0] = 'X'
        diag_board.boardArr[4] = 'X'
        diag_board.boardArr[8] = 'X'
        self.assertTrue(diag_board.has_winner(player))
    
    def test_convert_arr(self):
        self.assertEqual(tictactoe.convert_arr(1, 1), 0)
        self.assertEqual(tictactoe.convert_arr(1, 2), 1)
        self.assertEqual(tictactoe.convert_arr(1, 3), 2)
        self.assertEqual(tictactoe.convert_arr(2, 1), 3)
        self.assertEqual(tictactoe.convert_arr(2, 2), 4)
        self.assertEqual(tictactoe.convert_arr(2, 3), 5)
        self.assertEqual(tictactoe.convert_arr(3, 1), 6)
        self.assertEqual(tictactoe.convert_arr(3, 2), 7)
        self.assertEqual(tictactoe.convert_arr(3, 3), 8)

    def test_switch_player(self):
        board = tictactoe.Board()
        board.current_plyr = 'X'
        board.switch_player()
        self.assertEqual(board.current_plyr, 'O')
        board.switch_player()
        self.assertEqual(board.current_plyr, 'X')

    def test_matching_row(self):
        board1 = tictactoe.Board()
        board1.boardArr[0] = 'X'
        board1.boardArr[1] = 'X'
        board1.boardArr[2] = 'X'
        self.assertTrue(board1.matching_row('X'))

        board2 = tictactoe.Board()
        board2.boardArr[3] = 'X'
        board2.boardArr[4] = 'X'
        board2.boardArr[5] = 'X'
        self.assertTrue(board2.matching_row('X'))

        board3 = tictactoe.Board()
        board3.boardArr[6] = 'X'
        board3.boardArr[7] = 'X'
        board3.boardArr[8] = 'X'
        self.assertTrue(board3.matching_row('X'))

        board_no_match = tictactoe.Board()
        self.assertFalse(board_no_match.matching_row('X'))
        self.assertFalse(board_no_match.matching_row('O'))

    def text_matching_col(self):
        board1 = tictactoe.Board()
        board1.boardArr[0] = 'X'
        board1.boardArr[3] = 'X'
        board1.boardArr[6] = 'X'
        self.assertTrue(board1.matching_col('X'))

        board2 = tictactoe.Board()
        board2.boardArr[1] = 'X'
        board2.boardArr[4] = 'X'
        board2.boardArr[7] = 'X'
        self.assertTrue(board2.matching_col('X'))

        board3 = tictactoe.Board()
        board3.boardArr[2] = 'X'
        board3.boardArr[5] = 'X'
        board3.boardArr[8] = 'X'
        self.assertTrue(board3.matching_col('X'))

        board_no_match = tictactoe.Board()
        self.assertFalse(board_no_match.matching_col('X'))
        self.assertFalse(board_no_match.matching_col('O'))

    def matching_diag(self):
        board1 = tictactoe.Board()
        board1.boardArr[0] = 'X'
        board1.boardArr[4] = 'X'
        board1.boardArr[8] = 'X'
        self.assertTrue(board1.matching_diag('X'))

        board2 = tictactoe.Board()
        board2.boardArr[2] = 'X'
        board2.boardArr[4] = 'X'
        board2.boardArr[6] = 'X'
        self.assertTrue(board2.matching_diag('X'))

        board_no_match = tictactoe.Board()
        self.assertFalse(board_no_match.matching_diag('X'))
        self.assertFalse(board_no_match.matching_diag('O'))

    def play_game(self):
        board = tictactoe.Board()
        board.play_game(2, 2)
        self.assertEqual(board.boardArr[4], board.current_plyr)

    def test_print_board(self):
        board = tictactoe.Board()
        board.play_game(2, 2)



    def out_of_bounds(self):
        pass

    def board_full(self):
        pass

    #ARRANGE
    #ACT
    #ASSERT


if __name__ == '__main__':
    unittest.main()
