import pygame
import random

pygame.init()

win = pygame.display.set_mode((1000,800))
pygame.display.set_caption("First Game")

#player/white blood cell code
#Starting position in the bottom left
x = 0
y = 0
width = 100
height = 100
vel = 1

run = True

#score
#score_value = 0
#font = pygame.font.Font("comicsansms",10)
boardX = 10
boardY = 990
def show_score(x,y):
    score = font.render("Score: "+ str(score_value), True, (255,255,255))
    screen.blit(score,(x,y))



#virus code
virusImg = pygame.image.load("virus.png")
virusImg = pygame.transform.scale(virusImg, (50, 50))
virusX = random.randint(100,900)
virusY = random.randint(50,150)
#white bloodcells
whiteImg = pygame.image.load("cell.png")
whiteImg = pygame.transform.scale(whiteImg, (width, height))
#Positive Y direction = moving downward.
#Sets the downward velocity of the virus
virusY_change = 1

def virus(x, y):
    win.blit(virusImg, (x, y))

while run:
    pygame.time.delay(7) # This will delay the game the given amount of milliseconds. In our casee 0.1 seconds will be the delay
    show_score(boardX,boardY)
    #Ends game when window is closed
    for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
        if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
            run = False  # Ends the game loop

    #Moves the red rectangle when arrowkeys are pressed
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 1000 - width - vel:
        x += vel
    if keys[pygame.K_UP] and y > vel:
        y -= vel
    if keys[pygame.K_DOWN] and y < 800 - height - vel:
        y += vel


    #Adds background
    win.fill((0,0,0))

    win.blit(whiteImg, (x,y))
    #pygame.draw.rect(win, (255,0,0), (x, y, width, height))  #This takes: window/surface, color, rect

    #Draw virus image
    virus(virusX, virusY)

    #Moves the virus Right
    virusY +=virusY_change
    # This updates the screen so we can see our rectangle
    pygame.display.update()

#End loop
pygame.quit()  # If we exit the loop this will execute and close our game

#IMages from Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
