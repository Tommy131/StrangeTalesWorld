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
LastEditTime : 2024-07-25 01:05:09
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''
# weapon_roulette.py

import math
import pygame
import time

import game

from event.event_handler import EventHandler
from inventory.item.weapon import Weapon
from utils.settings import Settings

class WeaponRoulette(EventHandler):
    def __init__(self, weapons):
        """
        初始化对象

        :param weapons: 武器列表
        """
        self.weapons = weapons
        self.current_weapon = weapons[0] if weapons else None
        self.animations = []
        self.weapon_display_size = 100
        self.small_weapon_size = 60
        self.margin = 20
        self.arc_radius = 100
        self.font = pygame.font.Font(None, 36)
        self.animation_duration = 300  # 动画持续时间（毫秒）

    def draw(self):
        """
        绘制武器轮盘
        """
        # 绘制选中武器的中心坐标
        center_x = Settings.SCREEN_WIDTH - self.weapon_display_size // 2 - self.margin - 10
        center_y = Settings.SCREEN_HEIGHT - self.weapon_display_size // 2 - self.margin - 90

        if len(self.weapons) > 0:
            angle_step = math.pi / (len(self.weapons) + 1)  # 每个武器之间的角度间隔
            for i, weapon in enumerate(self.weapons):
                angle = angle_step * (i + 3)  # 计算每个武器的角度
                weapon_x = center_x + self.arc_radius * math.cos(angle) - self.small_weapon_size // 2 - self.margin
                weapon_y = center_y - self.arc_radius * math.sin(angle) - self.small_weapon_size // 2 - self.margin

                if weapon.main_image:
                    weapon_image = pygame.transform.scale(weapon.main_image, (self.small_weapon_size, self.small_weapon_size))
                    if weapon != self.current_weapon:
                        weapon_image.set_alpha(90)  # 设置透明度以弱化显示
                    else:
                        self.draw_shadow((weapon_x, weapon_y), alpha=50)
                    game.graphic.screen.blit(weapon_image, (weapon_x, weapon_y))
                else:
                    if weapon == self.current_weapon:
                        self.draw_shadow((weapon_x, weapon_y), alpha=90)
                    self.draw_circle_shadow(weapon.color, self.small_weapon_size, vector=(weapon_x, weapon_y))

        if self.current_weapon:
            if self.current_weapon.main_image:
                size = self.weapon_display_size
                # 固定显示坐标
                fixed_vector = (Settings.SCREEN_WIDTH - size - 20, Settings.SCREEN_HEIGHT - size - 130)
                # 创建带透明背景的圆形遮罩
                mask_surface = pygame.Surface((size, size), pygame.SRCALPHA)
                pygame.draw.circle(mask_surface, (*self.current_weapon.color[:3], 90), (size // 2, size // 2), size // 2)
                # 绘制当前武器
                current_weapon_image = pygame.transform.scale(self.current_weapon.main_image, (size, size))
                # 先绘制圆形遮罩
                game.graphic.screen.blit(mask_surface, fixed_vector)
                # 再绘制武器图片
                game.graphic.screen.blit(current_weapon_image, fixed_vector)

            else:
                self.draw_circle_shadow(self.current_weapon.color, self.weapon_display_size)

            # 绘制武器信息
            weapon_name = self.current_weapon.name if self.current_weapon is not None else 'None'
            ammo = self.current_weapon.ammo if isinstance(self.current_weapon, Weapon) else 'N'
            clip_size = self.current_weapon.clip_size if isinstance(self.current_weapon, Weapon) else 'A'
            weapon_info = [
                [f'Current Weapon: {weapon_name}', self.current_weapon.color],
                [f'Ammo: {ammo}/{clip_size}', Settings.WHITE]
            ]
            for i, line in enumerate(weapon_info):
                weapon_text = self.font.render(line[0], True, line[1])
                game.graphic.screen.blit(weapon_text, (Settings.SCREEN_WIDTH - weapon_text.get_width() - self.margin, Settings.SCREEN_HEIGHT - weapon_text.get_height() * (len(weapon_info) - i) - self.margin))

    def draw_shadow(self, pos, alpha=128):
        """
        绘制方形阴影

        :param pos: 坐标
        :param alpha: 透明值, defaults to 128
        """
        s = pygame.Surface((self.small_weapon_size, self.small_weapon_size))
        s.set_alpha(alpha)
        s.fill(Settings.BLACK)
        game.graphic.screen.blit(s, pos)

    def draw_circle_shadow(self, color, size, vector=None):
        """
        添加阴影

        :param color: 背景颜色
        :param size: 显示大小
        :param vector: 固定坐标, defaults to None
        """
        if vector:
            vector = (int(vector[0] + size // 2), int(vector[1] + size // 2))
        else:
            vector = (Settings.SCREEN_WIDTH - size // 2 - self.margin - 10, Settings.SCREEN_HEIGHT - size // 2 - self.margin - 110)
        pygame.draw.circle(game.graphic.screen, color, vector, size // 2 - 5)

    def on_call(self, event):
        """
        pygame 事件处理函数

        :param event: pygame 事件
        """
        if Settings.state == Settings.PLAYING:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    # 切换到下一个武器
                    current_index = self.weapons.index(self.current_weapon)
                    new_index = (current_index + 1) % len(self.weapons)
                    self.current_weapon = self.weapons[new_index]
                    self.animations.append([time.time(), new_index])