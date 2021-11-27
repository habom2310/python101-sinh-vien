from abc import abstractmethod, ABC

class Player:
    num_player = 0

    def __init__(self, name, type = "human"):
        self.name = name
        self.__class__.num_player += 1
        if self.__class__.num_player == 1:
            self.symbol = 'x' #người 1
        elif self.__class__.num_player == 2:
            self.symbol = 'o' #người 2

class Caro(ABC):
    def __init__(self, nrow = 10, ncol = 10):
        self.nrow = nrow
        self.ncol = ncol
        self.board = self.create_board(nrow = self.nrow, ncol = self.ncol)
        player1 = Player(input("nhap ten nguoi choi 1:"))
        player2 = Player(input("nhap ten nguoi choi 2:"))
        self.current_player = player1

    def create_board(nrow = 10, ncol = 10):
        array = [[0] * ncol for _ in range(nrow)]
        return array

    def draw_board(board):
        for row in board:
            for element in row:
                print(str(element),end="|")
            print("\n" + "-+"*len(row))

    @abstractmethod
    def move(self, row, col):
        """
        hàm move nhận input là row: int, col: int.
        Check input.
        update board. 
        """
        pass

    @abstractmethod
    def check_input(self, row, col):
        """
        input: row, col
        Check xem input đúng format
        check xem trên board ở vị trí row, col đã có ai đánh chưa
        """
        pass

    @abstractmethod
    def update_board(self, row, col, symbol):
        """
        update board hiện tại (thêm symbol: x, o vào vị trí input)
        """
        pass

    @abstractmethod
    def check_win(self):
        """
        check_row and check_col and check_diag
        kiểm tra điều kiện thắng: hàng, cột, chéo 
        """
        pass

    def check_row(self):
        pass

    def check_col(self):
        pass

    def check_diag(self):
        pass

    @abstractmethod
    def check_draw(self):
        """
        kiểm tra xem tất cả các ô đã bị đánh hay chưa
        """
        pass

    @abstractmethod
    def change_current_player(self):
        """
        gán self.current_player thành người chơi khác
        """
        pass

    @abstractmethod
    def start_game(self):
        """
        đóng gói tất cả tính năng.
        """
        pass