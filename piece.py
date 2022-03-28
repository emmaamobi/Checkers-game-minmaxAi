class Piece: 
    def __init__(self,c, x,y):
        self.color=c
        self.isKing=False
        self.xPosition=x
        self.yPosition=y
        self.possibleMoves=[]
        
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