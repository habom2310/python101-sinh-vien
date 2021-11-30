import utils

class Player:
    num_player = 0

    def __init__(self, name):
        self.name = name
        self.__class__.num_player += 1
        self.score = 0 
        if (self.__class__.num_player == 1):
            self.symbol = "X"
        elif (self.__class__.num_player == 2):
            self.symbol = "O"
        else:
            print("enough player")

    def __repr__(self):
        return self.name
        
class Caro:

    def __init__(self, x, y):
        self.board = self.create_board(x, y)
        print("Welcome to Caro Game")
        player1 = input("Enter player name 1: ")
        player2 = input("Enter player name 2: ")
        self.player1 = Player(player1)
        self.player2 = Player(player2)
        print(f"Player 1 {self.player1} will go first")
        self.current_player = self.player1
        self.print_board()
        self.is_win = False
        self.is_draw = False

    def move(self, player, x, y):
        if (self.board[x][y] != " "):
            print("This position is not empty. Please enter another position")
            return False
        else:
            print("-"*30 + "\n")
            print(f"Player {self.current_player}'s turn")
            self.board[x][y] = player.symbol
            self.print_board()
            self.is_win = self.check_win()
            self.is_draw = self.check_draw()
            self.change_player(player)

    def change_player(self, player):
        if (player == self.player1):
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def check_row(self):
        for row in self.board:
            for j in range(len(row) - 5):
                if row[j:j+5].count(row[j]) == 5 and row[j] != " ":
                    return True
        return False

    def check_col(self):
        for i in range(len(self.board[0])):
            col = [row[i] for row in self.board]
            for j in range(len(col) - 5):
                if col[j:j+5].count(col[j]) == 5 and col[j] != " ":
                    return True
        return False

    def check_diagonal(self):
        fdiag, bdiag = utils.get_diagonal(self.board)
        for diag in fdiag:
            if len(diag) < 5:
                continue
            else:
                for i in range(len(diag) - 5):
                    if diag[i:i+5].count(diag[i]) == 5 and diag[i] != " ":
                        return True
            
        for diag in bdiag:
            if len(diag) < 5:
                continue
            else:
                for i in range(len(diag) - 5):
                    if diag[i:i+5].count(diag[i]) == 5 and diag[i] != " ":
                        return True

        return False

    def check_win(self):
        if (self.check_row() or self.check_col() or self.check_diagonal()):
            print("Player {} win".format(self.current_player.name))
            return True
        else:
            return False
    
    def check_draw(self):
        for row in self.board:
            if " " in row:
                return False
        
        print("Draw")
        return True

    def print_board(self):
        utils.drawBoard(self.board)

    def reset(self):
        pass

    def create_board(self, x, y):
        board = [y * [" "] for _ in range(x)]
        return board

    def start_game(self):
        while (not self.is_win and not self.is_draw):
            while (not self.move(self.current_player, int(input("Enter x: ")), int(input("Enter y: ")))):
                if (self.is_win or self.is_draw):
                    break