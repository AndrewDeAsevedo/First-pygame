import pygame
import os


WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game :D")

WHITE = (255, 255, 255)

# Used to determine FPS, peep the clock variable and the clock.tick
FPS = 60

# Making sprites
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('first game', 'Assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('first game', 'Assets', 'spaceship_red.png'))

# NoTE: Order matters, fill in background first, then sprites
def draw_window():
    WIN.fill(WHITE)
    # Blit draws a surface onto the screen WIN.blit(image, position)
    # Note about positioning, 0,0 is top left of screen, not center
    WIN.blit(YELLOW_SPACESHIP_IMAGE, (300, 100))
    pygame.display.update()


# This code is so that when you click the x, it exits.
# Good practice is to draw your screen in a different function so you just call it in main
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            ##everytime this loop happens, it is going to draw window
            draw_window()

    # Once out of the while loop, quit, usually last line of code
    pygame.quit()


# This is that code that makes it so you dont call the file if its not the main one (remember from CS110)
if __name__ == "__main__":
    main()