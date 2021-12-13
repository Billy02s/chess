import pygame

piece_width, piece_height = 800//8, 800//8

bb = pygame.transform.smoothscale(pygame.image.load('assets/bBishop.png'), (piece_width, piece_height))
bk = pygame.transform.smoothscale(pygame.image.load('assets/bKing.png'), (piece_width, piece_height))
bn = pygame.transform.smoothscale(pygame.image.load('assets/bKnight.png'), (piece_width, piece_height))
bp = pygame.transform.smoothscale(pygame.image.load('assets/bPawn.png'), (piece_width, piece_height))
bq = pygame.transform.smoothscale(pygame.image.load('assets/bQueen.png'), (piece_width, piece_height))
br = pygame.transform.smoothscale(pygame.image.load('assets/bRook.png'), (piece_width, piece_height))

wb = pygame.transform.smoothscale(pygame.image.load('assets/wBishop.png'), (piece_width, piece_height))
wk = pygame.transform.smoothscale(pygame.image.load('assets/wKing.png'), (piece_width, piece_height))
wn = pygame.transform.smoothscale(pygame.image.load('assets/wKnight.png'), (piece_width, piece_height))
wp = pygame.transform.smoothscale(pygame.image.load('assets/wPawn.png'), (piece_width, piece_height))
wq = pygame.transform.smoothscale(pygame.image.load('assets/wQueen.png'), (piece_width, piece_height))
wr = pygame.transform.smoothscale(pygame.image.load('assets/wRook.png'), (piece_width, piece_height))

b_pieces = [bb, bk, bn, bp, bq, br]
w_pieces = [wb, wk, wn, wp ,wq, wr]

class Piece:
    image = -1

    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour
        self.selected = False
    
    def move(self):
        pass

    def selected(self):
        return self.selected

    def draw(self, board):
        if self.colour == "white":
            draw = w_pieces[self.image]
        elif self.colour == "black":
            draw = b_pieces[self.image]

        x = self.row
        y = self.col
        
        board.blit(draw, (x * 100,y * 100))

        

class Bishop(Piece):
    image = 0

class King(Piece):
    image = 1

class Knight(Piece):
    image = 2

class Pawn(Piece):
    image = 3

class Queen(Piece):
    image = 4

class Rook(Piece):
    image = 5

