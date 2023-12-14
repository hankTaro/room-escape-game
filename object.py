import os
import pygame
from user_request import *
from setting import *

# TODO : 將所有物件的圖片匯入 並調整至合適大小
# 同個物件 不同狀況(像是開啟/關閉)可以用相同名字，後面用tv-1 tv-2 做區分
tv_image = [pygame.transform.scale(pygame.image.load(f"image/Object/Tv/tv-{i}.png"), (int(201), int(211))) for i in range(1)]
newspaper_image = [pygame.transform.scale(pygame.image.load(f"image/Object/Newspaper/newspaper-{i}.png"), (int(466//3.5), int(260//3.5))) for i in range(1)]

right_image = pygame.transform.scale(pygame.image.load(f"image/Icon/right.png"), (int(30), int(30)))
left_image = pygame.transform.scale(pygame.image.load(f"image/Icon/left.png"), (int(30), int(30)))
menu_image = pygame.transform.scale(pygame.image.load(f"image/Icon/left.png"), (int(30), int(30)))
exit_image = pygame.transform.scale(pygame.image.load(f"image/Icon/left.png"), (int(30), int(30)))

door_image = pygame.transform.scale(pygame.image.load(f"image/Object/door.png"), (int(200), int(400)))

# 選單按鈕
class MenuButton:
    def __init__(self, x, y):
        self.image = menu_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y):
            # 測試用
            print('menu btn been press')
            # TODO : 叫出暫停選單
            pass

class RightButton:
    def __init__(self, x, y):
        self.image = right_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y):
            return 'right'
        else:
            return 0

class LeftButton:
    def __init__(self, x, y):
        self.image = left_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y):
            return 'left'
        else:
            return 0

class ExitButton:
    def __init__(self, x, y):
        self.image = exit_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y):
            return 'stop_investigation'
        else:
            return 0


class DoorToBedroom:
    def __init__(self, x, y):
        self.image = door_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y):
            return 'bedroom'
        else:
            return 0


class DoorToLivingRoom:
    def __init__(self, x, y):
        self.image = door_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y):
            return 'living_room'
        else:
            return 0


# 可互動物件大概會是這個架構

# TV 會用到的原件 ===========================================
class TvButton:
    def __init__(self, x, y, num):
        self.image = pygame.transform.scale(pygame.image.load(f"image/Object/Tv/btn.png"), (50, 50))
        self.number = num
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x: int, y: int):
        # TODO : 再看看要回傳甚麼 以及怎麼監測
        if self.rect.collidepoint(x, y):
            # 測試
            print(self.number)

            return self.number
        else:
            return 0

# 可互動物件本身 ===========================================
class Tv:
    def __init__(self, x, y):
        self.image = tv_image[0]
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        # 下方要有儲存解謎進度的data
        # TODO : 點擊放大後的圖片
        self.focus = pygame.transform.scale(pygame.image.load(f"image/Object/Tv/tv-investigation.png"), (GAME_WIDTH, GAME_HEIGHT))
        # TODO : 此圖片中可互動的物件
        self.object = [ExitButton(500,550),
                       TvButton(600,200,1),TvButton(700,200,2),TvButton(800,200,3),
                       TvButton(600,300,4),TvButton(700,300,5),TvButton(800,300,6),
                       TvButton(600,400,7),TvButton(700,400,8),TvButton(800,400,9)]

    def clicked(self, x: int, y: int):
        # TODO : 連接到 user_request 若是可互動物件被點到 轉換場景 若是不可互動則說話或是
        if self.rect.collidepoint(x, y):
            return 'investigation'

    # TODO : 用於改變在解謎中改動到的資料
    def puzzle(self):
        pass


# NewPaper 會用到的原件 ===========================================


# 可互動物件本身 ===========================================
class NewPaper:
    def __init__(self, x, y):
        self.image = tv_image[0]
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        # 下方要有儲存解謎進度的data
        # TODO : 點擊放大後的圖片
        self.focus = pygame.transform.scale(pygame.image.load(f"image/Object/Tv/tv-investigation.png"), (GAME_WIDTH, GAME_HEIGHT))
        # TODO : 此圖片中可互動的物件
        self.object = [ExitButton(500,550)]

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y):
            return 'investigation'

    # TODO : 用於改變在解謎中改動到的資料
    def puzzle(self):
        pass


# # 可互動物件(點了會變大 而非只有文字敘述(不論是旁白或是主角說的話))
# class Interactive_objects:
#     def __init__(self, x: int, y: int, text, react, image):
#         self.image = image[0]
#         self.rect = self.image.get_rect()
#         self.rect.center = (x, y)
#
#         # TODO : 還沒想好架構要怎麼做
#         # 點擊後會被導入至哪個畫面
#         self.react = react
#         # 點擊後螢幕下方字幕區會顯示的文字
#         self.text = text
#         # 此物品是否被解謎成功
#
#     # TODO : 將所有物件列出他們個別的 class method
#     @classmethod
#     def Newspaper(cls, x, y):
#         text = "這是昨天的報紙..."
#         react = newspaper_cont
#         newspaper = cls(x, y, text, newspaper_image)
#         return newspaper
#
#     @classmethod
#     def Tv(cls, x, y):
#         text = "這是昨天的報紙..."
#         newspaper = cls(x, y, text, newspaper_image)
#         return newspaper
#
#     @classmethod
#     def Extinguisher(cls, x, y):
#         text = "這是昨天的報紙..."
#         newspaper = cls(x, y, text, newspaper_image)
#         return newspaper
#
#     def clicked(self, x, y):
#         return True if self.rect.collidepoint(x, y) else False
