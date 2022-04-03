import pygame
from ui_consts import EACH_SQUARE, W,H,RED,WHITE,BLACK,BLUE
class Piece: 
    def __init__(self,c, x,y):
        """
        xPosition --> row
        yPosition --> col
        """
        self.color=c
        self.isKing=False
        self.xPosition=x
        self.yPosition=y
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
        self.yPosition=y
    def getKing(self):
        return self.isKing
    def getColor(self):
        return self.color
    def getPosition(self):
        return [self.xPosition, self.YPosition]
    def getPossibleMoves(self):
        return self.possibleMoves

    # UI STUFF 
    # set_cord --> to set the coordinates for drawing
    def set_cord(self):
        self.x_cord = (EACH_SQUARE * self.yPosition) + EACH_SQUARE // 2
        self.y_cord = (EACH_SQUARE * self.xPosition) + EACH_SQUARE // 2

    def draw_piece(self,win):
        x_y_cords = (self.x_cord, self.y_cord)
        pad, outline = 10, 4
        radius = (EACH_SQUARE // 2) - pad
        pygame.draw.circle(win, BLUE, x_y_cords, radiuis + self.outline )
        pygame.draw.circle(win, self.color, x_y_cords, radiuis)

