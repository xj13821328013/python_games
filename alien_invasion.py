# 1.creating a pygame window and responding to user input
# 2.setting the background color


import sys
# use the tools in sys module to exit the game when the player quits
import pygame

class AlienVasion:
    
    # Overall class to manage game assets and behavior
    def __init__(self):
        # Initialize the game, and create game resources
        pygame.init()
        # we call set_mode to create a display window, 1200 pixels wide and 800 pixels high
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # set the background color
        self.bg_color = (230, 230, 230)
    
    def run_game(self):
        # the while loop contains an event loop and code that manages
        # screeen updates
        while True:
            # an event is an action that the user performs while playing the game,
            # such as pressing a key or moving the mouse.
            for event in pygame.event.get():
                # we write this event loop to listen for events and perform appropriate
                # tasks deponding on the kinds of events that occur
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop
            # Each color value can range from 0 to 255. The color value (255, 0, 0) is red, 
            # (0, 255, 0) is green, and (0, 0, 255) is blue.
            self.screen.fill(self.bg_color)
            # tells Pygame to make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # make a game instance, then run the game
    ai = AlienVasion()
    ai.run_game()
    