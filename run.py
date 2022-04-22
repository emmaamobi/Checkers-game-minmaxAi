import pygame
from ui_consts import W, H
from utils import get_index_from_click
from gameLogic import GameLogic
from board import Board
from ui_consts import EACH_SQUARE, W,H,RED,WHITE,BLACK,BLUE,GOLD
import PySimpleGUI as sg
import sys

def display_winner(winner):
    layout = [[sg.Text("WINNER IS {}!!".format(winner))]]
    window = sg.Window("WINNER MESSAGE", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()


def getUserOption():
    options = ['PvP','PvAI']

    # All the stuff inside your window.
    layout = [ 
                [sg.Text('Select one->'), sg.Listbox(options,select_mode=sg.LISTBOX_SELECT_MODE_SINGLE,size=(20,len(options)))],
                [sg.Button('Ok'), sg.Button('Cancel')]
            ]

    # Create the Window
    window = sg.Window('SELECT GAME MODE', layout)

    # Event Loop to process "events" and get the "values" of the input
    while True:
        event, values = window.read()
        print( f"event={event}" )
        if event is None or event == 'Ok' or event == 'Cancel': # if user closes window or clicks cancel
            break
            
    # close  the window        
    window.close()

    return values[0]


# runner
def main():
    ans = getUserOption()
    game_option = 1 if ans == ['PvP'] else 0
    # initialize window
    WIN = pygame.display.set_mode((W,H))
    pygame.display.set_caption('checkers minmax')
    # AI_Game=False
    # print("WELCOME TO CHECKERS GAME")
    # game_option = int(input("SELECT '1' for P v P, or '0' for P v AI: "))
    # print("Starting game \n")
            
    
    running = True
    clock = pygame.time.Clock()
    board = Board()
    cur_game = GameLogic(board,WIN)
    winner = "TIE"

    if game_option == 0:
        # print("P VS AI NOT IMPLEMENTED YET, quitting")
        # sys.exit(0)
        while running:
            clock.tick(60) # constant framerate 

            if cur_game.check_for_winner() != None:
                winner = cur_game.check_for_winner()
                winner = "RED" if winner == RED else "WHITE"
                print("WINNER IS: ", winner)
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
                winner = cur_game.check_for_winner()
                winner = "RED" if winner == RED else "WHITE"
                print("WINNER IS: ", winner)
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
    display_winner(winner)


if __name__ == "__main__":
    main()
