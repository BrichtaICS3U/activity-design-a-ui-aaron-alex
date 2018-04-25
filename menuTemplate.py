# Pygame Template File
# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
import pygame

pygame.init()

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (242, 100, 25)
BRIGHT_ORANGE = (243, 114, 45)
RED = (234, 53, 70)
BRIGHT_RED = (241,126,137)
BRIGHT_BLUE = (45, 125, 210)
BLUE = (67,188,205)

# Open a new window
 # The window is defined as (width, height), measured in pixels
SCREENWIDTH = 800
SCREENHEIGHT = 600

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Button")

# --- Text elements

# Define text for title of game
#fontTitle = pygame.font.Font('freesansbold.ttf', 32)
#textSurfaceTitle = fontTitle.render('My Awesome Game!', True, BLACK) 
#textRectTitle = textSurfaceTitle.get_rect()
#textRectTitle.center = (100, 150)   # place the centre of the text


# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False

    # Get mouse locationBRIGHT_
    mouse = pygame.mouse.get_pos()
    #print(mouse) # Uncomment to see mouse position in shell

    # Check if mouse is pressed
    click = pygame.mouse.get_pressed()
    #print(click) # Uncomment to see mouse buttons clicked in shell
    
    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(WHITE)

    # Queue shapes to be drawn
    
    # Buttons

    # Green button
    if SCREENWIDTH/2-50 < mouse[0] < SCREENWIDTH/2+50 and SCREENHEIGHT/4 < mouse[1] < SCREENHEIGHT/4 + 50 and click[0] == 1:
        pygame.draw.rect(screen, RED, (SCREENWIDTH/2-50, SCREENHEIGHT/4, 100, 50))
        print('You pressed the button! You maniac!')
    elif SCREENWIDTH/2-50 < mouse[0] < SCREENWIDTH/2+50 and SCREENHEIGHT/4 < mouse[1] < SCREENHEIGHT/4 + 50:
        pygame.draw.rect(screen, ORANGE, (SCREENWIDTH/2-50, SCREENHEIGHT/4, 100, 50))
    else:
        pygame.draw.rect(screen, BRIGHT_ORANGE, (SCREENWIDTH/2-50, SCREENHEIGHT/4, 100, 50))

    # Red button
    if SCREENWIDTH/2-50 < mouse[0] < SCREENWIDTH/2+50 and SCREENHEIGHT*2/4 < mouse[1] < SCREENHEIGHT*2/4 + 50 and click[0] == 1:
        pygame.draw.rect(screen, RED, (SCREENWIDTH/2-50, SCREENHEIGHT*2/4, 100, 50))
        print('You have quit the Game!')
    elif SCREENWIDTH/2-50 < mouse[0] < SCREENWIDTH/2+50 and SCREENHEIGHT*2/4 < mouse[1] < SCREENHEIGHT*2/4 + 50:
        pygame.draw.rect(screen, BRIGHT_RED, (SCREENWIDTH/2-50, SCREENHEIGHT*2/4, 100, 50))
    else:
        pygame.draw.rect(screen, RED, (SCREENWIDTH/2-50, SCREENHEIGHT*2/4, 100, 50))
        
    # Blue button
    if SCREENWIDTH/2-50 < mouse[0] < SCREENWIDTH/2+50 and SCREENHEIGHT*3/4 < mouse[1] < SCREENHEIGHT*3/4 + 50 and click[0] == 1:
        pygame.draw.rect(screen, BLUE, (SCREENWIDTH/2-50, SCREENHEIGHT*3/4, 100, 50))
        print('You have paused the game!')
    elif SCREENWIDTH/2-50 < mouse[0] < SCREENWIDTH/2+50 and SCREENHEIGHT*3/4 < mouse[1] < SCREENHEIGHT*3/4 + 50:
        pygame.draw.rect(screen, BRIGHT_BLUE, (SCREENWIDTH/2-50, SCREENHEIGHT*3/4, 100, 50))
    else:
        pygame.draw.rect(screen, BLUE, (SCREENWIDTH/2-50, SCREENHEIGHT*3/4, 100, 50))

    # Text
    #screen.blit(textSurfaceTitle, textRectTitle)

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
