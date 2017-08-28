import sys
import pygame


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True

            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

            elif event.key == pygame.K_SPACE:
                ship.rect.centery -= 40

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.big_color)
    ship.blitme()
    pygame.display.flip()
