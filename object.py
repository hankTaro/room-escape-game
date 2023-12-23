import os
import pygame
import cv2
import numpy as np
from user_request import *
from setting import *

# TODO : 將所有物件的圖片匯入 並調整至合適大小
# 同個物件 不同狀況(像是開啟/關閉)可以用相同名字，後面用tv-1 tv-2 做區分
# tv_image = [pygame.transform.scale(pygame.image.load(f"image/Object/Tv/tv-{i}.png"), (int(201), int(211))) for i in range(1)]
tv_image = [pygame.transform.scale(pygame.image.load(f"image/living_room/Tv/tv_{i}.png"), (GAME_WIDTH, GAME_HEIGHT)) for i in range(1)]
newspaper_image = [pygame.transform.scale(pygame.image.load(f"image/Object/Newspaper/newspaper_{i}.png"), (int(466//3), int(260//3))) for i in range(1)]

clock_image = pygame.transform.scale(pygame.image.load(f"image/living_room/Clock/clock.png"), (GAME_WIDTH, GAME_HEIGHT))
clock_open_image = pygame.transform.scale(pygame.image.load(f"image/living_room/Clock/clock_open.png"), (GAME_WIDTH, GAME_HEIGHT))
hr_image = [pygame.transform.scale(pygame.image.load(f"image/living_room/Clock/hr/hr_{i}.png"), (int(1920//2), int(1080//2))) for i in range(0,12)]
mins_image = [pygame.transform.scale(pygame.image.load(f"image/living_room/Clock/mins/mins_{i}.png"), (int(1920//2), int(1080//2))) for i in range(0,60,5)]

right_image = pygame.transform.scale(pygame.image.load(f"image/Icon/right.png"), (int(30), int(30)))
left_image = pygame.transform.scale(pygame.image.load(f"image/Icon/left.png"), (int(30), int(30)))
menu_image = pygame.transform.scale(pygame.image.load(f"image/Icon/menu.png"), (int(30), int(30)))
exit_image = pygame.transform.scale(pygame.image.load(f"image/Icon/left.png"), (int(30), int(30)))

door_image = pygame.transform.scale(pygame.image.load(f"image/Object/door.png"), (int(200), int(400)))
#yj
door_image_1  = pygame.transform.scale(pygame.image.load(f"image/living_room/Door/door_1.png"), (GAME_WIDTH, GAME_HEIGHT))
door_image_2  = pygame.transform.scale(pygame.image.load(f"image/living_room/Door/door_2.png"), (GAME_WIDTH, GAME_HEIGHT))
door_image_3  = pygame.transform.scale(pygame.image.load(f"image/living_room/Door/door_3.png"), (GAME_WIDTH, GAME_HEIGHT))
door_image_4  = pygame.transform.scale(pygame.image.load(f"image/living_room/Door/door_4.png"), (GAME_WIDTH, GAME_HEIGHT))
door_image_2_reverse  = pygame.transform.scale(pygame.image.load(f"image/study/door_2.png"), (GAME_WIDTH, GAME_HEIGHT))

desk_image = pygame.transform.scale(pygame.image.load(f"image/study/desk.png"), (GAME_WIDTH, GAME_HEIGHT))
book_image = pygame.transform.scale(pygame.image.load(f"image/study/book2.png"), (GAME_WIDTH, GAME_HEIGHT))
book_shelf_image = pygame.transform.scale(pygame.image.load(f"image/study/BookShelf/book_shelf.png"), (GAME_WIDTH, GAME_HEIGHT))
globe_image = pygame.transform.scale(pygame.image.load(f"image/study/Globe/globe.png"), (GAME_WIDTH, GAME_HEIGHT))
globe_table_image = pygame.transform.scale(pygame.image.load(f"image/study/Globe/globe_table.png"), (GAME_WIDTH, GAME_HEIGHT))
window_image = pygame.transform.scale(pygame.image.load(f"image/study/window.png"), (GAME_WIDTH, GAME_HEIGHT))
chest_image = pygame.transform.scale(pygame.image.load(f"image/study/Chest/chest.png"), (GAME_WIDTH, GAME_HEIGHT))
dropped_painting_image = pygame.transform.scale(pygame.image.load(f"image/study/dropped_painting.png"), (GAME_WIDTH, GAME_HEIGHT))
wife_1_image = pygame.transform.scale(pygame.image.load(f"image/Object/Wife/wife.png"), (GAME_WIDTH, GAME_HEIGHT))


tv_channel_1 = cv2.VideoCapture("image/living_room/Tv/TV_show/meme_1.mp4")
tv_channel_2 = cv2.VideoCapture("image/living_room/Tv/TV_show/tyler1 scream meme.mp4")
tv_channel_3 = pygame.transform.scale(pygame.image.load(f"image/living_room/Tv/TV_show/channel_1.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_channel_4 = cv2.VideoCapture("image/living_room/Tv/TV_show/Pornhub Video intro.mp4")
tv_channel_5 = cv2.VideoCapture("image/living_room/Tv/TV_show/KFC Chickendales Mother’s Day Performance.mp4")


tv_power_off_image = pygame.transform.scale(pygame.image.load(f"image/living_room/Tv/power_off.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_power_btn = pygame.transform.scale(pygame.image.load(f"image/living_room/Tv/power.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_switch_btn = pygame.transform.scale(pygame.image.load(f"image/living_room/Tv/switch.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_decipher_card_detail_image = pygame.transform.scale(pygame.image.load(f"image/living_room/Tv/tv_decipher_card.png"), (GAME_WIDTH, GAME_HEIGHT))

# tv_show_1_sound = pygame.mixer.Sound('image/TV_show/meme_1.mp3')

# 書架相關 ===================================================
book_shelf_puzzle = pygame.transform.scale(pygame.image.load(f"image/study/BookShelf/book_shelf_investigation.png"), (GAME_WIDTH, GAME_HEIGHT))
book_shelf_left_door_close_image = pygame.transform.scale(pygame.image.load(f"image/study/BookShelf/left_door_close.png"), (GAME_WIDTH, GAME_HEIGHT))
book_shelf_right_door_close_image = pygame.transform.scale(pygame.image.load(f"image/study/BookShelf/right_door_close.png"), (GAME_WIDTH, GAME_HEIGHT))
book_shelf_left_door_open_image = pygame.transform.scale(pygame.image.load(f"image/study/BookShelf/left_door_open.png"), (GAME_WIDTH, GAME_HEIGHT))
book_shelf_right_door_open_image = pygame.transform.scale(pygame.image.load(f"image/study/BookShelf/right_door_open.png"), (GAME_WIDTH, GAME_HEIGHT))

locker_image = pygame.transform.scale(pygame.image.load(f"image/study/Locker/locker.png"), (GAME_WIDTH, GAME_HEIGHT))
locker_setup_image = pygame.transform.scale(pygame.image.load(f"image/study/Locker/locker_setup.png"), (GAME_WIDTH, GAME_HEIGHT))
locker_open_image = pygame.transform.scale(pygame.image.load(f"image/study/Locker/locker_open.png"), (GAME_WIDTH, GAME_HEIGHT))

chest_key_image = pygame.transform.scale(pygame.image.load(f"image/study/Chest/chest_key.png"), (GAME_WIDTH, GAME_HEIGHT))

knob_0_image = [pygame.transform.scale(pygame.image.load(f"image/study/knob/knob_000{i}.png"), (GAME_WIDTH, GAME_HEIGHT)) for i in range(10)]
knob_1_image = [pygame.transform.scale(pygame.image.load(f"image/study/knob/knob_1_000{i}.png"), (GAME_WIDTH, GAME_HEIGHT)) for i in range(10)]
knob_2_image = [pygame.transform.scale(pygame.image.load(f"image/study/knob/knob_2_000{i}.png"), (GAME_WIDTH, GAME_HEIGHT)) for i in range(10)]
knob_3_image = [pygame.transform.scale(pygame.image.load(f"image/study/knob/knob_3_000{i}.png"), (GAME_WIDTH, GAME_HEIGHT)) for i in range(10)]
# 相框相關 ===========================================================
photo_frame_image = pygame.transform.scale(pygame.image.load(f"image/study/PhotoFrame/photo_frame.png"), (GAME_WIDTH, GAME_HEIGHT))
photo_fragments_image = [pygame.transform.scale(pygame.image.load(f"image/study/PhotoFrame/photo_{i}.png"), (GAME_WIDTH, GAME_HEIGHT)) for i in range(1)]
photo_frame_puzzle = pygame.transform.scale(pygame.image.load(f"image/study/PhotoFrame/photo_frame_puzzle.png"), (GAME_WIDTH, GAME_HEIGHT))

# 可拾取物件 ===========================================================
handle_image = pygame.transform.scale(pygame.image.load(f"image/living_room/Clock/Handle.png"), (GAME_WIDTH, GAME_HEIGHT))
password_hint_1_image = pygame.transform.scale(pygame.image.load(f"image/living_room/Clock/Password_Hint_1.png"), (GAME_WIDTH, GAME_HEIGHT))

# icon==================================================================
password_hint_1_icon = pygame.transform.scale(pygame.image.load(f"image/Icon/password_hint_1_icon.png"), (ICON_SIZE, ICON_SIZE))
handle_icon = pygame.transform.scale(pygame.image.load(f"image/Icon/handle_icon.png"), (ICON_SIZE, ICON_SIZE))
chest_key_icon = pygame.transform.scale(pygame.image.load(f"image/Icon/chest_key_icon.png"), (ICON_SIZE, ICON_SIZE))
tv_decipher_card_detail_icon = pygame.transform.scale(pygame.image.load(f"image/Icon/tv_decipher_card_detail_icon.png"), (ICON_SIZE, ICON_SIZE))
# 調查畫面===============================================================
password_hint_1_observe = pygame.image.load(f"image/Observe/password_hint_1_observe.png")
handle_observe = pygame.image.load(f"image/Observe/handle_observe.png")
chest_key_observe = pygame.image.load(f"image/Observe/chest_key_observe.png")

# XX相關 ===========================================================


# 待繪製物件
none_image = pygame.transform.scale(BACKGROUND_IMAGE, (100, 100))
none_icon = pygame.transform.scale(pygame.image.load(f"image/icon.png"), (ICON_SIZE, ICON_SIZE))
observe_image = pygame.image.load(f"image/Observe/observe.png")

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

            return 'menu'

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

#yj
class DoorToBedRoom:
    def __init__(self, x, y):
        self.image = door_image_3
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.lock = True
        self.speaker = "旁白"
        self.dialog = "你嘗試打開這個扭曲變形的門\n...\n你使勁全力依然打不開他"

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            if self.lock:
                return 'dialog'
            else:
                return 'bedroom'
        else:
            return 0

#把所有doors存成class attribute，用room id來決定要用哪一個圖片
class DoorToLivingRoom:
    doors = [door_image_2_reverse, door_image]
    def __init__(self, x, y, room):
        self.image = self.doors[room]
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'living_room'
        else:
            return 0
        
#yj living room通往外面的門
class DoorToExit:
    def __init__(self, x, y):
        self.image = door_image_1
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'exit' #亂打的
        else:
            return 0

#yj 往study的門
class DoorToStudy:
    def __init__(self, x, y):
        self.image = door_image_2
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'study'
        else:
            return 0
        
#yj 往kitchen的門
class DoorToKitchen:
    def __init__(self, x, y):
        self.image = door_image_4
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'kitchen'
        else:
            return 0

# 可互動物件大概會是這個架構

# TV 會用到的原件 ===========================================
class TvSwitch:
    def __init__(self, x, y):
        self.image = tv_switch_btn
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'switch'

class TvPower:
    def __init__(self, x, y):
        self.image = tv_power_btn
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'shotdown'

class TvShow:
    def __init__(self, x, y):
        self.all_show = [tv_channel_1,tv_channel_2,tv_channel_3,tv_channel_4,tv_channel_5]
        # self.sound = [tv_show_1_sound]
        self.index = 0
        self.size = len(self.all_show)
        self.image = self.all_show[self.index]
        self.power_off = tv_power_off_image
        # 影片位置起始點與長寬
        self.x = 110
        self.y = 130
        self.w = 470 # 設定影片用
        self.h = 300 # 設定影片用
        self.ispower = False
        pygame.time.set_timer(VIDEO_EVENT, int(2000 / FPS), 0)
        self.rect = self.power_off.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.power_off)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x - self.rect.x, y - self.rect.y)) != 0 and \
                self.index == 2 and self.ispower:
            return 'card'

    def switch(self):
        if self.ispower:
            self.index += 1
            if self.index == self.size:
                self.index = 0
            self.image = self.all_show[self.index]
    
    def power(self):
        self.ispower = not self.ispower


class TvDecipherCardPuzzle:
    def __init__(self, x, y):
        self.image = tv_decipher_card_detail_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.drag = False

    def clicked(self, x: int, y: int):
        # 除了被點到 還要確定滑鼠是按住的才能拖動
        if self.rect.collidepoint(x, y) and self.mask.get_at((x - self.rect.x, y - self.rect.y)) != 0:
            return 'drag'

    def drag_set(self):
        self.drag = True

    def release(self):
        self.drag = False

    def move(self, rel):
        if self.drag:
            self.rect.move_ip(rel)

# 可互動物件本身 ===========================================
class Tv:
    def __init__(self, x, y):
        self.image = tv_image[0]
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.tvshow = TvShow(GAME_X, GAME_Y)
        self.mask = pygame.mask.from_surface(self.image)

        # 入口 也就是上一層 離開調查時要回到的地方 None 代表離開調查
        self.enter = None

        # 是否放上了膠片
        self.card = False

        # 下方要有儲存解謎進度的data
        # TODO : 點擊放大後的圖片
        self.focus = pygame.transform.scale(pygame.image.load(f"image/living_room/Tv/tv_investigation.png"), (GAME_WIDTH, GAME_HEIGHT))
        # TODO : 此圖片中可互動的物件
        self.object = [ExitButton(500,550),TvSwitch(GAME_X, GAME_Y),TvPower(GAME_X, GAME_Y),self.tvshow]

    def clicked(self, x: int, y: int):
        # TODO : 連接到 user_request 若是可互動物件被點到 轉換場景 若是不可互動則說話或是
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'investigation'

    # TODO : 用於改變在解謎中改動到的資料
    def puzzle(self):
        pass


# Clock 會用到的物件 ===========================================

# yj clock時針
class Hr:
    def __init__(self, x, y):
        self.index = 0
        self.image = hr_image[0]
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.ans = 1 # 1點
        self.lock = False

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            # 檢查是否已解完
            if self.lock:
                return 'lock'
            if self.index == 11:
                self.index = 0
            else:
                self.index += 1
            self.image = hr_image[self.index]
            self.rect = self.image.get_rect()
            self.rect.center = (self.x, self.y)
            self.mask = pygame.mask.from_surface(self.image)
            return 'move'

# yj clock秒針
class Mins:
    def __init__(self, x, y):
        self.index = 0
        self.image = mins_image[0]
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.ans = 9 #45分
        self.lock = False

    def clicked(self, x: int, y: int):

        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            # 檢查是否已解完
            if self.lock:
                return 'lock'
            if self.index == 11:
                self.index = 0
            else:
                self.index += 1
            self.image = mins_image[self.index]
            self.rect = self.image.get_rect()
            self.rect.center = (self.x, self.y)
            self.mask = pygame.mask.from_surface(self.image)
            return 'move'

# 可互動物件本身 ===========================================
#yj
class Clock:
    def __init__(self,x,y):
        self.image = clock_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        # 入口 也就是上一層 離開調查時要回到的地方 None 代表離開調查
        self.enter = None
        self.focus = pygame.transform.scale(pygame.image.load(f"image/living_room/Clock/clock_investigation.png"), (GAME_WIDTH, GAME_HEIGHT))
        # TODO : 此圖片中可互動的物件
        self.object = [ExitButton(500,550),
                       Mins(483,400),Hr(483,400)]
        self.hr_right = False
        self.min_right = False
        self.is_open = False
    
    def clicked(self, x: int, y: int):
        # TODO : 連接到 user_request 若是可互動物件被點到 轉換場景 若是不可互動則說話或是
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'investigation'
    def open(self):
        self.is_open = True
        self.image = clock_open_image
        self.object[1].lock = True
        self.object[2].lock = True
        self.focus = pygame.transform.scale(pygame.image.load(f"image/living_room/Clock/clock_open_investigation.png"), (GAME_WIDTH, GAME_HEIGHT))
        self.object = [ExitButton(500,550),Handle(GAME_X, GAME_Y),Password_Hint_1(GAME_X, GAME_Y)]



# NewPaper 會用到的物件 ===========================================


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
        self.focus = pygame.transform.scale(pygame.image.load(f"image/living_room/Tv/tv_investigation.png"), (GAME_WIDTH, GAME_HEIGHT))
        # TODO : 此圖片中可互動的物件
        self.object = [ExitButton(500,550)]

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y):
            return 'investigation'

    # TODO : 用於改變在解謎中改動到的資料
    def puzzle(self):
        pass

# Desk 會用到的物件 ===========================================
class Letter:
    def __init__(self, x, y, num):
        self.image = None
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
class Desk:
    def __init__(self, x, y):
        self.image = desk_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

        # 入口 也就是上一層 離開調查時要回到的地方 None 代表離開調查
        self.enter = None

        # 下方要有儲存解謎進度的data
        # TODO : 點擊放大後的圖片
        self.focus = pygame.transform.scale(pygame.image.load(f"image/living_room/Tv/tv_investigation.png"), (GAME_WIDTH, GAME_HEIGHT))
        # TODO : 此圖片中可互動的物件
        self.object = [ExitButton(500,550)]

    def clicked(self, x: int, y: int):
        # TODO : 連接到 user_request 若是可互動物件被點到 轉換場景 若是不可互動則說話或是
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'investigation'

    # TODO : 用於改變在解謎中改動到的資料
    def puzzle(self):
        pass



# 我打算把他與書桌合併(圖片上) 就不必宣告這個class by hank
#不確定是不是可互動物件
class Book:
    def __init__(self, x, y):
        self.image = book_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
    
    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'none'

# BookShelf 會用到的物件 ===========================================
class RightDoor:
    def __init__(self, x, y):
        self.image = book_shelf_right_door_close_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.open = False
    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            if self.open == False:
                self.open = True
                self.image = book_shelf_right_door_open_image
            else:
                self.open = False
                self.image = book_shelf_right_door_close_image
            self.rect = self.image.get_rect()
            self.rect.topleft = (self.x, self.y)
            self.mask = pygame.mask.from_surface(self.image)
            return 'door'

class LeftDoor:
    def __init__(self, x, y):
        self.image = book_shelf_left_door_close_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.open = False
    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            if self.open == False:
                self.open = True
                self.image = book_shelf_left_door_open_image
            else:
                self.open = False
                self.image = book_shelf_left_door_close_image
            self.rect = self.image.get_rect()
            self.rect.topleft = (self.x, self.y)
            self.mask = pygame.mask.from_surface(self.image)
            return 'door'

class Knob:
    def __init__(self, x, y, num):
        self.num = num
        self.index = 0
        self.x = x
        self.y = y
        self.image = globals()[f"knob_{self.num}_image"][self.index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            self.index += 1
            if self.index == 10:
                self.index = 0
            self.image = globals()[f"knob_{self.num}_image"][self.index]
            return 'knob'


class Locker:
    def __init__(self, x, y):
        self.all_image = [locker_image,locker_setup_image,locker_open_image]
        self.index = 0
        self.x = x
        self.y = y
        self.image = self.all_image[self.index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        #是否開啟
        self.open = False
        # 是否安裝好手把
        self.setup = False

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            if self.open == False:
                if self.setup == False:
                    return 'close'
                else:
                    return 'check'
            else:
                pass
    def add_handle(self):
        self.index += 1
        self.image = self.all_image[self.index]
        self.setup = True
    def unlock(self):
        self.index += 1
        self.image = self.all_image[self.index]
        self.open = True

#可互動物件
class BookShelf:
    def __init__(self, x, y):
        self.image = book_shelf_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

        # 入口 也就是上一層 離開調查時要回到的地方 None 代表離開調查
        self.enter = None

        self.focus = book_shelf_puzzle
        self.object = [ExitButton(500, 550), PhotoFrame(GAME_X, GAME_Y), ChestKey(GAME_X, GAME_Y),
                       Knob(GAME_X, GAME_Y, 0), Knob(GAME_X, GAME_Y, 1), Knob(GAME_X, GAME_Y, 2), Knob(GAME_X, GAME_Y, 3)
            , Locker(GAME_X, GAME_Y), RightDoor(GAME_X, GAME_Y), LeftDoor(GAME_X, GAME_Y)]
        # locker 的密碼相關
        self.ans = [4, 2, 7, 5]
        self.input = [0, 0, 0, 0]
        self.unlock = False

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'investigation'
    def remove_knob(self):
        self.object = [item for item in self.object if not isinstance(item, Knob)]
# 相框謎題 ======================================================================
class PhotoFragments:
    def __init__(self, x, y, num):
        self.num = num
        self.image = photo_fragments_image[num]
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.drag = False
        self.ans = pygame.Rect(GAME_X - 15,GAME_Y - 15,30,30)

        # 因為碎片也是用畫面大小輸出 只是涂色位置不同 所以所有碎片對準 GAME_X, GAME_Y 就會是正確位置

    def clicked(self, x: int, y: int):
        # 除了被點到 還要確定滑鼠是按住的才能拖動
        if self.rect.collidepoint(x, y) and self.mask.get_at((x - self.rect.x, y - self.rect.y)) != 0:
            return 'drag'
    def drag_set(self):
        self.drag = True
        # self.rect.move_ip(event.rel)
    def release(self):
        correct_position = (GAME_X, GAME_Y)
        # 畫面重疊區域大小必需高於此
        min_intersection_width = self.rect.width * 0.95
        min_intersection_height = self.rect.height * 0.95
        self.drag = False
        if self.rect.colliderect(pygame.Rect(correct_position, self.rect.size)):
            intersection = self.rect.clip(pygame.Rect(correct_position, self.rect.size))
            if intersection.width >= min_intersection_width and intersection.height >= min_intersection_height:
                print("拼圖正確放置！且相交區域足夠大")
    def move(self, rel):
        if self.drag:
            self.rect.move_ip(rel)

class PhotoFrame:
    def __init__(self, x, y):
        self.image = photo_frame_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

        # 入口 也就是上一層 離開調查時要回到的地方 None 代表離開調查
        self.enter = None
        self.focus = none_image
        # 這裡的起始位置要手動調整，使得碎片一開始疊在向框的外面
        self.object = [ExitButton(500, 550),PhotoFragments(GAME_X + 100, GAME_Y + 10, 0)]
    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'investigation'
# 相框謎題 ======================================================================

#可互動物件，investigation尚未完成
class Globe:
    def __init__(self, x, y):
        self.image = globe_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'none'

#可互動物件，investigation尚未完成        
class DroppedPainting:
    def __init__(self, x, y):
        self.image = dropped_painting_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'none'


# 非可互動物件
class Window:
    def __init__(self, x, y):
        self.image = window_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x - self.rect.x, y - self.rect.y)) != 0:
            return 'none'


# 非可互動物件
class GlobeTable:
    def __init__(self, x, y):
        self.image = globe_table_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x - self.rect.x, y - self.rect.y)) != 0:
            return 'none'


# 非可互動物件
class Chest:
    def __init__(self, x, y):
        self.image = chest_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x - self.rect.x, y - self.rect.y)) != 0:
            return 'none'

# 對話物件 ===========================================
class Wife_Ch1:
    def __init__(self, x, y):
        self.image = wife_1_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        # 對話內容
        self.text = ["要是能回到過去該有多好⋯","你找到遺產了嗎?"]
        self.text_index = 0
        self.text_size = 2


    def clicked(self, x: int, y: int):
        # TODO : 連接到 user_request 若是可互動物件被點到 轉換場景 若是不可互動則說話或是
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'speak'


# 物品欄物件(可放入物品欄的東西)
class Handle:
    def __init__(self, x, y):
        self.name = "把手"
        self.image = handle_image
        # 放入物品欄後顯示的圖示
        self.icon = handle_icon
        # 調查中此物品的樣貌
        self.observe = handle_observe
        # 調查中此物品的敘述
        self.description = "老舊的把手，十分沉重\n" \
                           "裏頭有個凹槽，似乎可以插進甚麼地方"
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
    # TODO : 一些交互用函式
    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            # 被撿起放入物品欄
            return 'take'

class Password_Hint_1:
    def __init__(self, x, y):
        self.name = "皺巴巴的筆記"
        self.image = password_hint_1_image
        self.icon = password_hint_1_icon
        # 調查中此物品的樣貌
        self.observe = password_hint_1_observe
        # 調查中此物品的敘述
        self.description = "一個皺巴巴的筆記\n" \
                           "已經放到泛黃了\n" \
                           "上頭寫著:" \
                           "A + B = 6\n" \
                           "A + C = 11\n" \
                           "B + D = C\n" \
                           "A + D = B + C"
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
    # TODO : 一些交互用函式

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            # 被撿起放入物品欄
            return 'take'

class ChestKey:
    def __init__(self, x, y):
        self.name = "黃色鑰匙"
        self.image = chest_key_image
        self.icon = chest_key_icon
        # 調查中此物品的樣貌
        self.observe = chest_key_observe
        # 調查中此物品的敘述
        self.description = "有著些許鏽斑的黃色鑰匙\n" \
                           "不知道能打開哪道索"
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)


    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            # 被撿起放入物品欄
            return 'take'


class TvDecipherCard:
    def __init__(self, x, y):
        self.name = "佈滿洞的膠片"
        self.image = none_image
        self.icon = tv_decipher_card_detail_icon
        # 調查中此物品的樣貌
        self.observe = tv_decipher_card_detail_image
        # 調查中此物品的敘述
        self.description = "一張佈滿洞的膠片，上面還畫著時鐘的圖案\n" \
                           "中間還有著一個像是用於校準的孔洞\n" \
                           "或許是某種用於加密與破譯的工具..."
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)


    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            # 被撿起放入物品欄
            return 'take'

