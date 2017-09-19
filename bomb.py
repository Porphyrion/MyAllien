import pygame
from pygame.sprite import Sprite


class Bomb(Sprite):

    def __init__(self, ai_settings, screen, alien):
        super(Bomb, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("images/bomb.bmp")

        self.rect = self.image.get_rect()
        self.rect.centerx = alien.rect.centerx
        self.rect.top = alien.rect.top

        self.shooting_sound = pygame.mixer.Sound("sounds/pew.wav")

        self.y = float(self.rect.y)

        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        self.y += self.speed_factor
        self.rect.y = self.y

    def draw_bomb(self):
        pygame.draw.rect(self.screen, self.rect)






