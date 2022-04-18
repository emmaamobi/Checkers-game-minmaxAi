import pygame
from ui_consts import W, H
from utils import get_index_from_click
from gameLogic import GameLogic
from board import Board
from ui_consts import EACH_SQUARE, W,H,RED,WHITE,BLACK,BLUE,GOLD

# initialize window
WIN = pygame.display.set_mode((W,H))
pygame.display.set_caption('checkers minmax')



# runner
def main():
    # AI_Game=False
    print("WELCOME TO CHECKERS GAME")
    game_option = int(input("SELECT '1' for P v P, or '0' for P v AI: "))
    print("Starting game \n")
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
    cur_game = GameLogic(board,WIN)

    if game_option == 0:
        while running:
            clock.tick(60) # constant framerate 

            if cur_game.currentPlayer == WHITE:
                ## call minmax here on board and get the best move for ai
                game.ai_make_move()
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

    pygame.quit() # close window


if __name__ == "__main__":
    main()
