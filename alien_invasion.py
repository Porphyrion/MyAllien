import pygame
import sys
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from logo import Logo


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(screen)  # создание кнопки PLAY
    logo = Logo(screen)
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    bombs = Group()
    ship = Ship(ai_settings, screen)  # создание корабля
    aliens = Group()  # создание вторжения
    bullets = Group()  # создаем пули
    gf.create_fleet(ai_settings, screen, ship, aliens)  # создаем флот

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, logo)
        gf.update_screen(ai_settings, screen, stats, sb, ship, bullets, aliens, play_button, logo, bombs)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, bombs)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
            gf.update_bomb(ai_settings, screen, stats, sb, ship, aliens, bullets, bombs)

run_game()
