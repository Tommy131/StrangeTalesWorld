'''
       _____   _          __  _____   _____   _       _____   _____
     /  _  \ | |        / / /  _  \ |  _  \ | |     /  _  \ /  ___|
     | | | | | |  __   / /  | | | | | |_| | | |     | | | | | |
     | | | | | | /  | / /   | | | | |  _  { | |     | | | | | |   _
     | |_| | | |/   |/ /    | |_| | | |_| | | |___  | |_| | | |_| |
     \_____/ |___/|___/     \_____/ |_____/ |_____| \_____/ \_____/

Copyright (c) 2023 by OwOTeam-DGMT (OwOBlog).
Date         : 2024-07-20 17:43:30
Author       : HanskiJay
LastEditors  : HanskiJay
LastEditTime : 2024-07-23 00:52:36
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''
# player.py

import pygame

from entity.entity import Entity
from utils.settings import Settings

class Player(Entity):
    def __init__(self, name='Player'):
        super().__init__(name, damage=1)

    def draw(self, surface):
        super().draw(surface)
        self.draw_health_bar(surface)

    def move(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
            self.last_direction = Settings.LEFT

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed
            self.last_direction = Settings.RIGHT

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed
            self.last_direction = Settings.UP

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed
            self.last_direction = Settings.DOWN

        # 玩家移速判断
        if keys[pygame.K_LSHIFT]:
            self.speed = self.MAX_SPEED
        else:
            self.speed = self.SPEED

        super().move()
