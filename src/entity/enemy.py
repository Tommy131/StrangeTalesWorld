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
LastEditTime : 2024-09-03 20:46:15
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''
# enemy.py

import os
import math
import random

import game
import pygame

from entity.entity import Entity
from utils.settings import Settings
from utils.utils import load_image, scale_image

class Enemy(Entity):
    # 示例名字和姓氏列表
    first_names = [
        'Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack',
        'Katherine', 'Liam', 'Mia', 'Noah', 'Olivia', 'Paul', 'Quincy', 'Rachel', 'Sam', 'Tina'
    ]

    last_names = [
        'Anderson', 'Brown', 'Clark', 'Davis', 'Evans', 'Garcia', 'Harris', 'Jackson', 'Johnson', 'King',
        'Lewis', 'Miller', 'Nelson', 'O\'Brien', 'Parker', 'Quinn', 'Robinson', 'Smith', 'Taylor', 'Wilson'
    ]

    def __init__(self, screen, name='Enemy'):
        """
        初始化玩家对象, 继承自 Entity 类

        :param name: 玩家名称, 默认为 'Player'
        """
        super().__init__(screen, name=name, speed=2, damage=5, color=Settings.RED)
        self.images = {index: scale_image(load_image(os.path.join('assets/images/enemy', f'enemy-{index}.png')), self.size, self.size) for index in Settings.DIRECTIONS}
        self.attack_images = {}
        self.attack_images.update({f'enemy-attack-{i}': scale_image(load_image(os.path.join('assets/images/enemy', f'enemy-attack-{i}.png')), self.size, self.size) for i in range(4)})

        self.last_direction = Settings.RIGHT
        self.facing_left = False
        self.attack_range = 500
        self.attack_cooldown = 0
        self.attack_animation_time = 0
        self.max_attack_frames = 4
        self.attack_frame = 0
        self.attacking = False
        self.can_display_health_bar = False
        self.current_weapon = None

    def generate_name(self):
        """
        生成随机名称

        :return: 字符串, 随机生成的全名, 包含姓和名
        """
        first_name = random.choice(self.first_names)
        last_name = random.choice(self.last_names)
        return f"{first_name} {last_name}"

    def _draw(self):
        """
        渲染角色当前的动画状态到指定的表面
        """
        if self.attacking:
            for i in range(4):
                image = self.attack_images[f'enemy-attack-{i}']
                if self.facing_left:
                    self.screen.blit(pygame.transform.flip(image, True, False), self.get_pos())
                else:
                    self.screen.blit(image, self.get_pos())
        else:
            if self.facing_left:
                self.screen.blit(pygame.transform.flip(self.images['right'], True, False), self.get_pos())
            else:
                self.screen.blit(self.images[self.last_direction], self.get_pos())

    def calculate_distance(self, other_entity):
        """
        计算当前实体与另一个实体之间的欧几里得距离

        :param other_entity: 另一个实体
        :return: 浮点数, 表示两个实体之间的距离
        """
        return math.sqrt((self.vector.x - other_entity.vector.x) ** 2 + (self.vector.y - other_entity.vector.y) ** 2)

    def is_attack_distance(self, other_entity):
        """
        判断另一个实体是否在攻击范围内

        :param other_entity: 另一个实体
        :return: 布尔值, 如果实体在攻击范围内则返回True, 否则返回False
        """
        distance = self.calculate_distance(other_entity)
        return distance <= self.attack_range

    def move_towards_other_entity(self, other_entity):
        """
        朝另一个实体移动

        :param other_entity: 另一个实体
        """
        if self.is_attack_distance(other_entity):
            if abs(self.vector.x - other_entity.vector.x) > abs(self.vector.y - other_entity.vector.y):
                if self.vector.x < other_entity.vector.x:
                    self.vector.x += self.speed
                    self.direction = Settings.RIGHT
                    self.facing_left = False
                elif self.vector.x > other_entity.vector.x:
                    self.vector.x -= self.speed
                    self.direction = Settings.LEFT
                    self.facing_left = True
            else:
                if self.vector.y < other_entity.vector.y:
                    self.vector.y += self.speed
                    self.direction = Settings.DOWN
                elif self.vector.y > other_entity.vector.y:
                    self.vector.y -= self.speed
                    self.direction = Settings.UP
            #更新朝向
            self.last_direction = self.direction

    def attack(self, other_entity):
        """
        检查当前实体是否攻击了另一个实体

        :param other_entity: 另一个实体
        :return: 布尔值, 如果当前实体攻击成功则返回True, 否则返回False
        """
        return (self.vector.x < other_entity.vector.x + self.size and
                self.vector.x + self.size > other_entity.vector.x and
                self.vector.y < other_entity.vector.y + self.size and
                self.vector.y + self.size > other_entity.vector.y)

    def attack_other_entity(self, other_entity):
        """
        对另一个实体进行攻击并造成伤害

        :param other_entity: 实体对象, 被攻击的实体
        """
        if self.attack_cooldown == 0:
            other_entity.take_damage(self.damage)
            self.attack_cooldown = 60  # 设置冷却时间, 例如60帧
            self.attacking = True
            self.attack_animation_time = 30  # 设置攻击动画时间, 例如30帧

    def update_cooldown(self):
        """
        更新攻击冷却时间

        :return: None
        """
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

    def update_attack_animation(self):
        """
        更新攻击动画状态

        :return: None
        """
        if self.attacking:
            self.attack_frame += 1
            if self.attack_frame >= self.max_attack_frames:
                self.attack_frame = 0
                self.attacking = False  # 动画播放完毕, 停止攻击状态

    def use_weapon(self):
        """
        使用当前武器进行攻击

        :return: 攻击结果对象, 如果没有武器则返回None
        """
        if self.current_weapon:
            attack_result = self.current_weapon.attack(self.get_pos(), self.size, self.last_direction)
            return attack_result
        return None

    def update(self):
        player = game.player

        if self.health <= 0:
            self.name = self.generate_name()
            self.vector.x = random.randint(0, Settings.SCREEN_WIDTH - self.size)
            self.vector.y = random.randint(0, Settings.SCREEN_HEIGHT - self.size)
            self.set_health(self.max_health)
            return

        # 更新敌对NPC的位置
        self.move_towards_other_entity(player)
        self.update_cooldown()
        self.update_attack_animation()

        # 碰撞检测: 玩家与敌对NPC
        if player.check_collision(self):
            if self.current_weapon and self.current_weapon.can_shoot():
                self.attack(player)
            else:
                self.attack_other_entity(player)

        # 判断敌对NPC是否拥有武器
        if self.is_attack_distance(player):
            attack_result = self.use_weapon()
            if attack_result:
                self.current_weapon.effect.append(attack_result)

        # 绘制敌对NPC的武器效果
        if self.current_weapon:
            self.current_weapon.effect(player)

        # 根据范围绘制敌对NPC的血量条
        display_distance = 300
        if (abs(self.vector.x - player.vector.x) <= display_distance) and (abs(self.vector.y - player.vector.y) <= display_distance):
            self.can_display_health_bar = True
        else:
            self.can_display_health_bar = False

        self.draw()