'''
       _____   _          __  _____   _____   _       _____   _____
     /  _  \ | |        / / /  _  \ |  _  \ | |     /  _  \ /  ___|
     | | | | | |  __   / /  | | | | | |_| | | |     | | | | | |
     | | | | | | /  | / /   | | | | |  _  { | |     | | | | | |   _
     | |_| | | |/   |/ /    | |_| | | |_| | | |___  | |_| | | |_| |
     \_____/ |___/|___/     \_____/ |_____/ |_____| \_____/ \_____/

 Copyright (c) 2023 by OwOTeam-DGMT (OwOBlog).
Date         : 2024-07-20 17:48:21
Author       : HanskiJay
LastEditors  : HanskiJay
LastEditTime : 2024-07-20 18:27:36
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''
# sword_effect.py

from effect.effect import Effect
from utils.settings import Settings

class SwordEffect(Effect):
    def __init__(self, size, color=Settings.LIGHT_YELLOW):
        """
        初始化对象

        :param vel: 向量
        :param size: 大小
        :param color: 颜色, defaults to Settings.YELLOW
        """
        super().__init__(size, color=color)
        self.frames = 10  # 效果显示的帧数

    def update(self):
        self.frames -= 1

    def draw(self):
        if self.frames > 0:
            super().draw()
