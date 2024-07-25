'''
       _____   _          __  _____   _____   _       _____   _____
     /  _  \ | |        / / /  _  \ |  _  \ | |     /  _  \ /  ___|
     | | | | | |  __   / /  | | | | | |_| | | |     | | | | | |
     | | | | | | /  | / /   | | | | |  _  { | |     | | | | | |   _
     | |_| | | |/   |/ /    | |_| | | |_| | | |___  | |_| | | |_| |
     \_____/ |___/|___/     \_____/ |_____/ |_____| \_____/ \_____/

 Copyright (c) 2023 by OwOTeam-DGMT (OwOBlog).
Date         : 2024-07-25 02:18:55
Author       : HanskiJay
LastEditors  : HanskiJay
LastEditTime : 2024-07-25 02:27:45
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''
# sword.py

import pygame

from inventory.item.weapon import Weapon
from utils.settings import Settings

from effect.empty_effect import EmptyEffect
from effect.sword_effect import SwordEffect

class Sword(Weapon):
    def __init__(self, item_id, name, description='no description', main_image=None, color=Settings.WHITE, attack_rate=2, damage=10, attack_cooldown=5):
        """
        初始化对象

        :param item_id: 枪的ID
        :param name: 枪的名称
        :param description: 枪的描述, defaults to 'no description'
        :param main_image: 枪的的主要显示图片, defaults to None
        :param color: 枪的颜色, defaults to Settings.WHITE
        :param attack_rate: 攻击范围, defaults to 2
        :param damage: 伤害, defaults to 10
        :param attack_cooldown: 攻击冷却时间, defaults to 5
        """
        super().__init__(item_id, name, description=description, i_type=Weapon.SWORD, main_image=main_image, color=color, attack_rate=attack_rate, damage=damage, attack_cooldown=attack_cooldown)
        self.last_attack_time = 0

    def attack(self, entity, direction):
        """
        攻击实体

        :param entity: 实体
        :param direction: 朝向
        :return: Effect 效果
        """
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time < self.attack_cooldown * 1000:
            return EmptyEffect()

        self.last_attack_time = current_time
        sword_effect_size = 20

        if direction == Settings.LEFT:
            sword_effect_pos = [entity.vector.x - sword_effect_size, entity.vector.y + entity.size // 2]
        elif direction == Settings.RIGHT:
            sword_effect_pos = [entity.vector.x + entity.size, entity.vector.y + entity.size // 2]
        elif direction == Settings.UP:
            sword_effect_pos = [entity.vector.x + entity.size // 2, entity.vector.y - sword_effect_size]
        elif direction == Settings.DOWN:
            sword_effect_pos = [entity.vector.x + entity.size // 2, entity.vector.y + entity.size]

        return SwordEffect(sword_effect_pos, sword_effect_size)