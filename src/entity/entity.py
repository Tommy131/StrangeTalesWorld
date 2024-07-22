'''
       _____   _          __  _____   _____   _       _____   _____
     /  _  \ | |        / / /  _  \ |  _  \ | |     /  _  \ /  ___|
     | | | | | |  __   / /  | | | | | |_| | | |     | | | | | |
     | | | | | | /  | / /   | | | | |  _  { | |     | | | | | |   _
     | |_| | | |/   |/ /    | |_| | | |_| | | |___  | |_| | | |_| |
     \_____/ |___/|___/     \_____/ |_____/ |_____| \_____/ \_____/

Copyright (c) 2023 by OwOTeam-DGMT (OwOBlog).
Date         : 2024-07-21 02:08:40
Author       : HanskiJay
LastEditors  : HanskiJay
LastEditTime : 2024-07-23 01:40:19
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''
# entity.py

import pygame

from utils.settings import Settings
from vector import Vector

class Entity:
    NAME = 'Entity'
    SIZE = 50
    SPEED = 5
    MAX_SPEED = 10
    HEALTH = 100
    DAMAGE = 0
    COLOR = (0, 255, 0)

    def __init__(self, name=NAME, size=SIZE, speed=SPEED, max_speed=MAX_SPEED, health=HEALTH, max_health=HEALTH, damage=DAMAGE, color=COLOR):
        """
        初始化实体对象

        :param name: 实体名称, 默认为 'Entity'
        :param size: 实体大小, 默认为 50
        :param speed: 实体速度, 默认为 5
        :param max_speed: 实体最大速度, 默认为 10
        :param health: 实体生命值, 默认为 100
        :param max_health: 实体最大生命值, 默认为 100
        :param damage: 实体伤害值, 默认为 0
        :param color: 实体颜色, 默认为 (0, 255, 0)
        """
        self.name = name
        self.size = size
        self.speed = speed
        self.max_speed = max_speed
        self.health = health
        self.max_health = max_health
        self.damage = damage
        self.color = color
        self.vector = Vector()

        # attack
        self.attack_flash_time = 0
        self.attack_flashing = False

        # 血条
        self.can_display_health_bar = False

    def set_size(self, size):
        """
        设置实体的大小

        :param size: 实体的新大小
        :return: 当前实体对象
        """
        self.size = size
        return self

    def set_speed(self, speed):
        """
        设置实体的速度

        :param speed: 实体的新速度
        :return: 当前实体对象
        """
        self.speed = speed
        return self

    def set_max_speed(self, max_speed):
        """
        设置实体的最大速度

        :param max_speed: 实体的新最大速度
        :return: 当前实体对象
        """
        self.max_speed = max_speed
        return self

    def set_health(self, health):
        """
        设置实体的生命值

        :param health: 实体的新生命值
        :return: 当前实体对象
        """
        self.health = health
        return self

    def get_vector(self):
        """
        获取实体的向量对象

        :return: 实体的向量对象
        """
        return self.vector

    def is_alive(self):
        """
        检查实体是否存活

        :return: 布尔值, 表示实体是否存活
        """
        return self.health > 0

    def is_speed_valid(self):
        """
        检查实体的速度是否在有效范围内

        :return: 布尔值, 表示速度是否有效
        """
        return 0 <= self.speed <= self.max_speed

    def move(self):
        """
        移动实体, 并限制实体在屏幕内移动
        """
        self.vector.x = max(0, min(self.vector.x, Settings.SCREEN_WIDTH - self.size))
        self.vector.y = max(0, min(self.vector.y, Settings.SCREEN_HEIGHT - self.size))

    def update_position(self):
        """
        更新实体的位置, 确保其不超出屏幕边界
        """
        if self.vector.x < 0:
            self.vector.x = 0
        if self.vector.x > Settings.SCREEN_WIDTH - self.size:
            self.vector.x = Settings.SCREEN_WIDTH - self.size
        if self.vector.y < 0:
            self.vector.y = 0
        if self.vector.y > Settings.SCREEN_HEIGHT - self.size:
            self.vector.y = Settings.SCREEN_HEIGHT - self.size

    def draw_header_info(self, screen):
        """
        绘制实体的头部信息, 包括名称和生命值条

        :param screen: 游戏窗口, 用于绘制实体的信息
        """
        font = pygame.font.Font(None, 24)
        name_text = font.render(self.name, True, Settings.WHITE)
        screen.blit(name_text, (self.vector.x, self.vector.y - 30))

        if self.can_display_health_bar:
            bar_width = 50
            bar_height = 5
            health_percentage = self.health / self.max_health
            health_bar_width = bar_width * health_percentage
            # 血量条背景
            pygame.draw.rect(screen, (255, 0, 0), (self.vector.x, self.vector.y - 10, bar_width, bar_height))
            # 血量条前景
            pygame.draw.rect(screen, (0, 255, 0), (self.vector.x, self.vector.y - 10, health_bar_width, bar_height))

    def draw(self, screen):
        """
        绘制实体, 包括头部信息和实体本身

        :param screen: 游戏窗口, 用于绘制实体
        """
        self.draw_header_info(screen)

        current_time = pygame.time.get_ticks()
        if self.attack_flashing and current_time - self.attack_flash_time < 3000:
            if ((current_time // 100) % 2 == 0):
                self._draw(screen)
                self.draw_weapon(screen)
        else:
            self._draw(screen)
            self.draw_weapon(screen)
            self.attack_flashing = False

    def _draw(self, screen):
        """
        绘制实体本身 (矩形)

        :param screen: 游戏窗口, 用于绘制实体
        """
        if self.color:
            pygame.draw.rect(screen, self.color, (*self.vector.get_pos(), self.size, self.size))
