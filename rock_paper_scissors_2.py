# import packages
import pygame
from pygame.locals import *
from AnimalButton import *
import sys

# define constants
background_color = ("#90EE90")
window_width = "100%"
window_height = "100%"
frames_per_second = 30

# initialize the world
pygame.init()
window = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

# load assets: images(s), sounds, etc.

# initialize variables

# create an instance of SimpleButton - we will rename to AnimalButton
objectButton = AnimalButton(window, (75, 80),
                            'images/buttonUp.png',
                            'images/buttonDown.png')

# loop forever
while True:

    # check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # pass the event to the button
        if objectButton.handleEvent(event):
            print('User has clicked the button.')

    # do any "per frame" actions

    # clear the window
    window.fill(background_color)