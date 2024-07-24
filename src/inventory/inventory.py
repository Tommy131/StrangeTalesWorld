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
LastEditTime : 2024-07-24 00:32:58
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''
# inventory.py

from inventory.item.item import Item

class Inventory:
    def __init__(self, capacity=50):
        """
        初始化背包

        :param capacity: 背包容量
        """
        self.capacity = capacity
        self.items = {}

    def __len__(self):
        """
        返回背包物品数量

        :return: int
        """
        return len(self.items)

    def is_empty(self):
        """
        判断背包是否为空

        :return: bool
        """
        return len(self) == 0

    def has_item(self, item_id):
        """
        判断是否存在一个物品

        :param item_id: 物品ID
        :return: bool
        """
        return self.items.get(item_id, None) == None

    def get_item_detail(self, item_id):
        """
        返回背包的指定物品ID的数据

        :param item_id: 物品ID
        :return: dict
        """
        item = self.items.get(item_id, None)
        return {
                'main_image': item.main_image,
                'quantity': item.quantity,
                'durability': item.durability
            } if item != None else {}

    def get_item_details(self):
        """
        返回当前背包的所有物品数据

        :return: dict
        """
        data = {}
        for item in self.items:
            data[item.id] = self.get_item_detail(item.id)
        return data

    def get_equipped_item_details(self):
        """
        返回当前已装备的物品数据

        :return: list
        """
        data = []
        for item in self.items:
            if item.is_equipped():
                data.append({
                    'item_id': item.id,
                    'main_image': item.main_image,
                    'quantity': item.quantity,
                    'durability': item.durability
                })
        return data

    def add_item(self, item, quantity=1, durability=Item.DURABILITY):
        """
        添加物品到背包

        :param item: 物品对象
        :param quantity: 物品数量
        :return: bool
        """
        if len(self.items) < self.capacity:
            if item.id in self.items:
                self.items[item.id].update(quantity=quantity, durability=durability)
            else:
                self.items[item.id] = item
            self.capacity -= 1
            return True
        return False

    def add_item_from_id(self, item_id, quantity=1, durability=Item.DURABILITY):
        """
        通过 ID 添加物品

        :param item_id: 物品ID
        :param quantity: 数量, defaults to 1
        :param durability: 耐久性, defaults to Item.DURABILITY
        :return: bool
        """
        if item_id not in self.items:
            self.items[item_id] = Item(quantity, durability)
        else:
            self.items[item_id].update(quantity=self.items[item_id].quantity + quantity, durability=durability)
        self.capacity -= 1
        return True

    def remove_item(self, item_id, quantity=1):
        """
        通过 ID 移除物品

        :param item_id: 物品ID
        :param quantity: 数量, defaults to 1
        :return: bool
        """
        if item_id in self.items:
            self.items[item_id].remove_quantity(quantity)
            self.capacity += 1
            return True
        return False
