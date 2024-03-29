import sys

# use the tools in sys module to exit the game when the player quits
import pygame
from bullet import Bullet

from settings import Settings
from ship import Ship
from alien import Alien

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
        # the group automatically calls update() for each sprite in the group
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
    
    def run_game(self):
        # the while loop contains an event loop and code that manages
        # screeen updates, The main loop of the game, a while loop
        while True: 
            self._check_events()
            self.ship.update()
            # The line self.bullets.update() calls bullet.update() for each bullet we place in the group bullets.
            # Now our main loop contains only minimal code, so we can quickly read the method names and understand what’s happening in the game.
            self._update_bullets()
            self._update_aliens()
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
            # print("ready to move left")
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            # print("ready to fire")
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit() 
        
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            #  The add() method is similar to append(), but it’s a method that’s written spe­ cifically for Pygame groups.
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """ Update position of bullets and get rid of old bullets. write the purpose of each function"""
        # Update bullet positions.
        self.bullets.update()
            
        # Get rid of bullets that have disappeared.
        # Because we can’t remove items from a list or group within a for loop, we have to loop over a copy of the group
        # We use the copy() method to set up the for loopu, which enables us to modify bullets inside the loopclear
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))
    
    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        alien_height = alien.rect.height
        ship_height = self.ship.rect.height
        # The result will create some empty space above the ship, so the player has some time 
        # to start shooting aliens at the beginning of each level.
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)
        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(row_number, alien_number)
            
    def _create_alien(self, row_number, alien_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.y = alien_height + 2 * alien_height * row_number
        alien.rect.x = alien.x
        self.aliens.add(alien)
    
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges() == True:
                # print("check edges")
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        """
            Check if the fleet is at an edge,
            then update the positions of all aliens in the fleet.
        """
        self._check_fleet_edges()
        self.aliens.update()

    def _update_screen(self):
        # Redraw the screen during each pass through the loop
        # Each color value can range from 0 to 255. The color value (255, 0, 0) is red, 
        # (0, 255, 0) is green, and (0, 0, 255) is blue.
        self.screen.fill(self.settings.bg_color)

        self.ship.blitme()
        # We also need to modify _update_screen() to make sure each bullet is drawn to the screen before we call flip().
        for bullet in self.bullets.sprites(): 
        # The bullets.sprites() method returns a list of all sprites in the group bullets.
            bullet.draw_bullet()
        # tells Pygame to make the most recently drawn screen visible
        # When you call draw() on a group, Pygame draws each element in the group at the position defined by its rect attribute.
        # self.aliens.update()
        self.aliens.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    # make a game instance, then run the game
    ai = AlienVasion()
    ai.run_game()
    
