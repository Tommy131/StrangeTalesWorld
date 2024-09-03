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
LastEditTime : 2024-09-03 17:59:51
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''
# player.py

import pygame

import game

from entity.entity import Entity
from utils.settings import Settings

class Player(Entity):
    def __init__(self, screen, name='Player'):
        """
        初始化玩家对象, 继承自 Entity 类

        :param name: 玩家名称, 默认为 'Player'
        """
        super().__init__(screen, name=name, damage=1, color=(0, 0, 255))
        self.can_display_health_bar = True

    def draw(self):
        """
        绘制玩家对象, 包括头部信息和生命值条
        """
        super().draw()

    def move(self, keys):
        """
        根据按键移动玩家, 并调整玩家速度

        :param keys: 当前按键状态的字典 (pygame.key.get_pressed() 的返回值)
        """
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vector.x -= self.speed
            self.last_direction = Settings.LEFT

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vector.x += self.speed
            self.last_direction = Settings.RIGHT

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.vector.y -= self.speed
            self.last_direction = Settings.UP

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.vector.y += self.speed
            self.last_direction = Settings.DOWN

        # 玩家移速判断
        if keys[pygame.K_LSHIFT]:
            self.speed = self.MAX_SPEED
        else:
            self.speed = self.SPEED

        super().move()

    def press(self, keys, entity):
        """
        实现玩家按下按键事件监听

        :param keys: 当前按键状态的字典 (pygame.key.get_pressed() 的返回值)
        """
        current_weapon = game.weapon_roulette.current_weapon

        # 使用武器
        if keys[pygame.K_SPACE] and game.player.last_direction:
            current_weapon.effects.append(current_weapon.attack(game.player, game.player.last_direction))

        # 重新加载武器 (按R键重新加载)
        if keys[pygame.K_r] and current_weapon:
            current_weapon.reload()

        # 绘制武器效果
        if game.weapon_roulette.weapons:
            for weapon in game.weapon_roulette.weapons:
                weapon.effect(entity)
                for effect in weapon.effects:
                    effect.draw()