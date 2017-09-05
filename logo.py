import pygame

class Logo:

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image_alien = pygame.image.load('images/alien.bmp')
        self.image_invasion = pygame.image.load('images/invasion.bmp')

        self.alien_rect = self.image_alien.get_rect()
        self.invasion_rect = self.image_alien.get_rect()

        self.height = self.alien_rect.height + self.invasion_rect.height + 30
        self.width = self.invasion_rect.width + 40

        self.invasion_rect.top = self.screen_rect.top
        self.invasion_rect.centerx = self.screen_rect.centerx
        self.alien_rect.top = self.invasion_rect.bottom
        self.alien_rect.centerx = self.screen_rect.centerx

        # print(self.rect.height, self.alien_rect.height, self.invasion_rect.height)

    def draw_logo(self):
        self.screen.blit(self.image_alien, self.alien_rect)
        self.screen.blit(self.image_invasion, self.invasion_rect)




