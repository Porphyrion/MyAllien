import pygame

class Logo:

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image_alien = pygame.image.load('images/alien.bmp')
        self.image_invasion = pygame.image.load('images/invasion.bmp')

        self.alien_rect = self.image_alien.get_rect()
        self.invasion_rect = self.image_invasion.get_rect()

        # self.height = self.alien_rect.height + self.invasion_rect.height + 30
        # self.width = self.invasion_rect.width + 40

        self.alien_rect.top = self.screen_rect.top + 1
        self.alien_rect.centerx = self.screen_rect.centerx
        self.invasion_rect.top = self.invasion_rect.bottom + 20
        self.invasion_rect.centerx = self.screen_rect.centerx

        self.speed_factor = 2

        self.sound_logo = pygame.mixer.music
        self.sound_logo.load('sounds/alien_batman.mp3')
        self.sound_logo.play()
        self.sound_trigger = True

        # print(self.invasion_rect.width, self.alien_rect.width)
        # print(self.rect.height, self.alien_rect.height, self.invasion_rect.height)

    def draw_logo(self):
        self.screen.blit(self.image_alien, self.alien_rect)
        self.screen.blit(self.image_invasion, self.invasion_rect)
        if (self.alien_rect.top < self.screen_rect.top) or (self.invasion_rect.bottom > self.screen_rect.bottom):
            self.speed_factor *= -1
            # print("tut")
        self.update_logo()

    def update_logo(self):
        self.alien_rect.y += self.speed_factor
        self.invasion_rect.y += self.speed_factor

    def sound_off(self):
        self.sound_trigger = False
        self.sound_logo.pause()




