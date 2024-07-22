'''
       _____   _          __  _____   _____   _       _____   _____
     /  _  \ | |        / / /  _  \ |  _  \ | |     /  _  \ /  ___|
     | | | | | |  __   / /  | | | | | |_| | | |     | | | | | |
     | | | | | | /  | / /   | | | | |  _  { | |     | | | | | |   _
     | |_| | | |/   |/ /    | |_| | | |_| | | |___  | |_| | | |_| |
     \_____/ |___/|___/     \_____/ |_____/ |_____| \_____/ \_____/

Copyright (c) 2023 by OwOTeam-DGMT (OwOBlog).
Date         : 2024-07-20 14:30:27
Author       : HanskiJay
LastEditors  : HanskiJay
LastEditTime : 2024-07-22 15:25:21
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''
# config.py

import json
import os

from utils.settings import Settings

class Config:
    def __init__(self, config_file=f'{Settings.USER_PATH}config.json'):
        """
        初始化配置对象, 并加载配置文件

        :param config_file: 配置文件的路径, 默认为 '{Settings.USER_PATH}config.json'
        """
        self.config_file = config_file
        self.settings = {
            'screen-width': Settings.SCREEN_WIDTH,
            'screen-height': Settings.SCREEN_HEIGHT,
            'fps': Settings.FPS,
            'debug-mode': Settings.debug_mode
        }
        self.load_config()

    def load_config(self):
        """
        加载配置文件中的设置. 如果文件不存在, 则创建一个默认配置文件
        """
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                self.settings = json.load(f)
        else:
            self.save_config()

    def save_config(self):
        """
        将当前设置保存到配置文件中. 如果配置文件所在的文件夹不存在, 则创建文件夹
        """
        folder_path = os.path.dirname(self.config_file)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        with open(self.config_file, 'w') as f:
            json.dump(self.settings, f, indent=4)

    def get(self, key, default=None):
        """
        获取指定键的配置值. 如果键不存在, 则返回默认值

        :param key: 配置项的键
        :param default: 键不存在时返回的默认值
        :return: 配置项的值或默认值
        """
        return self.settings.get(key, default)

    def set(self, key, value):
        """
        设置指定键的配置值, 并保存配置文件

        :param key: 配置项的键
        :param value: 配置项的值
        """
        self.settings[key] = value
        self.save_config()
