import pygame
from rules import Rules
from ui_consts import EACH_SQUARE, W,H,RED,WHITE,BLACK
from AIPlayer import AIPlayer

class GameLogic:
   
    def __init__(self, board,window): 
        self.board = board
        self.window = window
        self.rules = Rules()
        self.player_1 = RED # referes to pieces
        self.player_2 = WHITE
        self.currentPlayer=self.player_1
        self.selected = None
        self.valid_moves = {}
        self.AIPlayer = AIPlayer()
        # self.ai_game=AIGame
        #self.gameScore = self.score() 


    # def playing_game(self):

    #     while self.check_for_winner()==True :
    #         print(self.currentPlayer, "pieces turn") 
         
    #         # calls board to get board state, playing piece and chosen by USER move
    #         # 
    #         if self.rules.validateMove(self.board.getInput(boardState,playing_piece, chosen_move)):
    #             self.game.makeMove(playing_piece, chosen_move)
    #             self.game.switchTurn()
    #             print("Move is made") # for debugging purposes

    #             return True
    #         else:
    #             print ("Invalid move, try again")
        
    #     self.playing_game()
                


    def update_ui(self):
        self.board.draw_game(self.window)
        if self.selected:
            piece = self.selected
            piece.highlight(self.window)
        pygame.display.update()

    def select_square(self, row, col):
        if self.selected:
            res = self.makeMove(row, col)
            if not res:
                self.selected = None
                self.select_square(row, col)
        
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.currentPlayer:
            self.selected = piece
            # highlight piece

            self.valid_moves = self.rules.possibleMoves(self.board,piece)
            # print("VALID MOVES: ", self.valid_moves)
            return True
            
        return False

    def makeMove(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move_piece(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.switchTurn()
        else:
            return False

        return True
            

    def switchTurn(self):
        self.valid_moves = {} # reset valid moves
        self.selected = None
        if self.currentPlayer == self.player_1:
            self.currentPlayer = self.player_2
            print("white 'pieces turn")
        else:
            self.currentPlayer= self.player_1 
            print("red 'pieces turn")

    def ai_make_move(self,piece, row, col):
        self.valid_moves = self.rules.possibleMoves(self.board,piece)
        self.board.move_piece(piece, row, col)
        skipped = self.valid_moves[(row, col)]
        if skipped:
            self.board.remove(skipped)
        self.switchTurn()

    def ai_play_random(self):
        piece, row, col = self.AIPlayer.randomMove(self.board)
        self.ai_make_move(piece, row, col)

    def ai_play_minimax(self):
        piece, row, col=self.AIPlayer.minimax(self.board, self, 2)
        self.ai_make_move(piece, row, col)
        

    def ai_make_move(self,piece, row, col):
        self.valid_moves = self.rules.possibleMoves(self.board,piece)
        self.board.move_piece(piece, row, col)
        skipped = self.valid_moves[(row, col)]
        if skipped:
            self.board.remove(skipped)
        self.switchTurn()

    def ai_play_random(self):
        piece, row, col = self.AIPlayer.randomMove(self.board)
        self.ai_make_move(piece, row, col)

    def ai_play_minimax(self):
        piece, row, col=self.AIPlayer.minimax(self.board, self, 2)
        self.ai_make_move(piece, row, col)
        
    def check_for_winner(self):
        return self.rules.winner(self.board)



