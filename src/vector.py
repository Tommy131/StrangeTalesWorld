'''
       _____   _          __  _____   _____   _       _____   _____
     /  _  \ | |        / / /  _  \ |  _  \ | |     /  _  \ /  ___|
     | | | | | |  __   / /  | | | | | |_| | | |     | | | | | |
     | | | | | | /  | / /   | | | | |  _  { | |     | | | | | |   _
     | |_| | | |/   |/ /    | |_| | | |_| | | |___  | |_| | | |_| |
     \_____/ |___/|___/     \_____/ |_____/ |_____| \_____/ \_____/

Copyright (c) 2023 by OwOTeam-DGMT (OwOBlog).
Date         : 2024-07-22 17:47:39
Author       : HanskiJay
LastEditors  : HanskiJay
LastEditTime : 2024-07-22 17:49:45
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''

import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # 返回向量的字符串表示形式
    def __repr__(self):
        return f'Vector(x={self.x}, y={self.y})'

    # 向量加法
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError('Operand must be of type Vector')

    # 向量减法
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            raise TypeError('Operand must be of type Vector')

    # 向量与标量相乘
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        else:
            raise TypeError('Operand must be a number')

    # 向量与标量相除
    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            if scalar != 0:
                return Vector(self.x / scalar, self.y / scalar)
            else:
                raise ValueError('Division by zero is not allowed')
        else:
            raise TypeError('Operand must be a number')

    #  计算向量的模 (长度)
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # 将向量标准化为单位向量
    def normalize(self):
        mag = self.magnitude()
        if mag != 0:
            return self / mag
        else:
            return Vector(0, 0)

    # 计算两个向量的点积
    def dot(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError('Operand must be of type Vector')

    # 移动向量
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    # 更新坐标x
    def set_x(self, x):
        self.x = x
        return self

    # 更新坐标y
    def set_y(self, y):
        self.y = y
        return self