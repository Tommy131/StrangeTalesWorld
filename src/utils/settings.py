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
LastEditTime : 2024-07-24 00:39:13
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''
# settings.py

class Settings:
    # ~ 常量定义
    # 屏幕尺寸
    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080

    # FPS
    FPS = 60

    # 颜色
    TRANSPARENT = (0, 0, 0, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREY = (169, 169, 169)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    LIGHT_YELLOW = (255, 234, 0)

    # 方向
    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'
    DIRECTIONS = [LEFT, RIGHT, UP, DOWN]

    # 游戏状态
    MENU = 'menu'
    SETTINGS = 'settings'
    PLAYING = 'playing'
    PAUSED = 'paused'

    # 用户数据存储路径
    USER_PATH = './user/'
    SAVED_PATH = f'{USER_PATH}saved/'

    # 资源文件存储路径
    ASSETS_PATH = './assets/'
    IMAGE_PATH = f'{ASSETS_PATH}images/'
    FONT_PATH = f'{ASSETS_PATH}font/'

    # 字体
    FONT_CN = f'{FONT_PATH}SimHei.ttf'

    # 物品栏
    ITEM_SIZE = 50
    DISPLAY_ITEM_NUM = 7
    ITEM_PADDING = 5
    DURABILITY_BAR_HEIGHT = 5
    BG_COLOR = (30, 30, 30)

    # ~ 变量定义
    # 调试模式
    debug_mode = False

    # 当前屏幕状态
    state = MENU