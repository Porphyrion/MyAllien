import pygame
import sys
import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Allien  Invasion")
    ship = Ship(screen)

    while True:
        # gf.check_events(ship)
        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.rect.centerx += 10

                elif event.key == pygame.K_LEFT:
                    ship.rect.centerx -= 10

                elif event.key == pygame.K_DOWN:
                    ship.rect.centery -= 10

                elif event.key == pygame.K_SPACE:
                    ship.rect.centerx += 10

        gf.update_screen(ai_settings, screen, ship)


run_game()
