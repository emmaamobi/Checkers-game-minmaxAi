import pygame

# UI variables 
w,h = 720, 720
each_square = w / 8 # divide width by number of rows or cols
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

# initialize window
WIN = pygame.display.set_mode((w,h))
pygame.display.set_caption('checkers minmax')



# runner
def main():
    running = True
    clock = pygame.time.Clock()
    while running:
        clock.tick(60) # constant framerate 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

    pygame.quit() # close window


if __name__ == "__main__":
    main()
