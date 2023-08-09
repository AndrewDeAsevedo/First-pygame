import pygame
import os


WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game :D")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BORDER = pygame.Rect(445, 0, 10, HEIGHT)

# Used to determine FPS, peep the clock variable and the clock.tick
FPS = 60
VEL = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

# Making sprites
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join( 'Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join( 'Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (
    SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 270)

# NoTE: Order matters, fill in background first, then sprites
def draw_window(red, yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    # Blit draws a surface onto the screen WIN.blit(image, position)
    # Note about positioning, 0,0 is top left of screen, not center
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
 # How to get keys pressed
        if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: # Left
            yellow.x -= VEL
        if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: # Right
            yellow.x += VEL
        if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # Up
            yellow.y -= VEL
        if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15: # Down
            yellow.y += VEL

def red_handle_movement(keys_pressed, red):
 # How to get keys pressed
        if keys_pressed[pygame.K_LEFT]: # Left
            red.x -= VEL
        if keys_pressed[pygame.K_RIGHT]: # Right
            red.x += VEL
        if keys_pressed[pygame.K_UP]: # Up
            red.y -= VEL
        if keys_pressed[pygame.K_DOWN]: # Down
            red.y += VEL

# This code is so that when you click the x, it exits.
# Good practice is to draw your screen in a different function so you just call it in main
def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    # This code creates a rectangle on previous space ships, with the x and y position then you specify its height and width

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)



        ##everytime this loop happens, it is going to draw window
        draw_window(red, yellow)

    # Once out of the while loop, quit, usually last line of code
    pygame.quit()


# This is that code that makes it so you dont call the file if its not the main one (remember from CS110)
if __name__ == "__main__":
    main()