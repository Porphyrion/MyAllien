import sys
import pygame


def check_events(ship):
    for event in pygame.event.get():
        ship.rect.centery -= 10
        ship.rect.centerx += 10
        # if event.type == pygame.QUIT:
        #    sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.rect.centerx += 10

            elif event.key == pygame.K_LEFT:
                ship.rect.centerx -= 10

            elif event.key == pygame.K_DOWN:
                ship.rect.centery -= 10

            elif event.key == pygame.K_SPACE:
                ship.rect.centerx += 10


def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.big_color)
    ship.blitme()
    pygame.display.flip()

