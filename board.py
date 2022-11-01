class Board:
    def __init__(self):
        self.board = [" " for i in range(9)]
        self.result = None
        self.pieces = ["x", "o"]
        
    def insert(self, piece, square):
        if square > 8 or square < 0:
            return False
        
        if self.board[square] != " ":
            return False

        self.board[square] = piece
        return True

    def check_result(self):
        wincombos = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                     [0, 3, 6], [1, 4, 7], [2, 5, 8],
                     [0, 4, 8], [2, 4, 6]]

        for piece in self.pieces:
            for wincombo in wincombos:
                if (self.board[wincombo[0]], self.board[wincombo[1]], self.board[wincombo[2]]) == (piece, piece, piece):
                    return piece
        
        if " " not in self.board:
            self.result = "d"
            return "d"
        
        return False

    def __repr__(self):
        string = ""
        string += f" {self.board[0]} | {self.board[1]} | {self.board[2]} \n"
        string += "-----------\n"
        string += f" {self.board[3]} | {self.board[4]} | {self.board[5]} \n"
        string += "-----------\n"
        string += f" {self.board[6]} | {self.board[7]} | {self.board[8]} \n"
        return string

    def __getitem__(self, idx):
        return self.board[idx-1]