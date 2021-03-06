import pygame
from ui_consts import EACH_SQUARE, W,H,RED,WHITE,BLACK
from piece import Piece
class Board: 
    """
    Standard Checkers board, 8 x 8 grid, red vs white pieces. 
    """

    def __init__(self):
        self.board = []
        self.rows = 8
        self.cols = 8
        self.white_pieces = 12
        self.red_pieces = 12
        self.white_kings = 0
        self.red_kings = 0
        self.initializeBoard()

        # pygame UI variables

        

    def initializeBoard(self):

        for row in range(self.rows):
            self.board.append([])
            for col in range(self.cols):
                if col % 2 == ((row + 1) % 2): # draw only on black squares
                    if row < 3:# white on first 3 rows
                        white_piece = Piece(WHITE,row,col)
                        self.board[row].append(white_piece)

                    elif row > 4: #red on bottom 3 rows
                        red_piece = Piece(RED,row,col)
                        self.board[row].append(red_piece)

                    else: # fill empty playable slots with 0
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
  
    def initializePossibleBoard(self, b): 
        for row in range(b.rows):
            for col in range(b.cols):
                self.board[row][col]=b.board[row][col]


    def get_board(self):
        return self.board
    

    def draw_board(self,window):
        window.fill(BLACK)
        for row in range(self.rows):
            x_cord = row*EACH_SQUARE
            width, height = EACH_SQUARE, EACH_SQUARE
            for col in range(row % 2, self.rows, 2):
                y_cord = col*EACH_SQUARE
                mini_square = (x_cord, y_cord, width, height)
                pygame.draw.rect(window, WHITE, mini_square)

    def draw_pieces(self, window):
        for row in range (self.rows):
            for col in range(self.cols):
                cur_piece = self.board[row][col]
                if cur_piece != 0:
                    cur_piece.draw_piece(window)
    
    def draw_game(self,window):
        self.draw_board(window)
        self.draw_pieces(window)
    
    def move_piece(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]

        # make white king
        if row == self.rows-1 and piece.color == WHITE and piece.isKing == False:
            piece.setKing()
            self.white_kings += 1

        # make red king
        if row == 0 and piece.color == RED and piece.isKing == False:
            piece.setKing()
            self.red_kings += 1

        # update piece pos
        piece.update_pos(row,col)

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece.color == RED:
                self.red_pieces -= 1
            else:
                self.white_pieces -= 1
        # print("RED PIECES: ", self.red_pieces)
        # print("white PIECES: ", self.white_pieces)

    """
    returns piece at given index
    """
    def get_piece(self, row, col):
        return self.board[row][col]
    
    #get all pieces for given color
    def getAllPieces(self, color):
        pieces=[]
        for row in range(self.rows): 
            for col in range(self.cols):
                piece=self.board[row][col]
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces
                        
                        
                        
                        
                        
                        
