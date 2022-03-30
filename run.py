import pygame
from board import Board
from ui_consts import W, H

# UI variables 
w,h = 720, 720
each_square = w / 8 # divide width by number of rows or cols to get square size
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

# initialize window
WIN = pygame.display.set_mode((W,H))
pygame.display.set_caption('checkers minmax')



# runner
def main():
    running = True
    clock = pygame.time.Clock()
    board = Board()

    while running:
        clock.tick(60) # constant framerate 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        board.draw_board(WIN)
        pygame.display.update()

    pygame.quit() # close window


if __name__ == "__main__":
    main()