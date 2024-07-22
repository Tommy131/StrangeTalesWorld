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
LastEditTime : 2024-07-22 18:06:44
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
        self.name = name
        self.size = size
        self.speed = speed
        self.max_speed = max_speed
        self.health = health
        self.max_health = max_health
        self.damage = damage
        self.color = color
        self.flash_time = 0
        self.flashing = False
        self.vector = Vector()

    # 设置实体大小
    def set_size(self, size):
        self.size = size
        return self

    # 设置实体移速
    def set_speed(self, speed):
        self.speed = speed
        return self

    # 设置实体最大移速
    def set_max_speed(self, max_speed):
        self.max_speed = max_speed
        return self

    # 设置实体生命值
    def set_health(self, health):
        self.health = health
        return self

    # 获取实体向量
    def get_vector(self):
        return self.vector

    # 检查实体是否存活
    def is_alive(self):
        return self.health > 0

    # 检查实体速度是否有效
    def is_speed_valid(self):
        return 0 <= self.speed <= self.max_speed

    # 移动实体
    def move(self):
        # 限制实体在屏幕内移动
        self.vector.x = max(0, min(self.vector.x, Settings.SCREEN_WIDTH - self.size))
        self.vector.y = max(0, min(self.vector.y, Settings.SCREEN_HEIGHT - self.size))