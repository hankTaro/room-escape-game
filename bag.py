import os
import pygame
from user_request import *
from setting import *

# 待繪製物件
none_image = pygame.transform.scale(pygame.image.load(f"image/white.png"), (70, 70))

bag_image = pygame.transform.scale(pygame.image.load(f"image/bag.png"), (WIN_WIDTH, GAME_HEIGHT))
blank_image = pygame.transform.scale(pygame.image.load(f"image/Icon/blank.png"), (BLANK_SIZE, BLANK_SIZE))
blank_selected_image = pygame.transform.scale(pygame.image.load(f"image/Icon/blank_select.png"), (BLANK_SIZE, BLANK_SIZE))



class Blank:
    def __init__(self, x, y):
        self.image = blank_image
        # 被手持時的背景色
        self.selected_image = blank_selected_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        # 儲存此格子存放的物品
        self.item = None

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x - self.rect.x, y - self.rect.y)) != 0 and self.item is not None:
            return True
        else:
            return False



class Bag:
    def __init__(self):
        self.image = bag_image
        self.x = -50
        self.y = 50
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.mask = pygame.mask.from_surface(self.image)

        self.blank_x = 910 #885
        self.blank_y = 50 #70
        self.blank_tolerance = 80  # 885


        self.blank = [Blank(self.blank_x, self.blank_y),Blank(self.blank_x, self.blank_y + self.blank_tolerance),Blank(self.blank_x, self.blank_y + self.blank_tolerance * 2),
                      Blank(self.blank_x, self.blank_y + self.blank_tolerance * 3),Blank(self.blank_x, self.blank_y + self.blank_tolerance * 4),Blank(self.blank_x, self.blank_y + self.blank_tolerance * 5),
                      Blank(self.blank_x, self.blank_y),Blank(self.blank_x, self.blank_y + self.blank_tolerance),Blank(self.blank_x, self.blank_y + self.blank_tolerance * 2),
                      Blank(self.blank_x, self.blank_y + self.blank_tolerance * 3),Blank(self.blank_x, self.blank_y + self.blank_tolerance * 4),Blank(self.blank_x, self.blank_y + self.blank_tolerance * 5)]

        # 手持的物品(最多只能手持一個東西)
        self.hold = None
        self.hold_blank = None

        # 當前頁數(包包數量等於 頁數*6)
        self.page = 1

        # 最大包包頁數
        self.max_page = 2

    def save_item(self, item):
        for i in self.blank:
            if i.item == None:
                i.item = item
                break

    # 這邊統一由 bag 確認點擊後 在將點擊位置傳入各個blank
    def clicked(self, x: int, y: int):
        for i in self.blank[6 * (self.page - 1): 6 * self.page]:
            if i.clicked(x, y):
                # 手持的物品與點選的不同
                if self.hold != i.item:
                    self.hold = i.item
                    self.hold_blank = i
                # 手持的物品與點選的相同
                else:
                    self.hold = None
                    self.hold_blank = None
    def remove_hold_item(self):
        self.hold_blank.item = None
        self.hold = None
        self.hold_blank = None







