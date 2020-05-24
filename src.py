import pygame
import random

pygame.init()

win = pygame.display.set_mode((1000,800))
pygame.display.set_caption("First Game")

x = 0
y = 0
width = 50
height = 50
vel = 1

run = True

virusImg = pygame.image.load("virus.png")
virusImg = pygame.transform.scale(virusImg, (50, 50))
virusX = random.randint(100,900)
virusY = random.randint(50,150)
virusX_change = 1

def virus(x, y):
    win.blit(virusImg, (x, y))

while run:
    pygame.time.delay(7) # This will delay the game the given amount of milliseconds. In our casee 0.1 seconds will be the delay

    #Ends game when window is closed
    for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
        if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
            run = False  # Ends the game loop

    #Moves the red rectangle when arrowkeys are pressed
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel

    #Adds background
    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))  #This takes: window/surface, color, rect

    #Draw
    virus(virusX, virusY)

    virusX +=virusX_change

    pygame.display.update() # This updates the screen so we can see our rectangle

#End loop
pygame.quit()  # If we exit the loop this will execute and close our game

#IMages from Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
