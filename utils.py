import pygame
from ui_consts import EACH_SQUARE, W,H,RED,WHITE,BLACK
# get the row and column index from mouse click
def get_index_from_click(click):
    x_cord, y_cord = click
    row = y_cord // EACH_SQUARE
    col = x_cord // EACH_SQUARE

    return int(row), int(col)


