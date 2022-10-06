import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    # The Bullet class inherits from Sprite
    """A class to manage bullets fired from the ship"""
    def __init__(self, ai_game):
        
        """Create a bullet object at the ship's current position."""
        # To create a bullet instance, __init__() needs the current instance of AlienInvasion, 
        # and we call super() to inherit properly from Sprite
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        # we have to build a rect from scratch using the pygame.Rect() class
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,self.settings.bullet_height)
        #  we set the bullet’s midtop attribute to match the ship’s midtop attri­ bute. 
        # This will make the bullet emerge from the top of the ship
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a decimal value.
        # We store a decimal value for the bullet’s y­coordinate so we can make fine adjustments to the bullet’s speed
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        self.y -= self.settings.bullet_speed
        # Update the decimal position of the bullet.
        
        # Update the rect position.
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

