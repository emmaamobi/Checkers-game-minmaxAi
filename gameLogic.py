class GameLogic:
   
    def __init__(self, player1, player2): 
        self.game = self
        self.player_1=player1
        self.player_2=player2
        self.currentPlayer=player1
        self.gameScore = self.score()
    
       

    def switchTurn(self):
        if self.currentPlayer == self.player_1:
            self.currentPlayer = self.player_2
            print("Second player turn")
        else:
            self.currentPlayer= self.player_1 
            print("First player turn")


    def check_for_winner(self):
        if self.player_1.getPieces() == 0 :
            print("Second player won")
            return False
        elif self.player_2.getPieces() == 0 :
            print("First player won")
            return False
        else:
            return True   


    # def score(self):
    #     self.score = self.player_1.getPieces()-self.player_2.getPieces()+(self.player_1.getNumberKings()*1.5 -self.player_2.getNumberKings()*1.5)

