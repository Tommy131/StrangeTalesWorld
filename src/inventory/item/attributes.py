'''
       _____   _          __  _____   _____   _       _____   _____
     /  _  \ | |        / / /  _  \ |  _  \ | |     /  _  \ /  ___|
     | | | | | |  __   / /  | | | | | |_| | | |     | | | | | |
     | | | | | | /  | / /   | | | | |  _  { | |     | | | | | |   _
     | |_| | | |/   |/ /    | |_| | | |_| | | |___  | |_| | | |_| |
     \_____/ |___/|___/     \_____/ |_____/ |_____| \_____/ \_____/

 Copyright (c) 2023 by OwOTeam-DGMT (OwOBlog).
Date         : 2024-07-20 19:49:47
Author       : HanskiJay
LastEditors  : HanskiJay
LastEditTime : 2024-09-03 19:00:56
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''
# attributes.py

from inventory.item.gun import Gun
from inventory.item.sword import Sword

class AK47(Gun):
    def __init__(self):
        super().__init__(item_id=1947, name='AK-47', bullet_speed=15, damage=35, clip_size=30, attack_rate=100, color=(110, 38, 14))

    def image(self):
        return f'assets/img/weapons/gun/AK-47.png'

class M4A4(Gun):
    def __init__(self):
        super().__init__(item_id=1994, name='M4A4', bullet_speed=20, damage=30, clip_size=30, attack_rate=90, color=(69, 75, 27))

    def image(self):
        return f'assets/img/weapons/gun/M4A4.png'

class Negev(Gun):
    def __init__(self):
        super().__init__(item_id=1997, name='Negev', bullet_speed=10, damage=25, clip_size=150, attack_rate=50, color=(53, 94, 59))

    def image(self):
        return f'assets/img/weapons/gun/Negev.png'

class SG553(Gun):
    def __init__(self):
        super().__init__(item_id=2000, name='SG553', bullet_speed=20, damage=30, clip_size=30, attack_rate=90, color=(64, 130, 109))

    def image(self):
        return f'assets/img/weapons/gun/SG553.png'

# 新增武器, 暂时缺失图片资源
class Glock18(Gun):
    def __init__(self):
        super().__init__(item_id=1982, name='Glock-18', bullet_speed=12, damage=20, clip_size=17, attack_rate=120, color=(42, 42, 42))

    def image(self):
        return f'assets/img/weapons/gun/Glock-18.png'

class DesertEagle(Gun):
    def __init__(self):
        super().__init__(item_id=1983, name='Desert Eagle', bullet_speed=25, damage=50, clip_size=7, attack_rate=50, color=(128, 128, 128))

    def image(self):
        return f'assets/img/weapons/gun/Desert_Eagle.png'

class P90(Gun):
    def __init__(self):
        super().__init__(item_id=1990, name='P90', bullet_speed=20, damage=25, clip_size=50, attack_rate=150, color=(88, 92, 80))

    def image(self):
        return f'assets/img/weapons/gun/P90.png'

class UMP45(Gun):
    def __init__(self):
        super().__init__(item_id=1999, name='UMP-45', bullet_speed=18, damage=30, clip_size=25, attack_rate=100, color=(60, 60, 60))

    def image(self):
        return f'assets/img/weapons/gun/UMP-45.png'

class MP5(Gun):
    def __init__(self):
        super().__init__(item_id=1966, name='MP5', bullet_speed=20, damage=25, clip_size=30, attack_rate=110, color=(50, 50, 50))

    def image(self):
        return f'assets/img/weapons/gun/MP5.png'
# ---

# 根据类名创建枪械实例
def create_gun_instance(class_name):
    gun_classes = {
        'AK-47': AK47,
        'M4A4': M4A4,
        'Negev': Negev,
        'SG553': SG553,
        'Glock18': Glock18,
        'DesertEagle': DesertEagle,
        'P90': P90,
        'UMP45': UMP45,
        'MP5': MP5,

        'Sword': Sword
    }

    gun_class = gun_classes.get(class_name)
    if gun_class:
        return gun_class()
    else:
        raise ValueError(f"Unknown gun class name: {class_name}")