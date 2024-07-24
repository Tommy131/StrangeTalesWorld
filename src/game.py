'''
       _____   _          __  _____   _____   _       _____   _____
     /  _  \ | |        / / /  _  \ |  _  \ | |     /  _  \ /  ___|
     | | | | | |  __   / /  | | | | | |_| | | |     | | | | | |
     | | | | | | /  | / /   | | | | |  _  { | |     | | | | | |   _
     | |_| | | |/   |/ /    | |_| | | |_| | | |___  | |_| | | |_| |
     \_____/ |___/|___/     \_____/ |_____/ |_____| \_____/ \_____/

Copyright (c) 2023 by OwOTeam-DGMT (OwOBlog).
Date         : 2024-07-23 23:19:01
Author       : HanskiJay
LastEditors  : HanskiJay
LastEditTime : 2024-07-24 02:25:18
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''
# game.py
# ~ 游戏文件入口

import random
import pygame
import sys

from entity.player import Player

from event.event import Event
from event.debug_event_handler import DebugEventHandler

from inventory.item.item import Item
from inventory.item.weapon import Weapon

from ui.item_bar import ItemBar
from ui.weapon_roulette import WeaponRoulette

from utils.settings import Settings
from ui.graphic import Graphic

# 初始化游戏相关组件
graphic = Graphic()
event = Event(graphic.screen)
event.register(DebugEventHandler())

# 初始化玩家
player = Player(graphic.screen, name='HanskiJay')
player.vector.set_x(Settings.SCREEN_WIDTH // 2).set_y(Settings.SCREEN_HEIGHT // 2)

# 初始化玩家物品栏
player_equipped_items = player.inventory.get_item_details() if not player.inventory.is_empty() else [None] * Settings.DISPLAY_ITEM_NUM

# ! TODO: 测试数据, 记得删除
items = []
for i in range(7):
    # 随机生成数量
    quantity = random.randint(1, 10)

    # 随机生成耐久度，可能为 False 或 0 到 1 之间的随机值
    durability = random.choice([False] + [random.uniform(0.1, 1.0) for _ in range(3)])

    # 添加物品到列表
    items.append(Item(random.randint(10000, 99999), f'Item#{i}', main_image=None, quantity=quantity, durability=durability))
player_equipped_items = items
# ! ------------

item_bar = ItemBar(player_equipped_items)
event.register(item_bar)

# ! 创建虚拟武器数据 TODO: 测试数据, 记得删除
weapons = [
    Weapon("Pistol", color=Settings.RED, ammo=10, clip_size=15),
    Weapon("Rifle", color=Settings.GREY, ammo=30, clip_size=30),
    Weapon("Shotgun", color=Settings.WHITE, ammo=8, clip_size=8),
]
# ! ------------

# 创建 WeaponRoulette 实例
weapon_roulette = WeaponRoulette(weapons)
event.register(weapon_roulette)


def reset_game(message, use_popup=True, font=None, duration=2000):
    """
    重置游戏状态到菜单界面, 并可选地显示弹窗消息
    ! TODO: 保存游戏数据 & 重置游戏状态

    :param message: 弹窗中显示的消息内容
    :param use_popup: 是否显示弹窗, 默认为 True
    :param font: 用于弹窗的字体格式, 默认为 None
    :param duration: 弹窗显示的持续时间 (毫秒), 默认为 2000 毫秒
    """
    global player

    Settings.state = Settings.MENU
    player.reset()

    if use_popup:
        graphic.draw_popup_screen(message, font=font, duration=duration)

def quit_game():
    """
    退出游戏并关闭程序
    """
    print('Bye Bye~')
    pygame.quit()
    sys.exit()