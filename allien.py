import pygame
from pygame.sprite import Sprite
from random import randint


class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        image_type = randint(0, 1)

        self.bomb = False

        if image_type:
            self.image = pygame.image.load("images/ufo.bmp")
        else:
            self.image = pygame.image.load("images/ufo2.bmp")
        self.rect = self.image.get_rect()

        self.health = 1

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


class SecondAlien(Alien):

    def __init__(self, ai_settings, screen):
        super(SecondAlien, self).__init__(ai_settings, screen)
        self.image = pygame.image.load("images/ufo3.bmp")
        self.health = 2
        self.bomb = True


class DevilAlien(Alien):

    def __init__(self, ai_settings, screen):
        super(DevilAlien, self).__init__(ai_settings, screen)
        self.image = pygame.image.load("images/ufo4.bmp")
        self.health = 3
        self.bomb = True


class HtonAlien(Alien):

    def __init__(self, ai_settings, screen):
        super(HtonAlien, self).__init__(ai_settings, screen)
        self.image = pygame.image.load("images/ufo5.bmp")
        self.health = 5
        self.bomb = True






