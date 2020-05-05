def convert_arr(row_str, col_str):
    col = int(col_str)
    row = int(row_str)
    row -= 1
    col -= 1
    index = row * 3 + col
    return index


class Board(object):

    def __init__(self):
        self.boardArr = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.plyr1 = 'X'
        self.plyr2 = 'O'
        self.current_plyr = self.plyr2

    def print_board(self):
        print("Printed Board")
        print(self.boardArr[0] + self.boardArr[1] + self.boardArr[2])
        print(self.boardArr[3] + self.boardArr[4] + self.boardArr[5])
        print(self.boardArr[6] + self.boardArr[7] + self.boardArr[8])

    def mark_square(self, index, player):
        #if(index>8):
        self.boardArr[index] = player

    def switch_player(self):
        if self.current_plyr == self.plyr1:
            self.current_plyr = self.plyr2
        else:
            self.current_plyr = self.plyr1

    def matching_row(self, player):
        if self.boardArr[0] == player and self.boardArr[1] == player and self.boardArr[2] == player:
            return 1
        if self.boardArr[3] == player and self.boardArr[4] == player and self.boardArr[5] == player:
            return 1
        if self.boardArr[6] == player and self.boardArr[7] == player and self.boardArr[8] == player:
            return 1
        else:
            return 0

    def matching_col(self, player):
        if self.boardArr[0] == player and self.boardArr[3] == player and self.boardArr[6] == player:
            return 1
        if self.boardArr[1] == player and self.boardArr[4] == player and self.boardArr[7] == player:
            return 1
        if self.boardArr[2] == player and self.boardArr[5] == player and self.boardArr[8] == player:
            return 1
        else:
            return 0

    def matching_diag(self, player):
        if self.boardArr[0] == player and self.boardArr[4] == player and self.boardArr[8] == player:
            return 1
        elif self.boardArr[2] == player and self.boardArr[4] == player and self.boardArr[6] == player:
            return 1
        else:
            return 0

    def has_winner(self, player):
        if self.matching_row(player):
            return 1
        elif self.matching_col(player):
            return 1
        elif self.matching_diag(player):
            return 1
        else:
            return 0

    def play_game(self, row, col):
        index = convert_arr(row, col)
        self.mark_square(index, self.current_plyr)


if __name__ == '__main__':
    board = Board()
    while not board.has_winner(board.current_plyr):
        board.print_board()
        board.switch_player()
        print("Player " + board.current_plyr + "'s move")
        row, col = input("Enter row, col: ").split(',')
        board.play_game(row, col)

    winner = board.current_plyr
    print("{} has won!".format(winner))
