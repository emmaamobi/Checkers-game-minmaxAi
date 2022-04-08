import pygame
from ui_consts import W, H
from utils import get_index_from_click
from gameLogic import GameLogic
from board import Board

# initialize window
WIN = pygame.display.set_mode((W,H))
pygame.display.set_caption('checkers minmax')



# runner
def main():
    running = True
    clock = pygame.time.Clock()
    board = Board()
    cur_game = GameLogic(board,WIN)

    while running:
        clock.tick(60) # constant framerate 
        # if cur_game.check_for_winner() != None:
        #     print("WINNER IS: ", cur_game.check_for_winner())
        #     running = False 


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pos()
                row, col = get_index_from_click(click)
                # cur_game.select(row,col)
                piece = board.get_piece(row,col)
                print(piece)
        board.draw_game(WIN) # use cur_game.update()  instead
        
        pygame.display.update()

    pygame.quit() # close window


if __name__ == "__main__":
    main()
