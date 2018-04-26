# Menu template with button class and basic menu navigation
# Adapted from http://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/

import pygame, sys
pygame.init()

# Define some colours
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

SCREENWIDTH = 800
SCREENHEIGHT = 600
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

class Button():
    """This is a class for a generic button.
    
       txt = text on the button
       location = (x,y) coordinates of the button's centre
       action = name of function to run when button is pressed
       bg = background colour (default is white)
       fg = text colour (default is black)
       size = (width, height) of button
       font_name = name of font
       font_size = size of font
    """
    def __init__(self, txt, location, action, bg=WHITE, fg=BLACK, size=(80, 30), font_name="Segoe Print", font_size=16):
        self.color = bg  # the static (normal) color
        self.bg = bg  # actual background color, can change on mouseover
        self.fg = fg  # text color
        self.size = size

        self.font = pygame.font.SysFont(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])

        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center=location)

        self.call_back_ = action

    def draw(self):
        self.mouseover()

        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surface, self.rect)

    def mouseover(self):
        """Checks if mouse is over button using rect collision"""
        self.bg = self.color
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.bg = GRAY  # mouseover color

    def call_back(self):
        """Runs a function when clicked"""
        self.call_back_()

def my_shell_function():
    """A generic function that prints something in the shell"""
    print('Fire the nukes!')

def my_next_function():
    """A function that advances to the next level"""
    global level
    level += 1

def my_previous_function():
    """A function that retreats to the previous level"""
    global level
    level -= 1

def my_quit_function():
    """A function that will quit the game and close the pygame window"""
    pygame.quit()
    sys.exit()

def mousebuttondown(level):
    """A function that checks which button was pressed"""
    pos = pygame.mouse.get_pos()
    if level == 1:
        for button in level1_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 2:
        for button in level2_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()

level = 1
carryOn = True
clock = pygame.time.Clock()

#create button objects
button_01 = Button("Next", (SCREENWIDTH/2, SCREENHEIGHT/3), my_next_function)
button_02 = Button("Previous", (SCREENWIDTH/2, SCREENHEIGHT/3), my_previous_function)
button_03 = Button("Quit", (SCREENWIDTH/2, SCREENHEIGHT*2/3), my_quit_function, bg=(50, 200, 20))

#arrange button groups depending on level
level1_buttons = [button_01, button_03]
level2_buttons = [button_02, button_03]

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # Player clicked the mouse
            mousebuttondown(level)

    # --- Game logic goes here

    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(WHITE)

    # Draw buttons
    if level == 1:
        for button in level1_buttons:
            button.draw()
    elif level == 2:
        for button in level2_buttons:
            button.draw()

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()


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

fontTitle = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceTitle = fontTitle.render('My Awesome Game!', True, BLACK) 
textRectTitle = textSurfaceTitle.get_rect()
textRectTitle.center = (100, 150)   # place the centre of the text


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
