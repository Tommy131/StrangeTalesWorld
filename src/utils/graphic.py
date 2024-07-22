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
LastEditTime : 2024-07-23 00:46:12
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''
# graphics.py

import pygame

from entity.entity import Entity
from utils.settings import Settings
from utils.utils import find_longest_element

class Graphic:
    # 初始化游戏
    def initialize_game(self):
        pygame.init()
        screen = pygame.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
        pygame.display.set_caption('末日幸存者')

        background_image = pygame.image.load(f'{Settings.IMAGE_PATH}background.jpg').convert()
        background_image = pygame.transform.scale(background_image, (Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
        return screen, background_image

    # 保存游戏
    def save_game(self, entity):
        try:
            if isinstance(entity, Entity):
                entity.save_state(f'{Settings.SAVED_PATH}{entity.__class__.__name__}.json')
                return True
            return False
        except FileNotFoundError:
            pass

    # 读取游戏存档
    def load_game(self, entity):
        try:
            if isinstance(entity, Entity):
                entity.load_state(f'{Settings.SAVED_PATH}{entity.__class__.__name__}.json')
                return entity
            return False
        except FileNotFoundError:
            pass

    # 绘制文字到页面
    def draw_text(self, screen, text=[], text_position=[], text_color=[], font=Settings.FONT_CN, font_size=36, background_color=Settings.BLACK):
        popup_screen = pygame.Surface((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT), pygame.SRCALPHA)
        popup_screen.fill(background_color)

        if isinstance(font, str) or (font == None):
            font = pygame.font.Font(font, font_size)

        for i, line in enumerate(text):
            text_screen = font.render(line, True, text_color[i] if i in range(len(text_color)) else (255, 255, 255))
            popup_rect = text_screen.get_rect(center=text_position[i] if i in range(len(text_position)) else (Settings.SCREEN_WIDTH // 2, Settings.SCREEN_HEIGHT // 2 + i * 50))
            popup_screen.blit(text_screen, popup_rect)

        screen.blit(popup_screen, (0, 0))
        pygame.display.flip()

    # 绘制弹窗
    def draw_popup(self, screen, message, font=Settings.FONT_CN, duration=2000):
        self.draw_text(screen, text=[message] if not isinstance(message, list) else message, font=font, background_color=(0, 0, 0, 128))
        pygame.time.delay(duration)

    # 绘制圆形阴影
    def draw_circle_shadow(self, screen, source, size, fixed_vector=None, color=(0, 0, 0, 128)):
        # 固定显示坐标
        if fixed_vector == None:
            fixed_vector = (Settings.SCREEN_WIDTH - size - 30, Settings.SCREEN_HEIGHT - size - 90)
        # 创建带透明背景的圆形遮罩
        mask_screen = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(mask_screen, color, (size // 2, size // 2), size // 2)
        # 绘制当前武器
        current_weapon_image = pygame.transform.scale(source, (size, size))
        # 先绘制圆形遮罩
        screen.blit(mask_screen, fixed_vector)
        # 再绘制武器图片
        screen.blit(current_weapon_image, fixed_vector)


    # 绘制游戏主页面
    def draw_menu(self, screen):
        width = Settings.SCREEN_WIDTH // 2
        self.draw_text(screen, text=[
            '末日幸存者',
            '按 Enter 开始游戏',
            '按 S 进入设置',
            '按 Q 退出游戏'
        ],
        text_color=[
            (64, 224, 208)
        ], text_position=[
            (width, Settings.SCREEN_HEIGHT // 2 - 100),
            (width, Settings.SCREEN_HEIGHT // 2),
            (width, Settings.SCREEN_HEIGHT // 2 + 50),
            (width, Settings.SCREEN_HEIGHT // 2 + 100),
        ])

    # 绘制游戏设置页面
    def draw_settings(self, screen):
        width = Settings.SCREEN_WIDTH // 2
        self.draw_text(screen, text=[
            '设置界面',
            '按 ESC 返回菜单',
        ],
        text_color=[
            (243, 58, 106)
        ], text_position=[
            (width, Settings.SCREEN_HEIGHT // 2 - 100),
            (width, Settings.SCREEN_HEIGHT // 2),
        ])

    # 绘制游戏暂停页面
    def draw_pause(self, screen):
        width = Settings.SCREEN_WIDTH // 2
        self.draw_text(screen, text=[
            '游戏已暂停',
            '按 P 或 ESC 继续游戏',
            '按 S 保存游戏',
            '按 L 读取游戏',
            '按 Q 退出游戏'
        ],
        text_color=[
            (255, 234, 0)
        ], text_position=[
            (width, Settings.SCREEN_HEIGHT // 2 - 100),
            (width, Settings.SCREEN_HEIGHT // 2 - 50),
            (width, Settings.SCREEN_HEIGHT // 2),
            (width, Settings.SCREEN_HEIGHT // 2 + 50),
            (width, Settings.SCREEN_HEIGHT // 2 + 100),
        ])

    # 绘制调试窗口
    def draw_debug_window(self, screen, debug_text=[], color=[]):
        if debug_text == None or len(debug_text) == 0:
            return

        margin = 10
        overlay_width = margin + len(find_longest_element(debug_text)) * (margin - 1)
        overlay_height = margin + len(debug_text) * 20

        # 创建带透明背景的遮罩
        debug_screen = pygame.Surface((overlay_width, overlay_height), pygame.SRCALPHA)
        debug_screen.fill((0, 0, 0, 128))  # 透明黑色

        # 绘制调试信息
        font = pygame.font.Font(None, 24)

        for i, line in enumerate(debug_text):
            text_screen = font.render(line, True, color[i] if i in range(len(color)) else (255, 255, 255))
            debug_screen.blit(text_screen, (margin, margin + i * 20))

        # 在屏幕上绘制调试窗口
        screen.blit(debug_screen, (margin, margin))