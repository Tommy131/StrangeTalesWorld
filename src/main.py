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
LastEditTime : 2024-07-24 00:18:06
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''
# main.py

import pygame

import game
from utils.settings import Settings

def is_playing():
    """
    根据当前游戏状态渲染对应的界面, 并返回是否处于游戏进行状态

    :param screen: 游戏窗口, 用于渲染界面
    :param graphic: 处理图形显示的对象
    :return: 布尔值, 表示是否处于游戏进行状态
    """
    game_state = Settings.state
    if game_state == Settings.MENU:
        game.graphic.draw_menu_screen()
    elif game_state == Settings.SETTINGS:
        game.graphic.draw_settings_screen()
    elif game_state == Settings.PAUSED:
        game.graphic.draw_pause_screen()
    elif game_state == Settings.PLAYING:
        return True
    return False

def main():
    """
    游戏主函数, 初始化 pygame, 设置玩家对象, 处理游戏循环和逻辑
    """

    # 主循环
    clock = pygame.time.Clock()
    running = True

    while running:
        # 监听事件处理
        game.event.pygame_event_handler()

        # 游戏中逻辑执行
        if is_playing():
            # 判断玩家是否存活
            if not game.player.is_alive():
                game.reset_game('Game Over!')
                continue

            # 清屏
            game.graphic.screen.blit(game.graphic.background_image, (0, 0))


            # ~[START] 游戏内逻辑执行区域

            keys = pygame.key.get_pressed()
            game.player.move(keys)
            game.player.draw()
            game.item_bar.draw()
            game.weapon_roulette.draw()

            # ~[END] -------------------


            # 绘制调试窗口
            if Settings.debug_mode:
                game.graphic.draw_debug_window([
                    'Version=0.0.1 (Build 202407220001) | DEBUG_MODE=ON',
                    f'FPS: {clock.get_fps()}',
                    f'Player Info: {game.player}'
                ], color=[
                    (0, 255, 255),
                    (250, 250, 51)
                ])
                # player.set_health(100)

            # 更新显示
            pygame.display.flip()

        # 控制帧率
        clock.tick(Settings.FPS)

if __name__ == '__main__':
    main()
