'''
       _____   _          __  _____   _____   _       _____   _____
     /  _  \ | |        / / /  _  \ |  _  \ | |     /  _  \ /  ___|
     | | | | | |  __   / /  | | | | | |_| | | |     | | | | | |
     | | | | | | /  | / /   | | | | |  _  { | |     | | | | | |   _
     | |_| | | |/   |/ /    | |_| | | |_| | | |___  | |_| | | |_| |
     \_____/ |___/|___/     \_____/ |_____/ |_____| \_____/ \_____/

 Copyright (c) 2023 by OwOTeam-DGMT (OwOBlog).
Date         : 2024-07-20 22:27:42
Author       : HanskiJay
LastEditors  : HanskiJay
LastEditTime : 2024-07-25 02:04:47
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''
# empty_effect.py


from effect.effect import Effect
from utils.settings import Settings

class EmptyEffect(Effect):
    def __init__(self, color=Settings.WHITE):
        """
        初始化对象

        :param color: 颜色, defaults to Settings.YELLOW
        """
        super().__init__(0, color=color)

    def update(self):
        pass

    def draw(self):
        pass

    def collide(self, entity):
        pass

    def is_off_screen(self):
        return False