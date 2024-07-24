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
        """
        初始化一个新的 Vector 实例

        :param x: 向量的 x 分量
        :param y: 向量的 y 分量
        """
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector(x={self.x}, y={self.y})'
        """
        返回向量的字符串表示形式

        :return: 向量的字符串表示
        """

    def __add__(self, other):
        """
        实现向量加法

        :param other: 要加的向量
        :return: 结果向量
        :raises TypeError: 如果 other 不是 Vector 类型
        """
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError('Operand must be of type Vector')

    def __sub__(self, other):
        """
        实现向量减法

        :param other: 要减的向量
        :return: 结果向量
        :raises TypeError: 如果 other 不是 Vector 类型
        """
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            raise TypeError('Operand must be of type Vector')

    def __mul__(self, scalar):
        """
        实现向量与标量相乘

        :param scalar: 要乘的标量
        :return: 结果向量
        :raises TypeError: 如果 scalar 不是数字类型
        """
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        else:
            raise TypeError('Operand must be a number')

    def __truediv__(self, scalar):
        """
        实现向量与标量相除

        :param scalar: 要除的标量
        :return: 结果向量
        :raises TypeError: 如果 scalar 不是数字类型
        :raises ValueError: 如果 scalar 为 0
        """
        if isinstance(scalar, (int, float)):
            if scalar != 0:
                return Vector(self.x / scalar, self.y / scalar)
            else:
                raise ValueError('Division by zero is not allowed')
        else:
            raise TypeError('Operand must be a number')

    def magnitude(self):
        """
        计算向量的模 (长度)

        :return: 向量的模
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        """
        将向量标准化为单位向量

        :return: 标准化后的单位向量
        """
        mag = self.magnitude()
        if mag != 0:
            return self / mag
        else:
            return Vector(0, 0)

    def dot(self, other):
        """
        计算两个向量的点积

        :param other: 要计算点积的向量
        :return: 向量的点积
        :raises TypeError: 如果 other 不是 Vector 类型
        """
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError('Operand must be of type Vector')

    def move(self, dx, dy):
        """
        移动向量的位置

        :param dx: x 方向上的位移
        :param dy: y 方向上的位移
        """
        self.x += dx
        self.y += dy

    def set_x(self, x):
        """
        更新向量的 x 坐标

        :param x: 新的 x 坐标
        :return: 当前向量实例
        """
        self.x = x
        return self

    def set_y(self, y):
        """
        更新向量的 y 坐标

        :param y: 新的 y 坐标
        :return: 当前向量实例
        """
        self.y = y
        return self

    def get_pos(self):
        """
        返回向量元组

        :return: Tuple
        """
        return (self.x, self.y)