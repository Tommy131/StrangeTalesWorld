'''
       _____   _          __  _____   _____   _       _____   _____
     /  _  \ | |        / / /  _  \ |  _  \ | |     /  _  \ /  ___|
     | | | | | |  __   / /  | | | | | |_| | | |     | | | | | |
     | | | | | | /  | / /   | | | | |  _  { | |     | | | | | |   _
     | |_| | | |/   |/ /    | |_| | | |_| | | |___  | |_| | | |_| |
     \_____/ |___/|___/     \_____/ |_____/ |_____| \_____/ \_____/

Copyright (c) 2023 by OwOTeam-DGMT (OwOBlog).
Date         : 2024-07-23 21:19:50
Author       : HanskiJay
LastEditors  : HanskiJay
LastEditTime : 2024-07-24 00:43:11
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''
# debug_event_handler.py
# ! TODO: 仅供测试使用, 记得删除!

import pygame

import game
from event.event_handler import EventHandler
from utils.settings import Settings

class DebugEventHandler(EventHandler):
    def on_call(self, event):
        """
        事件调用方法

        :param event: pygame 事件
        """
        if event.type == pygame.KEYDOWN and Settings.debug_mode and event.key == pygame.K_F2:
            game.reset_game('游戏状态已重置', font=Settings.FONT_CN)