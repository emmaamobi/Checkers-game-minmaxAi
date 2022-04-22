import pygame
from rules import Rules
from ui_consts import EACH_SQUARE, W,H,RED,WHITE,BLACK
from AIPlayer import AIPlayer
from copy import deepcopy

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

    def ai_make_move(self,piece, row, col):
        self.valid_moves = self.rules.possibleMoves(self.board,piece)
        self.board.move_piece(piece, row, col)
        if (row, col) in self.valid_moves: #This might be part of skip problem!!!
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
        self.switchTurn()

    def ai_play_random(self):
        piece, row, col = self.AIPlayer.randomMove(self.board)
        self.ai_make_move(piece, row, col)

    def ai_play_minimax(self):
        score,oldrow,oldcol,newrow,newcol=self.AIPlayer.minimax(self.board,None,None,None,None, 1,WHITE)
        piece=self.board.board[oldrow][oldcol]
        self.ai_make_move(piece, newrow, newcol)
        
    def check_for_winner(self):
        return self.rules.winner(self.board)



