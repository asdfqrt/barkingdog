class TicTacToe:
    def __init__(self):
        self.board = [["-" for i in range(3)] for j in range(3)]

    def display_board(self):
        for row in self.board:
            print(" ".join(row))

    def update_board(self, row, col, player):
        self.board[row][col] = player

    def is_full(self):
        for row in self.board:
            if "-" in row:
                return False
        return True

    def has_won(self, player):
        for row in self.board:
            if row == [player, player, player]:
                return True

        for col in range(3):
            if all([row[col] == player for row in self.board]):
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True

        return False

    def get_valid_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "-":
                    moves.append((i, j))
        return moves

    def minimax(self, player):
        if self.has_won("X"):
            return 1
        if self.has_won("O"):
            return -1
        if self.is_full():
            return 0

        scores = []
        for row, col in self.get_valid_moves():
            self.update_board(row, col, player)
            if player == "X":
                scores.append(self.minimax("O"))
            else:
                scores.append(self.minimax("X"))
            self.update_board(row, col, "-")

        if player == "X":
            return max(scores)
        else:
            return min(scores)

    def best_move(self, player):
        best_score = None
        best_move = None
        for row, col in self.get_valid_moves():
            self.update_board(row, col, player)
            score = self.minimax("O" if player == "X" else "X")
            self.update_board(row, col, "-")

            if player == "X":
                if best_score is None or score > best_score:
                    best_score = score
                    best_move = (row, col)
            else:
                if best_score is None or score < best_score:
                    best_score = score
                    best_move = (row, col)

        return best_move


game = TicTacToe()
game.display_board()
while not game.has_won("X") and not game.has_won("O") and not game.is_full():
    x,y = map(int,input().split())
    game.update_board(x, y, 'X')
    game.display_board()
    print("")
    computer_move = game.best_move('O')
    game.update_board(*computer_move, 'O')
    game.display_board()
    print("")
if game.has_won("X"):
    print("X has won!")
elif game.has_won("O"):
    print("O has won!")
elif game.is_full():
    print("The game has ended in a draw.")