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
    sound_logo = pygame.mixer.music
    sound_logo.load('sounds/alien_batman.mp3')
    sound_logo.play()
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)  # создание корабля
    aliens = Group()  # создание вторжения
    bullets = Group()  # создаем пули
    gf.create_fleet(ai_settings, screen, ship, aliens)  # создаем флот

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, bullets, aliens, play_button, logo)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
            # gf.update_screen(ai_settings, screen, stats, ship, bullets, aliens, play_button)

run_game()
