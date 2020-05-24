import pygame
import random

pygame.init()

win = pygame.display.set_mode((1000,800))
pygame.display.set_caption("First Game")

font = pygame.font.Font('Naughty_Cartoons.ttf', 16)
introtext = pygame.font.Font('Naughty_Cartoons.ttf', 115)

#player/white blood cell code
#Starting position in the bottom left
x = 0
y = 800
width = 100
height = 100
vel = 2
virusHeight = 50
virusWidth = 50

run = True

score = 100
score_value = 0
scoreX = 100
scoreY = 100

boardX = 10
boardY = 990

def show_score(x,y):
    score = font.render("Score: "+ str(score_value), True, (255,255,255))
    win.blit(score,(x,y))

## Three Things TO DO:
#1. Enemy collision
#2. Enemy Spawn
#3. Enemy Respawning

#virus code to create many viruses
virusImg = []
virusX = []
virusY = []
virusY_change = []
virusX_change = []
num_of_virus = 3

for i in range(num_of_virus):
    virusImg.append(pygame.image.load("virus.png"))
    virusImg[i] = pygame.transform.scale(virusImg, (virusWidth, virusHeight))
    virusX[i]=random.randint(100,900)
    virusY[i]=random.randint(50,150)
    virusY_change.append(random.randint(1,10))
    virusX_change.append(random.randint(1,10))

#white bloodcells
whiteImg = pygame.image.load("cell.png")
whiteImg = pygame.transform.scale(whiteImg, (width, height))
#Positive Y direction = moving downward.
#Sets the downward velocity of the virus

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

    #Shows the score
    show_score(scoreX,scoreY)
    # This updates the screen so we can see our rectangle
    pygame.display.update()

#End loop
pygame.quit()  # If we exit the loop this will execute and close our game

#IMages from Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
