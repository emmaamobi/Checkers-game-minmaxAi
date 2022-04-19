import pygame
from ui_consts import W, H
from utils import get_index_from_click
from gameLogic import GameLogic
from board import Board
from ui_consts import EACH_SQUARE, W,H,RED,WHITE,BLACK,BLUE,GOLD
import PySimpleGUI as sg

# initialize window
WIN = pygame.display.set_mode((W,H))
pygame.display.set_caption('checkers minmax')



# runner
def main():
    AI_Game=False
    # event, values = sg.Window('What kind of game would you like to play?', [[sg.Text('Select one->'), sg.Listbox(['One Player', 'Two Player'], size=(20, 3), key='LB')],
    # [sg.Button('Ok'), sg.Button('Cancel')]]).read(close=True)
    
    # if event == 'Ok':
    #     if {values["LB"][0]}=="Two Player":
    #         AI_Game=True
    #     sg.popup(f'You chose {values["LB"][0]}')
    # else:
    #     sg.popup_cancel('User aborted')
            
    
    
    running = True
    clock = pygame.time.Clock()
    board = Board()
<<<<<<< Updated upstream
    cur_game = GameLogic(board,WIN,AI_Game)

    while running:
        clock.tick(60) # constant framerate 
        if cur_game.check_for_winner() != None:
            color = cur_game.check_for_winner()
            color = "RED" if color == RED else "WHITE"
            print("WINNER IS: ", color)
            running = False 
        
        if AI_Game==True and cur_game.currentPlayer==WHITE :
            print("AI game running")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pos()
                row, col = get_index_from_click(click)
                cur_game.select_square(row,col)
                # piece = board.get_piece(row,col)
                # print(piece)
        cur_game.update_ui()
=======
    cur_game = GameLogic(board,WIN)

    if game_option == 0:
        # print("P VS AI NOT IMPLEMENTED YET, quitting")
        # sys.exit(0)
        while running:
            clock.tick(60) # constant framerate 

            if cur_game.check_for_winner() != None:
                color = cur_game.check_for_winner()
                color = "RED" if color == RED else "WHITE"
                print("WINNER IS: ", color)
                running = False 
                break

            if cur_game.currentPlayer == WHITE:
                ## call minmax here on board and get the best move for ai
                cur_game.ai_play_minimax()
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = pygame.mouse.get_pos()
                    row, col = get_index_from_click(click)
                    cur_game.select_square(row,col)
                    # piece = board.get_piece(row,col)
                    # print(piece)
            cur_game.update_ui()
    else:
        while running:
            clock.tick(60) # constant framerate 
            if cur_game.check_for_winner() != None:
                color = cur_game.check_for_winner()
                color = "RED" if color == RED else "WHITE"
                print("WINNER IS: ", color)
                running = False 
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = pygame.mouse.get_pos()
                    row, col = get_index_from_click(click)
                    cur_game.select_square(row,col)
                    # piece = board.get_piece(row,col)
                    # print(piece)
            cur_game.update_ui()
>>>>>>> Stashed changes

    pygame.quit() # close window


if __name__ == "__main__":
    main()
