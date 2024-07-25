'''
       _____   _          __  _____   _____   _       _____   _____
     /  _  \ | |        / / /  _  \ |  _  \ | |     /  _  \ /  ___|
     | | | | | |  __   / /  | | | | | |_| | | |     | | | | | |
     | | | | | | /  | / /   | | | | |  _  { | |     | | | | | |   _
     | |_| | | |/   |/ /    | |_| | | |_| | | |___  | |_| | | |_| |
     \_____/ |___/|___/     \_____/ |_____/ |_____| \_____/ \_____/

Copyright (c) 2023 by OwOTeam-DGMT (OwOBlog).
Date         : 2024-07-23 15:12:40
Author       : HanskiJay
LastEditors  : HanskiJay
LastEditTime : 2024-07-25 01:54:32
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''
# item.py

import pygame

import game

from utils.settings import Settings
from vector import Vector
from utils.utils import load_image, scale_image

class Item:
    DURABILITY = 1

    ITEM = 'item'
    WEAPON = 'weapon'
    GUN = 'weapon/gun'
    SWORD = 'weapon/sword'

    ITEM_TYPES = [ITEM, WEAPON, GUN, SWORD]

    def __init__(self, item_id, name, description='no description', i_type=ITEM, size=50, main_image=None, quantity=1, durability=DURABILITY, color=Settings.WHITE):
        """
        初始化物品

        :param item_id: 物品ID
        :param name: 物品名称
        :param description: 物品描述
        :param quantity: 物品数量, defaults to 1
        :param durability: 耐久性, defaults to DURABILITY
        :param color: 物品颜色, defaults to Settings.WHITE
        """
        self.id = item_id
        self.name = name
        self.description = description
        self.i_type = i_type
        self.size = size
        self.main_image = scale_image(load_image(f'{Settings.ASSETS_PATH}/images/{i_type}/{main_image}'), size, size) if main_image != None else None
        self.quantity = quantity
        self.durability = durability
        self.vector = Vector()
        self.color = color

        self.equipped = False
        self.is_on_ground = False

    def __repr__(self):
        """
        返回物品描述

        :return: str
        """
        return (f'Item(id={self.id}, name={self.name}, description={self.description}',
                f'quantity={self.quantity}), durability={self.durability}, color={self.color}',
                f'is_equipped={self.equipped.__str__}, is_on_ground={self.is_on_ground.__str__}')

    def __len__(self):
        """
        返回物品数量

        :return: int
        """
        return self.quantity

    def is_equipped(self):
        """
        返回当前物品装备状态

        :return: bool
        """
        return self.equipped == True

    def is_on_ground(self):
        """
        判断物品是否在地上

        :return: bool
        """
        return self.is_on_ground == False

    def update(self, quantity=0, durability=0):
        """
        更新物品的数量和耐久性

        :param quantity: 要增加的数量
        :param durability: 要增加的耐久性
        """
        self.quantity += quantity
        self.durability = min(self.durability + durability, Item.DURABILITY)

    def remove_quantity(self, quantity):
        """
        移除指定数量的物品

        :param quantity: 要移除的数量
        """
        if quantity >= self.quantity:
            self.quantity = 0
        else:
            self.quantity -= quantity

    def use(self, quantity=1):
        """
        使用物品

        :param entity: 实体
        :param quantity: 数量, defaults to 1
        """
        # 省略执行逻辑, 因物品不同所需执行的代码不同

        self.remove_quantity(quantity)
        return True

    def draw(self, pos=None):
        if self.main_image == None:
            pygame.draw.rect(game.graphic.screen, self.color, (*self.vector.get_pos(), self.size, self.size))
        else:
            game.graphic.screen.blit(self.main_image, pos if pos != None else self.vector.get_pos())