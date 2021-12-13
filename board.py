from piece import Bishop
from piece import King
from piece import Knight
from piece import Pawn
from piece import Queen
from piece import Rook

class Board:
    def __init__(self, row, col):
        self.row = row
        self.col = col

        self.board = [[0 for x in range(8)] for _ in range(row)]
        
        self.board[0][0] = Rook(0,0,"black")
        self.board[1][0] = Knight(1,0,"black")
        self.board[2][0] = Bishop(2,0,"black")
        self.board[3][0] = Queen(3,0,"black")
        self.board[4][0] = King(4,0,"black")
        self.board[5][0] = Bishop(5,0,"black")
        self.board[6][0] = Knight(6,0,"black")
        self.board[7][0] = Rook(7,0,"black")

        self.board[0][1] = Pawn(0,1,"black")
        self.board[1][1] = Pawn(1,1,"black")
        self.board[2][1] = Pawn(2,1,"black")
        self.board[3][1] = Pawn(3,1,"black")
        self.board[4][1] = Pawn(4,1,"black")
        self.board[5][1] = Pawn(5,1,"black")
        self.board[6][1] = Pawn(6,1,"black")
        self.board[7][1] = Pawn(7,1,"black")

        self.board[0][7] = Rook(0,7,"white")
        self.board[1][7] = Knight(1,7,"white")
        self.board[2][7] = Bishop(2,7,"white")
        self.board[3][7] = Queen(3,7,"white")
        self.board[4][7] = King(4,7,"white")
        self.board[5][7] = Bishop(5,7,"white")
        self.board[6][7] = Knight(6,7,"white")
        self.board[7][7] = Rook(7,7,"white")

        self.board[0][6] = Pawn(0,6,"white")
        self.board[1][6] = Pawn(1,6,"white")
        self.board[2][6] = Pawn(2,6,"white")
        self.board[3][6] = Pawn(3,6,"white")
        self.board[4][6] = Pawn(4,6,"white")
        self.board[5][6] = Pawn(5,6,"white")
        self.board[6][6] = Pawn(6,6,"white")
        self.board[7][6] = Pawn(7,6,"white")

    def draw(self, screen):
        for i in range(self.row):
            for j in range(self.col):
                if self.board[i][j] != 0:
                    self.board[i][j].draw(screen)
