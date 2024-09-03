'''
       _____   _          __  _____   _____   _       _____   _____
     /  _  \ | |        / / /  _  \ |  _  \ | |     /  _  \ /  ___|
     | | | | | |  __   / /  | | | | | |_| | | |     | | | | | |
     | | | | | | /  | / /   | | | | |  _  { | |     | | | | | |   _
     | |_| | | |/   |/ /    | |_| | | |_| | | |___  | |_| | | |_| |
     \_____/ |___/|___/     \_____/ |_____/ |_____| \_____/ \_____/

 Copyright (c) 2023 by OwOTeam-DGMT (OwOBlog).
Date         : 2024-07-19 21:30:04
Author       : HanskiJay
LastEditors  : HanskiJay
LastEditTime : 2024-07-20 22:28:16
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''
# bullet.py

from effect.effect import Effect
from utils.settings import Settings
from vector import Vector

class BulletEffect(Effect):
    def __init__(self, vector, vel, size, color=Settings.YELLOW):
        """
        初始化对象

        :param vel: 向量
        :param size: 大小
        :param color: 颜色, defaults to Settings.YELLOW
        """
        super().__init__(size, vector=vector, color=color)
        self.vel = vel

    def update(self):
        self.vector.x += self.vel.x
        self.vector.y += self.vel.y
