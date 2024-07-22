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
LastEditTime : 2024-07-23 01:50:49
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''
# utils.py

import pygame

def find_longest_element(input_list):
    """
    查找列表中最长的元素

    :param input_list: 要检查的列表
    :return: 列表中最长的元素如果列表为空, 则返回 None
    """
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

def load_image(filename):
    """
    从文件加载图片

    :param filename: 图片文件的路径
    :return: 加载的图片对象
    """
    return pygame.image.load(filename)

def scale_image(image, width, height):
    """
    调整图片的大小

    :param image: 要调整大小的图片对象
    :param width: 新的宽度
    :param height: 新的高度
    :return: 调整大小后的图片对象
    """
    return pygame.transform.scale(image, (width, height))
