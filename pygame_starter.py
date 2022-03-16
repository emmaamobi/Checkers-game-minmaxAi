import pygame
from pygame.locals import *

# Initialization
pygame.init()
timer = pygame.time.Clock()
window = pygame.display.set_mode( ( 300 , 300 ) )
pygame.display.set_caption( "Testing out PyGame!" )

# Game loop
done = False
while done == False:

    # Check input
    for event in pygame.event.get():
        if ( event.type == QUIT ):
            done = True

    # Update screen
    pygame.display.update()
    timer.tick( 30 )
