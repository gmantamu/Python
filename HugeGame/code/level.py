import pygame
from settings import *

class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # sprite group setup
        self.all_sprites = pygame.sprite.Group()

    def run(self,dt):
        # update and draw the game
        self.dispaly_surfact.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update()
