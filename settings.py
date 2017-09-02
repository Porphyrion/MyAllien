class Settings:

    def __init__(self):
        self.screen_width = 900
        self.screen_height = 650

        self.big_color = (230, 230, 230)
        self.ship_speed_factor = 5
        self.ship_limit = 3

        self.bullet_speed_factor = 3
        self.bullet_allowed = 3

        self.alien_speed_factor = 20
        self.fleet_drop_speed = 10
        self.fleet_direction = 1    # 1 - движение вправо, -1 влево

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        # self.aliens_point = 10

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 4
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 5

        self.fleet_direction = 1

        self.aliens_point = 10

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.aliens_point *= int(self.aliens_point * self.score_scale)












