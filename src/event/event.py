'''
       _____   _          __  _____   _____   _       _____   _____
     /  _  \ | |        / / /  _  \ |  _  \ | |     /  _  \ /  ___|
     | | | | | |  __   / /  | | | | | |_| | | |     | | | | | |
     | | | | | | /  | / /   | | | | |  _  { | |     | | | | | |   _
     | |_| | | |/   |/ /    | |_| | | |_| | | |___  | |_| | | |_| |
     \_____/ |___/|___/     \_____/ |_____/ |_____| \_____/ \_____/

Copyright (c) 2023 by OwOTeam-DGMT (OwOBlog).
Date         : 2024-07-22 21:05:07
Author       : HanskiJay
LastEditors  : HanskiJay
LastEditTime : 2024-07-24 00:04:51
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''
# event.py

import pygame

import game
from event.event_handler import EventHandler
from utils.settings import Settings

class Event:
    def __init__(self, screen):
        self.screen = screen
        # 初始化事件处理函数字典
        self.event_handlers = []

    def register(self, handler):
        """
        注册事件处理函数
        :param handler: 事件处理函数
        """
        if handler not in self.event_handlers and isinstance(handler, EventHandler):
            self.event_handlers.append(handler)

    def unregister(self, handler):
        """
        注销事件处理函数
        :param event_type: 事件类型，例如 pygame.KEYDOWN 或 pygame.MOUSEBUTTONDOWN
        :param handler: 事件处理函数
        """
        if handler in self.event_handlers:
            self.event_handlers.remove(handler)

    def pygame_event_handler(self):
        """
        处理 pygame 事件, 包括用户输入和窗口关闭
        :param player: 玩家对象, 可选, 用于保存和加载游戏时使用
        """
        game_state = Settings.state
        for event in pygame.event.get():
            # 处理外部注册的事件
            for handler in self.event_handlers:
                handler.on_call(event)

            # 处理 pygame 事件的具体逻辑
            if event.type == pygame.QUIT:
                game.quit_game()
            elif event.type == pygame.KEYDOWN:
                if game_state == Settings.MENU:
                    if event.key == pygame.K_RETURN:
                        Settings.state = Settings.PLAYING
                    elif event.key == pygame.K_s:
                        Settings.state = Settings.SETTINGS
                    elif event.key == pygame.K_q:
                        game.quit_game()
                elif game_state == Settings.SETTINGS:
                    if event.key == pygame.K_ESCAPE:
                        Settings.state = Settings.MENU
                elif game_state == Settings.PLAYING:
                    if event.key == pygame.K_ESCAPE:
                        Settings.state = Settings.PAUSED
                    elif event.key == pygame.K_F5:
                        Settings.debug_mode = not Settings.debug_mode
                elif game_state == Settings.PAUSED:
                    if event.key in [pygame.K_p, pygame.K_ESCAPE]:
                        Settings.state = Settings.PLAYING
                    elif event.key == pygame.K_s:
                        game.graphic.save_game(self.screen, player)
                    elif event.key == pygame.K_l:
                        player = game.graphic.load_game(self.screen, player)
                    elif event.key == pygame.K_q:
                        game.quit_game()