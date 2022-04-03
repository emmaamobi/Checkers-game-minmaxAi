from rules import Rules

class GameLogic:
   
    def __init__(self, board): 
        self.game = self
        self.board = board
        self.rules = Rules()
        self.player_1 ="RED" # referes to pieces
        self.player_2 ="BLACK"
        self.currentPlayer=self.player_1
        self.playing_game()
        #self.gameScore = self.score() 


    def playing_game(self):

        while self.check_for_winner()==True :
            print(self.currentPlayer, "pieces turn") 
         
            # calls board to get board state, playing piece and chosen by USER move
            # 
            if self.rules.validateMove(self.board.getInput(boardState,playing_piece, chosen_move)):
                self.game.makeMove(playing_piece, chosen_move)
                self.game.switchTurn()
                print("Move is made") # for debugging purposes

                return True
            else:
                print ("Invalid move, try again")
        
        self.playing_game()
                


    def makeMove(self,piece,destination_coordinate):
        piece_position = piece.getPosition()
        
        # check if the piece is jumping over an opponent's piece
        if abs(destination_coordinate[0]-piece_position[0])>1 or abs(destination_coordinate[1]-piece_position[1])  :
            currentPiece = piece.getColor()

            # decrease number of opponent's pieces
            if currentPiece == "RED":
                self.board.setBlackPieces(self.board.getBlakcPieces()-1)
            else:
                self.board.setRedPieces(self.board.getRedPieces()-1)
        # changes playing piece position       
        piece.setPosition(destination_coordinate[0],destination_coordinate[1])      
            

    def switchTurn(self):
        if self.currentPlayer == self.player_1:
            self.currentPlayer = self.player_2
            print("Red'pieces turn")
        else:
            self.currentPlayer= self.player_1 
            print("Black'pieces turn")


    def check_for_winner(self):
        if self.board.getRedPieces() == 0 :
            print("Black pieces player won")
            return False
        elif self.board.getBlackPieces() == 0 :
            print("Red pieces player won")
            return False
        else:
            print("Keep playing..")
            return True   


    # def score(self):
    #     self.score = self.player_1.getPieces()-self.player_2.getPieces()+(self.player_1.getNumberKings()*1.5 -self.player_2.getNumberKings()*1.5)

