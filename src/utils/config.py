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
        self.config_file = config_file
        self.settings = {
            'screen-width': Settings.SCREEN_WIDTH,
            'screen-height': Settings.SCREEN_HEIGHT,
            'fps': Settings.FPS,
            'debug-mode': Settings.debug_mode
        }
        self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                self.settings = json.load(f)
        else:
            self.save_config()

    def save_config(self):
        folder_path = os.path.dirname(self.config_file)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        with open(self.config_file, 'w') as f:
            json.dump(self.settings, f, indent=4)

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def set(self, key, value):
        self.settings[key] = value
        self.save_config()