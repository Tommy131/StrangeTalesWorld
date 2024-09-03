'''
       _____   _          __  _____   _____   _       _____   _____
     /  _  \ | |        / / /  _  \ |  _  \ | |     /  _  \ /  ___|
     | | | | | |  __   / /  | | | | | |_| | | |     | | | | | |
     | | | | | | /  | / /   | | | | |  _  { | |     | | | | | |   _
     | |_| | | |/   |/ /    | |_| | | |_| | | |___  | |_| | | |_| |
     \_____/ |___/|___/     \_____/ |_____/ |_____| \_____/ \_____/

Copyright (c) 2023 by OwOTeam-DGMT (OwOBlog).
Date         : 2024-07-24 02:52:09
Author       : HanskiJay
LastEditors  : HanskiJay
LastEditTime : 2024-09-03 18:37:50
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''
# weapon.py

import random

from inventory.item.item import Item
from utils.settings import Settings

class Weapon(Item):
    def __init__(self, item_id, name, description='no description', i_type=Item.WEAPON, main_image=None, durability=Item.DURABILITY, color=Settings.WHITE, attack_rate=0, damage=0, attack_cooldown=5):
        """
        初始化对象

        :param item_id: 武器ID
        :param name: 武器名称
        :param description: 武器描述, defaults to 'no description'
        :param i_type: 武器类型, defaults to Item.WEAPON
        :param main_image: 武器的主要显示图片, defaults to None
        :param durability: 耐久度, defaults to Item.DURABILITY
        :param color: 武器颜色, defaults to Settings.WHITE
        :param attack_rate: 攻击范围, defaults to 2
        :param damage: 伤害, defaults to 10
        :param attack_cooldown: 攻击冷却时间, defaults to 5
        """
        super().__init__(item_id, name, description=description, i_type=i_type, main_image=main_image, quantity=1, durability=durability, color=color)
        self.attack_rate = attack_rate
        self.damage = damage
        self.attack_cooldown = attack_cooldown

        self.is_taken = False
        self.effects = []

    def spawn(self):
        """
        生成武器
        """
        self.vector.x = random.randint(0, Settings.SCREEN_WIDTH - 50)
        self.vector.y = random.randint(0, Settings.SCREEN_HEIGHT - 50)

    def effect(self, entity):
        """
        激活武器效果

        :param entity: _description_
        :return: bool
        """
        for effect in self.effects[:]:
            effect.update()
            if entity and effect.collide(entity):
                self.effects.remove(effect)
                entity.take_damage(self.damage)
                if entity.is_alive() == False:
                    return True
            elif effect.is_off_screen():
                self.effects.remove(effect)
        return False

    def attack(self):
        """
        攻击实现方法
        """
        pass