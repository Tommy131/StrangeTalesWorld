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
LastEditTime : 2024-07-22 14:58:27
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''
# utils.py

import pygame

# 找出最长元素
def find_longest_element(input_list):
    # 检查输入列表是否为空
    if not input_list:
        return None

    # 初始化最长元素及其长度
    longest_element = ''
    max_length = 0

    # 遍历列表中的每个元素
    for element in input_list:
        # 计算当前元素的长度
        current_length = len(element)
        # 如果当前元素的长度大于已知最长元素的长度
        if current_length > max_length:
            longest_element = element
            max_length = current_length

    return longest_element

# 从文件加载图片
def load_image(filename):
    return pygame.image.load(filename)

# 调整图片大小
def scale_image(image, width, height):
    return pygame.transform.scale(image, (width, height))