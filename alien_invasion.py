# 1. creating a pygame window and responding to user input
# 2. setting the background color
# 3. creating a setting class
# 4. Adding the Ship Image
# 5. Create the ship class
# 6. drawing the ship to the screen 
# 7. Refactor: the _check_events() and _update_screen() Methods
# 8. ploting the ship -- responding to the keypress
# 9. Allowing Continuous Movement
# 10. Moving Both Left and Right
# 11. Adjusting the Ship’s Speed
# 12. Limiting the Ship’s Range
# 13. Pressing Q to Quit
# 14. Running the Game in Fullscreen Mode

from re import S
import sys
# use the tools in sys module to exit the game when the player quits
import pygame

from settings import Settings
from ship import Ship

class AlienVasion:
    
    # Overall class to manage game assets and behavior
    def __init__(self):
        # Initialize the game, and create game resources
        pygame.init()
        # Then we create an instance of Settings and assign it to self.settings
        self.settings = Settings()
        # we call set_mode to create a display window, 1200 pixels wide and 800 pixels high
        # self.screen = pygame.display.set_mode((1200, 800))

        # Make sure you can quit by pressing Q before running the game in fullscreen mode; 
        # Pygame offers no default way to quit a game while in fullscreen mode.
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # set the background color
        # self.bg_color = (230, 230, 230)

        # The call to Ship() requires one argument, an instance of AlienInvasion.
        self.ship = Ship(self)
    
    def run_game(self):
        # the while loop contains an event loop and code that manages
        # screeen updates
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        # an event is an action that the user performs while playing the game,
        # such as pressing a key or moving the mouse.
        for event in pygame.event.get():
            # we write this event loop to listen for events and perform appropriate
            # tasks deponding on the kinds of events that occur
            if event.type == pygame.QUIT:
                sys.exit()
            
            # moving_right is set to True when the right arrow key is pressed and False when the key is released
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit() 
        
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        # Redraw the screen during each pass through the loop
        # Each color value can range from 0 to 255. The color value (255, 0, 0) is red, 
        # (0, 255, 0) is green, and (0, 0, 255) is blue.
        self.screen.fill(self.settings.bg_color)

        self.ship.blitme()
        # tells Pygame to make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    # make a game instance, then run the game
    ai = AlienVasion()
    ai.run_game()
    
