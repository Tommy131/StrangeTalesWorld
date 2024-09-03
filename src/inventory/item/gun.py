'''
       _____   _          __  _____   _____   _       _____   _____
     /  _  \ | |        / / /  _  \ |  _  \ | |     /  _  \ /  ___|
     | | | | | |  __   / /  | | | | | |_| | | |     | | | | | |
     | | | | | | /  | / /   | | | | |  _  { | |     | | | | | |   _
     | |_| | | |/   |/ /    | |_| | | |_| | | |___  | |_| | | |_| |
     \_____/ |___/|___/     \_____/ |_____/ |_____| \_____/ \_____/

Copyright (c) 2023 by OwOTeam-DGMT (OwOBlog).
Date         : 2024-07-25 01:24:04
Author       : HanskiJay
LastEditors  : HanskiJay
LastEditTime : 2024-07-25 02:27:10
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''
# gun.py

import pygame

from vector import Vector

from inventory.item.weapon import Weapon
from utils.settings import Settings

from effect.bullet_effect import BulletEffect
from effect.empty_effect import EmptyEffect

class Gun(Weapon):
    def __init__(self, item_id, name, description='no description', main_image=None, color=Settings.WHITE, attack_rate=10, damage=10, ammo=30, bullet_speed=10, clip_size=30, attack_cooldown=5):
        """
        初始化对象

        :param item_id: 枪的ID
        :param name: 枪的名称
        :param description: 枪的描述, defaults to 'no description'
        :param main_image: 枪的的主要显示图片, defaults to None
        :param color: 枪的颜色, defaults to Settings.WHITE
        :param attack_rate: 枪的射程, defaults to 10
        :param damage: 伤害, defaults to 10
        :param ammo: 子弹数量, defaults to 30
        :param bullet_speed: 枪的射速, defaults to 10
        :param clip_size: 弹夹容量, defaults to 30
        :param attack_cooldown: 攻击冷却时间, defaults to 5
        """
        super().__init__(item_id, name, description=description, i_type=Weapon.GUN, main_image=main_image, color=color, attack_rate=attack_rate, damage=damage, attack_cooldown=attack_cooldown)
        self.bullet_speed = bullet_speed
        self.ammo = ammo
        self.clip_size = clip_size
        self.last_shot_time = 0

    def reload(self):
        """
        换弹操作
        """
        self.ammo = self.clip_size

    def can_shoot(self):
        """
        判断是否可以射击

        :return: bool
        """
        return self.ammo != 0

    def attack(self, entity, direction):
        """
        攻击实体

        :param entity: 实体
        :param direction: 朝向
        :return: Effect 效果
        """
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time < self.attack_rate or self.ammo <= 0:
            return EmptyEffect()

        self.last_shot_time = current_time
        self.ammo -= 1
        bullet_size = 5

        if direction == Settings.LEFT:
            bullet_pos = [entity.vector.x - bullet_size, entity.vector.y + entity.size // 2]
            bullet_vel = [-self.bullet_speed, 0]
        elif direction == Settings.RIGHT:
            bullet_pos = [entity.vector.x + entity.size, entity.vector.y + entity.size // 2]
            bullet_vel = [self.bullet_speed, 0]
        elif direction == Settings.UP:
            bullet_pos = [entity.vector.x + entity.size // 2, entity.vector.y - bullet_size]
            bullet_vel = [0, -self.bullet_speed]
        elif direction == Settings.DOWN:
            bullet_pos = [entity.vector.x + entity.size // 2, entity.vector.y + entity.size]
            bullet_vel = [0, self.bullet_speed]

        return BulletEffect(Vector(x=bullet_pos[0], y=bullet_pos[1]), Vector(x=bullet_vel[0], y=bullet_vel[1]), bullet_size)