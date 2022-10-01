from this import d
import pygame

class Ship:
    # A class to manage the ship

    def __init__(self, ai_game):
        # initialize the ship and set its starting position

        # we assign the screen to an attribute of Ship, so we can access it easily in all the methods in this class
        self.screen = ai_game.screen

        # we access the screen’s rect attribute using the get_rect() method and assign it to self.screen_rect. Doing so allows us to place the ship in the correct location on the screen.
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        # draw the ship at its current location.
        # we define the blitme() method, which draws the image to the screen at the position specified by self.rect.
        self.screen.blit(self.image, self.rect)
