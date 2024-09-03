'''
       _____   _          __  _____   _____   _       _____   _____
     /  _  \ | |        / / /  _  \ |  _  \ | |     /  _  \ /  ___|
     | | | | | |  __   / /  | | | | | |_| | | |     | | | | | |
     | | | | | | /  | / /   | | | | |  _  { | |     | | | | | |   _
     | |_| | | |/   |/ /    | |_| | | |_| | | |___  | |_| | | |_| |
     \_____/ |___/|___/     \_____/ |_____/ |_____| \_____/ \_____/

Copyright (c) 2023 by OwOTeam-DGMT (OwOBlog).
Date         : 2024-07-20 18:28:09
Author       : HanskiJay
LastEditors  : HanskiJay
LastEditTime : 2024-07-20 22:32:38
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''
# effect.py

import pygame

import game

from utils.settings import Settings
from vector import Vector

class Effect:
    def __init__(self, size, vector=Vector(), color=Settings.BLUE):
        """
        初始化对象

        :param vel: 向量
        :param size: 大小
        :param color: 颜色, defaults to Settings.BLUE
        """
        self.vector = vector
        self.size = size
        self.color = color

    def update(self):
        """
        更新效果状态
        """
        pass

    def draw(self):
        """
        绘制效果
        """
        pygame.draw.circle(game.graphic.screen, self.color, self.vector.get_pos(), self.size)

    def collide(self, entity):
        """
        检测碰撞

        :param entity: 实体
        :return: bool
        """
        return (self.vector.x > entity.vector.x and self.vector.x < entity.vector.x + entity.size and
                self.vector.y > entity.vector.y and self.vector.y < entity.vector.y + entity.size)

    def is_off_screen(self):
        """
        检测效果是否超出屏幕范围

        :return: bool
        """
        return (self.vector.x < 0 or self.vector.x > Settings.SCREEN_WIDTH or
                self.vector.y < 0 or self.vector.y > Settings.SCREEN_HEIGHT)