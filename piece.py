import pygame
from ui_consts import EACH_SQUARE, W,H,RED,WHITE,BLACK,BLUE,GOLD
class Piece: 
    def __init__(self,c, row,col):
        self.color=c
        self.isKing=False
        self.row=row
        self.col=col
        self.possibleMoves=[]

         # for position on board, UI
        self.x_cord = 0
        self.y_cord = 0
        self.set_cord()


        
#TODO: Implement setter for possible moves
        

    def setKing(self): 
        self.isKing=True
    def setColor(self,c):
        self.color=c
    def setPosition(self,x,y):
        self.xPostion=x
        self.col=y
    def getKing(self):
        return self.isKing
    def getColor(self):
        return self.color
    def getPosition(self):
        return [self.row, self.YPosition]
    def getPossibleMoves(self):
        return self.possibleMoves

    # UI STUFF 
    # set_cord --> to set the coordinates for drawing
    def set_cord(self):
        self.x_cord = (EACH_SQUARE * self.col) + EACH_SQUARE // 2
        self.y_cord = (EACH_SQUARE * self.row) + EACH_SQUARE // 2

    def draw_piece(self,win):
        x_y_cords = (self.x_cord, self.y_cord)
        pad = 10
        radius = (EACH_SQUARE // 2) - pad
        #outline = 2
        ## pygame.draw.circle(win, BLUE, x_y_cords, radius + outline )
        pygame.draw.circle(win, self.color, x_y_cords, radius)

        ## draw king
        if self.isKing:
            radius_smaller = ((EACH_SQUARE // 2) // 2)
            pygame.draw.circle(win, GOLD, x_y_cords, radius_smaller)

    def update_pos(self,row,col):
        self.row = row
        self.col = col
        self.set_cord()

    def __repr__(self):
        res = ""
        res += "{} piece located at {},{}\n".format(self.color,self.row,self.col)
        return res

