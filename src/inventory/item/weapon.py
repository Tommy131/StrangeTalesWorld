'''
       _____   _          __  _____   _____   _       _____   _____
     /  _  \ | |        / / /  _  \ |  _  \ | |     /  _  \ /  ___|
     | | | | | |  __   / /  | | | | | |_| | | |     | | | | | |
     | | | | | | /  | / /   | | | | |  _  { | |     | | | | | |   _
     | |_| | | |/   |/ /    | |_| | | |_| | | |___  | |_| | | |_| |
     \_____/ |___/|___/     \_____/ |_____/ |_____| \_____/ \_____/

Copyright (c) 2023 by OwOTeam-DGMT (OwOBlog).
Date         : 2024-07-24 02:52:09
Author       : HanskiJay
LastEditors  : HanskiJay
LastEditTime : 2024-07-24 02:52:19
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''
class Weapon:
    def __init__(self, name, main_image=None, ammo=0, clip_size=0, color=(0, 0, 0)):
        self.name = name
        self.main_image = main_image
        self.ammo = ammo
        self.clip_size = clip_size
        self.color = color