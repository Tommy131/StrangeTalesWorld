'''
       _____   _          __  _____   _____   _       _____   _____
     /  _  \ | |        / / /  _  \ |  _  \ | |     /  _  \ /  ___|
     | | | | | |  __   / /  | | | | | |_| | | |     | | | | | |
     | | | | | | /  | / /   | | | | |  _  { | |     | | | | | |   _
     | |_| | | |/   |/ /    | |_| | | |_| | | |___  | |_| | | |_| |
     \_____/ |___/|___/     \_____/ |_____/ |_____| \_____/ \_____/

Copyright (c) 2023 by OwOTeam-DGMT (OwOBlog).
Date         : 2024-07-24 01:35:55
Author       : HanskiJay
LastEditors  : HanskiJay
LastEditTime : 2024-07-24 02:38:16
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''
# item_bar.py

import pygame

import game

from event.event_handler import EventHandler
from utils.settings import Settings

class ItemBar(EventHandler):
    def __init__(self, items):
        """
        初始化物品栏类

        :param items (list): 物品对象的列表
        """
        self.items = items  # 物品列表
        self.dragging_item = None  # 当前被拖动的物品索引
        self.drag_offset_x = 0  # 拖动物品时的横向偏移
        self.drag_offset_y = 0  # 拖动物品时的纵向偏移
        self.drag_pos = None  # 拖动物品的当前位置
        self.animation_duration = 300  # 动画持续时间（毫秒）
        self.animations = []  # 动画列表

    def draw(self):
        """
        绘制物品栏和物品
        """
        font = pygame.font.Font(None, 24)  # 设置字体
        num_items = len(self.items)  # 物品数量
        bar_width = (Settings.ITEM_SIZE + Settings.ITEM_PADDING) * num_items + Settings.ITEM_PADDING  # 物品栏宽度
        bar_height = Settings.ITEM_SIZE + 2 * Settings.ITEM_PADDING + 5  # 物品栏高度

        # 动态调整物品栏的位置和尺寸
        bar_x = (Settings.SCREEN_WIDTH - bar_width) // 2  # 物品栏X坐标
        bar_y = Settings.SCREEN_HEIGHT - bar_height - 20  # 物品栏Y坐标

        # 绘制物品栏背景
        pygame.draw.rect(game.graphic.screen, Settings.GREY, (bar_x, bar_y, bar_width, bar_height))

        # 绘制物品
        for i, item in enumerate(self.items):
            item_x = bar_x + Settings.ITEM_PADDING + i * (Settings.ITEM_SIZE + Settings.ITEM_PADDING)  # 物品X坐标
            item_y = bar_y + Settings.ITEM_PADDING  # 物品Y坐标

            if self.dragging_item == i:
                continue  # 如果物品正在被拖动，跳过绘制

            if item.main_image:
                game.graphic.screen.blit(item.main_image, (item_x, item_y))  # 绘制物品图片
            else:
                pygame.draw.rect(game.graphic.screen, Settings.WHITE, (item_x, item_y, Settings.ITEM_SIZE, Settings.ITEM_SIZE))  # 如果没有图片，用颜色填充

            # 显示物品数量
            quantity_text = font.render(str(item.quantity), True, Settings.BLACK)
            game.graphic.screen.blit(quantity_text, (item_x + Settings.ITEM_SIZE - quantity_text.get_width() - 5, item_y + Settings.ITEM_SIZE - quantity_text.get_height() - 5))

            # 显示物品耐久度条
            if item.durability != False:
                self.draw_durability_bar(item_x, item_y, item.durability)

        # 绘制动画
        for anim in self.animations:
            item_x, item_y, target_x, target_y, start_time = anim  # 获取动画参数
            progress = (pygame.time.get_ticks() - start_time) / self.animation_duration  # 计算动画进度
            if progress >= 1:
                self.animations.remove(anim)
                continue
            current_x = item_x + (target_x - item_x) * progress  # 当前X坐标
            current_y = item_y + (target_y - item_y) * progress  # 当前Y坐标
            item = self.items[self.animations.index(anim)]  # 获取物品
            if item.main_image:
                game.graphic.screen.blit(item.main_image, (current_x, current_y))  # 绘制物品图片
            else:
                pygame.draw.rect(game.graphic.screen, Settings.WHITE, (current_x, current_y, Settings.ITEM_SIZE, Settings.ITEM_SIZE))  # 用颜色填充

                if item.durability != False:
                    self.draw_durability_bar(current_x, current_y, item.durability)  # 绘制耐久度条

            # 显示物品数量
            quantity_text = font.render(str(item.quantity), True, Settings.BLACK)
            game.graphic.screen.blit(quantity_text, (current_x + Settings.ITEM_SIZE - quantity_text.get_width() - 5, current_y + Settings.ITEM_SIZE - quantity_text.get_height() - 5))

        # 绘制被拖动的物品
        if self.dragging_item is not None and self.drag_pos is not None:
            item = self.items[self.dragging_item]  # 获取被拖动的物品
            if item.main_image:
                game.graphic.screen.blit(item.main_image, self.drag_pos)  # 绘制物品图片
            else:
                pygame.draw.rect(game.graphic.screen, Settings.WHITE, (*self.drag_pos, Settings.ITEM_SIZE, Settings.ITEM_SIZE))  # 用颜色填充

                if item.durability != False:
                    self.draw_durability_bar(self.drag_pos[0], self.drag_pos[1], item.durability)  # 绘制耐久度条

            # 显示物品数量
            quantity_text = font.render(str(item.quantity), True, Settings.BLACK)
            game.graphic.screen.blit(quantity_text, (self.drag_pos[0] + Settings.ITEM_SIZE - quantity_text.get_width() - 5, self.drag_pos[1] + Settings.ITEM_SIZE - quantity_text.get_height() - 5))

    def draw_durability_bar(self, x, y, durability):
        """
        绘制物品的耐久度条

        :param x (int) :耐久度条的X坐标
        :param y (int): 耐久度条的Y坐标
        :param durability (float): 物品的耐久度（0到1之间）
        """
        bar_width = Settings.ITEM_SIZE  # 耐久度条的宽度
        bar_height = 5  # 耐久度条的高度
        fill_width = bar_width * durability  # 耐久度条填充的宽度
        y += Settings.ITEM_SIZE  # 耐久度条的Y坐标

        pygame.draw.rect(game.graphic.screen, Settings.RED, (x, y, bar_width, bar_height))  # 绘制背景（红色）
        pygame.draw.rect(game.graphic.screen, Settings.GREEN, (x, y, fill_width, bar_height))  # 绘制填充（绿色）

    def on_call(self, event):
        """
        处理事件

        :param event (pygame.event.Event): pygame事件对象
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # 处理鼠标左键按下事件
                mouse_x, mouse_y = event.pos  # 获取鼠标位置
                for i, item in enumerate(self.items):
                    item_x = (Settings.SCREEN_WIDTH - (Settings.ITEM_SIZE + Settings.ITEM_PADDING) * len(self.items) - Settings.ITEM_PADDING) // 2 + Settings.ITEM_PADDING + i * (Settings.ITEM_SIZE + Settings.ITEM_PADDING)
                    item_y = Settings.SCREEN_HEIGHT - Settings.ITEM_SIZE - 2 * Settings.ITEM_PADDING - 20 + Settings.ITEM_PADDING
                    if item_x < mouse_x < item_x + Settings.ITEM_SIZE and item_y < mouse_y < item_y + Settings.ITEM_SIZE:
                        # 判断鼠标是否在物品上
                        self.dragging_item = i  # 设置被拖动的物品
                        self.drag_offset_x = mouse_x - item_x  # 设置拖动偏移
                        self.drag_offset_y = mouse_y - item_y  # 设置拖动偏移
                        self.drag_pos = (mouse_x - self.drag_offset_x, mouse_y - self.drag_offset_y)  # 设置拖动位置
                        break

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and self.dragging_item is not None:
                # 处理鼠标左键松开事件
                mouse_x, mouse_y = event.pos  # 获取鼠标位置
                bar_x = (Settings.SCREEN_WIDTH - (Settings.ITEM_SIZE + Settings.ITEM_PADDING) * len(self.items) - Settings.ITEM_PADDING) // 2  # 获取物品栏X坐标
                new_index = (mouse_x - bar_x) // (Settings.ITEM_SIZE + Settings.ITEM_PADDING)  # 计算新的物品位置索引
                new_index = max(0, min(len(self.items) - 1, new_index))  # 确保索引在有效范围内
                self.animations.append([self.drag_pos[0], self.drag_pos[1], bar_x + new_index * (Settings.ITEM_SIZE + Settings.ITEM_PADDING) + Settings.ITEM_PADDING, Settings.SCREEN_HEIGHT - Settings.ITEM_SIZE - 2 * Settings.ITEM_PADDING - 20 + Settings.ITEM_PADDING, pygame.time.get_ticks()])
                self.items.insert(new_index, self.items.pop(self.dragging_item))  # 移动物品到新的位置
                self.dragging_item = None  # 重置拖动状态
                self.drag_pos = None  # 重置拖动位置

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging_item is not None:
                # 处理鼠标移动事件
                mouse_x, mouse_y = event.pos  # 获取鼠标位置
                self.drag_pos = (mouse_x - self.drag_offset_x, mouse_y - self.drag_offset_y)  # 更新拖动位置
