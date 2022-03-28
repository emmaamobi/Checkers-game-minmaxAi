import pygame
from ui_consts import EACH_SQUARE, W,H,RED,WHITE,BLACK
class Board: 
    """
    Standard Checkers board, 8 x 8 grid, red vs white pieces. 
    """

    def __init__(self):
        self.board = []
        self.rows = 8
        self.cols = 8
        self.initializeBoard()

        # pygame UI variables

        

    def initializeBoard(self):
        square = 1 # white

        for row in range(self.rows):
            self.board.append([])
            for col in range(self.cols):
                self.board[row].append(square)
                if col == self.cols-1:
                    continue
                square = 0 if square == 1 else 1
    def get_board(self):
        return self.board

    def draw_board(self,win):

        win.fill(BLACK)
        for row in range(self.rows):
            x_cord = row*EACH_SQUARE
            width, height = EACH_SQUARE, EACH_SQUARE
            for col in range(row % 2, self.rows, 2):
                y_cord = col*EACH_SQUARE
                mini_square = (x_cord, y_cord, width, height)
                pygame.draw.rect(win, WHITE, mini_square)




