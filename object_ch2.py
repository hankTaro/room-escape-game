import os
import pygame
import cv2
import numpy as np
from user_request import *
from setting import *
from show import *
from object import ExitButton

# TODO : 將所有物件的圖片匯入 並調整至合適大小
# 同個物件 不同狀況(像是開啟/關閉)可以用相同名字，後面用tv-1 tv-2 做區分
# tv_image = [pygame.transform.scale(pygame.image.load(f"image/Object/Tv/tv-{i}.png"), (int(201), int(211))) for i in range(1)]
pygame.mixer.init()
pygame.mixer.music.set_volume(0.2)
# 時鐘 ======================================================================================================
clock_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/Clock/clock.png"), (GAME_WIDTH, GAME_HEIGHT))
# 窗戶 ======================================================================================================
living_room_window_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/Window/window.png"), (GAME_WIDTH, GAME_HEIGHT))
# 門 ========================================================================================================
door_image_1  = pygame.transform.scale(pygame.image.load(f"image/Ch2/Door/door_1.png"), (GAME_WIDTH, GAME_HEIGHT))
door_image_2  = pygame.transform.scale(pygame.image.load(f"image/Ch2/Door/door_2.png"), (GAME_WIDTH, GAME_HEIGHT))
door_image_3  = pygame.transform.scale(pygame.image.load(f"image/Ch2/Door/door_3.png"), (GAME_WIDTH, GAME_HEIGHT))
door_image_4  = pygame.transform.scale(pygame.image.load(f"image/Ch2/Door/door_4.png"), (GAME_WIDTH, GAME_HEIGHT))
# 書桌 ======================================================================================================
desk_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/Desk/desk.png"), (GAME_WIDTH, GAME_HEIGHT))
# 電視櫃相關 =================================================================================================
tv_shelf_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/TvShelf/tv_shelf.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_shelf_investigation_l = pygame.transform.scale(pygame.image.load(f"image/Ch2/TvShelf/tv_shelf_investigation_l.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_shelf_investigation_r = pygame.transform.scale(pygame.image.load(f"image/Ch2/TvShelf/tv_shelf_investigation_r.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_shelf_left_door_close_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/TvShelf/tv_shelf_door_close_l.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_shelf_right_door_close_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/TvShelf/tv_shelf_door_close_r.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_shelf_left_door_open_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/TvShelf/tv_shelf_door_open_l.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_shelf_right_door_open_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/TvShelf/tv_shelf_door_open_r.png"), (GAME_WIDTH, GAME_HEIGHT))
# 電視相關 ==================================================================================================
tv_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/Tv/tv.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_power_off_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/Tv/power_off.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_power_btn = pygame.transform.scale(pygame.image.load(f"image/Ch2/Tv/power.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_switch_btn = pygame.transform.scale(pygame.image.load(f"image/Ch2/Tv/switch.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_decipher_card_detail_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/Tv/tv_decipher_card.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_channel_1 = cv2.VideoCapture("image/Ch2/Tv/TV_show/meme_1.mp4")
tv_channel_2 = cv2.VideoCapture("image/Ch2/Tv/TV_show/tyler1 scream meme.mp4")
tv_channel_3 = pygame.transform.scale(pygame.image.load(f"image/Ch2/Tv/TV_show/channel_1.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_channel_4 = cv2.VideoCapture("image/Ch2/Tv/TV_show/Pornhub Video intro.mp4")
tv_channel_5 = cv2.VideoCapture("image/Ch2/Tv/TV_show/KFC Chickendales Mother’s Day Performance.mp4")
# 寶箱 =====================================================================================================
chest_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/TvShelf/chest.png"), (GAME_WIDTH, GAME_HEIGHT))
# 地球儀 ===================================================================================================
globe_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/Globe/globe.png"), (GAME_WIDTH, GAME_HEIGHT))
globe_table_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/Globe/globe_table.png"), (GAME_WIDTH, GAME_HEIGHT))
# 書架相關 =================================================================================================
book_shelf_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/BookShelf/book_shelf.png"), (GAME_WIDTH, GAME_HEIGHT))
book_shelf_puzzle = pygame.transform.scale(pygame.image.load(f"image/Ch2/BookShelf/book_shelf_investigation.png"), (GAME_WIDTH, GAME_HEIGHT))
book_shelf_left_door_close_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/BookShelf/left_door_close.png"), (GAME_WIDTH, GAME_HEIGHT))
book_shelf_right_door_close_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/BookShelf/right_door_close.png"), (GAME_WIDTH, GAME_HEIGHT))
book_shelf_left_door_open_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/BookShelf/left_door_open.png"), (GAME_WIDTH, GAME_HEIGHT))
book_shelf_right_door_open_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/BookShelf/right_door_open.png"), (GAME_WIDTH, GAME_HEIGHT))
# 書架保險箱 ===============================================================================================
locker_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/Bookshelf/Locker/locker.png"), (GAME_WIDTH, GAME_HEIGHT))
locker_setup_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/Bookshelf/Locker/locker_setup.png"), (GAME_WIDTH, GAME_HEIGHT))
locker_open_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/Bookshelf/Locker/locker_open.png"), (GAME_WIDTH, GAME_HEIGHT))
# 書架保險箱密碼 ===========================================================================================
knob_0_image = [pygame.transform.scale(pygame.image.load(f"image/Ch2/Bookshelf/knob/knob_000{i}.png"), (GAME_WIDTH, GAME_HEIGHT)) for i in range(10)]
knob_1_image = [pygame.transform.scale(pygame.image.load(f"image/Ch2/Bookshelf/knob/knob_1_000{i}.png"), (GAME_WIDTH, GAME_HEIGHT)) for i in range(10)]
knob_2_image = [pygame.transform.scale(pygame.image.load(f"image/Ch2/Bookshelf/knob/knob_2_000{i}.png"), (GAME_WIDTH, GAME_HEIGHT)) for i in range(10)]
knob_3_image = [pygame.transform.scale(pygame.image.load(f"image/Ch2/Bookshelf/knob/knob_3_000{i}.png"), (GAME_WIDTH, GAME_HEIGHT)) for i in range(10)]
# 書櫃鑰匙 ================================================================================================
chest_key_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/BookShelf/chest_key.png"), (GAME_WIDTH, GAME_HEIGHT))
# icon ===================================================================================================
chest_key_icon = pygame.transform.scale(pygame.image.load(f"image/Icon/chest_key_icon.png"), (ICON_SIZE, ICON_SIZE))
# 調查畫面===============================================================
chest_key_observe = pygame.image.load(f"image/Observe/chest_key_observe.png")

# 聲音
tv_show_1_sound = pygame.mixer.Sound('music/meme_1.wav')
tv_show_2_sound = pygame.mixer.Sound('music/tyler1 scream meme.wav')
tv_show_4_sound = pygame.mixer.Sound('music/Pornhub Video intro.wav')
tv_show_5_sound = pygame.mixer.Sound('music/KFC Chickendales Mother’s Day Performance.wav')
clock_sound = pygame.mixer.Sound('music/clock.wav')
clock_hand_sound = pygame.mixer.Sound('music/clock_hand.wav')
walking_sound = pygame.mixer.Sound('music/walking.wav')
door_open_sound = pygame.mixer.Sound('music/door_open.wav')
tv_change_channel_sound = pygame.mixer.Sound('music/tv_change_channel.wav')
tv_power_sound = pygame.mixer.Sound('music/tv_change_channel.wav')
knob_twist_sound = pygame.mixer.Sound('music/knob_twist.wav')
knob_open_sound = pygame.mixer.Sound('music/knob_open.wav')
locker_setup_sound = pygame.mixer.Sound('music/locker_setup.wav')
locker_open_sound = pygame.mixer.Sound('music/locker_open.wav')
little_cabinet_open_sound = pygame.mixer.Sound('music/little_cabinet_open.wav')
little_cabinet_close_sound = pygame.mixer.Sound('music/little_cabinet_close.wav')
cheat_code_sound = pygame.mixer.Sound('music/cheat_code.mp3')
glass_sound = pygame.mixer.Sound('music/glass.wav')
card_collide_sound = pygame.mixer.Sound('music/card_collide.wav')
paper_sound = pygame.mixer.Sound('music/paper.wav')
door_locked_sound = pygame.mixer.Sound('music/door_locked.wav')
rock_sound = pygame.mixer.Sound('music/rock.wav')
rust_sound = pygame.mixer.Sound('music/rust.wav')
clicked_sound = pygame.mixer.Sound('music/clicked.wav')
pick_up_items_sound = pygame.mixer.Sound('music/物品拾取聲.mp3')

# 門 ===========================================================================
class DoorToExitCh2:
    def __init__(self, x, y):
        self.image = door_image_1
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

        self.speaker = "旁白"
        self.dialog = "離開房屋的門\n手把上充滿著鏽蝕與歲月痕跡\n" \
                      "在你進屋開門時，他發出了吵雜的摩擦噪音" #\n千里迢迢來到這裡可不只是為了進來撇一眼的\n你使勁全力依然打不開他
        self.music = door_open_sound

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'done'
        else:
            return 0

class DoorToStudyCh2:
    def __init__(self, x, y):
        self.image = door_image_2
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.music = door_open_sound

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            self.music.play()
            return 'study'
        else:
            return 0

class DoorToBedRoomCh2:
    def __init__(self, x, y):
        self.image = door_image_3
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.lock = True
        self.speaker = ["旁白","","旁白"]
        self.dialog = ["你嘗試打開這個扭曲變形的門,","...","你使勁全力依然打不開他"]
        # self.locked_music = [(door_locked_sound,1)]
        self.music = [(door_locked_sound,1)]

        self.show = Show(self.dialog, self.speaker, None, self.music, None)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            if self.lock:
                # self.locked_music.play()
                return 'dialog'
            else:
                self.music.play()
                return 'bedroom'
        else:
            return 0
        
class DoorToKitchenCh2:
    def __init__(self, x, y):
        self.image = door_image_4
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

        self.speaker = ["旁白","","旁白"]
        self.speaker_2 = ["旁白"]
        self.dialog = ["這條通往廚房的通道已經被碎石瓦礫掩埋了\n你靠近嘗試挖掘...","..." ,
                      "挖掘的好一陣子，碎石瓦礫依舊阻擋著通道\n但是你在瓦礫堆中找到了一張...膠片?"]
        self.dialog_2 = ["你看著自己紅腫刺痛的手，想想還是別再挖了好了"]
        # 已獲得膠片
        self.lock = True
        self.give = None
        self.music = [(rock_sound,1)]

        self.show = Show(self.dialog, self.speaker, None, self.music, None)
        self.show_2 = Show(self.dialog_2, self.speaker_2, None, None, None)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            if self.lock == False:
                # self.music.play()
                return 'dialog_sp'
            else:
                return 'dialog'
        else:
            return 0

# 窗戶 ==================================================================================================
class LivingRoomWindowCh2:
    def __init__(self, x, y):
        self.image = living_room_window_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

        self.music = [(glass_sound,0)]

        self.speaker = ["旁白"]
        self.dialog = ["寒冷的空氣從破碎的窗戶灌入\n破碎的玻璃映出你疲憊的臉\n" 
                      "前往這裡的過程顯然耗費了你許多心神..."]
        self.show = Show(self.dialog,self.speaker,None,self.music,None)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x - self.rect.x, y - self.rect.y)) != 0:
            # self.music.play()
            return 'dialog'
        
# 時鐘 =====================================================================================================
class ClockCh2:
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
        self.object = [ExitButton(500,550)]
        self.hr_right = False
        self.min_right = False
        self.is_open = False
        self.music = clock_sound
    
    def clicked(self, x: int, y: int):
        # TODO : 連接到 user_request 若是可互動物件被點到 轉換場景 若是不可互動則說話或是
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'investigation'
    def open(self):
        self.is_open = True
        self.object[1].lock = True
        self.object[2].lock = True
        self.focus = pygame.transform.scale(pygame.image.load(f"image/living_room/Clock/clock_open_investigation.png"), (GAME_WIDTH, GAME_HEIGHT))
        self.object = [ExitButton(500,550)]
        self.music.play()

# BookShelf 會用到的物件 ===========================================
class RightDoorCh2:
    def __init__(self, x, y):
        self.image = book_shelf_right_door_close_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.open = False
        self.open_music = little_cabinet_open_sound
        self.close_music = little_cabinet_close_sound
    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            if self.open == False:
                self.open = True
                self.image = book_shelf_right_door_open_image
                self.open_music.play()
            else:
                self.open = False
                self.image = book_shelf_right_door_close_image
                self.close_music.play()
            self.rect = self.image.get_rect()
            self.rect.topleft = (self.x, self.y)
            self.mask = pygame.mask.from_surface(self.image)
            return 'door'

class LeftDoorCh2:
    def __init__(self, x, y):
        self.image = book_shelf_left_door_close_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.open = False
        self.open_music = little_cabinet_open_sound
        self.close_music = little_cabinet_close_sound
    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            if self.open == False:
                self.open = True
                self.image = book_shelf_left_door_open_image
                self.open_music.play()
            else:
                self.open = False
                self.image = book_shelf_left_door_close_image
                self.close_music.play()
            self.rect = self.image.get_rect()
            self.rect.topleft = (self.x, self.y)
            self.mask = pygame.mask.from_surface(self.image)
            return 'door'

class KnobCh2:
    def __init__(self, x, y, num):
        self.num = num
        self.index = 0
        self.x = x
        self.y = y
        self.image = globals()[f"knob_{self.num}_image"][self.index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.music = knob_twist_sound
    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            self.music.play()
            self.index += 1
            if self.index == 10:
                self.index = 0
            self.image = globals()[f"knob_{self.num}_image"][self.index]
            return 'knob'


class LockerCh2:
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
        self.setup_music = locker_setup_sound
        self.open_music = locker_open_sound

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
        self.setup_music.play()
    def unlock(self):
        self.index += 1
        self.image = self.all_image[self.index]
        self.open = True
        self.open_music.play()

# 書架 ===================================================================================================
class BookShelfCh2:
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
        self.object = [ExitButton(500, 550), ChestKeyCh2(GAME_X, GAME_Y), 
                       KnobCh2(GAME_X, GAME_Y, 0), KnobCh2(GAME_X, GAME_Y, 1), KnobCh2(GAME_X, GAME_Y, 2), KnobCh2(GAME_X, GAME_Y, 3),
                       LockerCh2(GAME_X, GAME_Y), RightDoorCh2(GAME_X, GAME_Y), LeftDoorCh2(GAME_X, GAME_Y)]
        # locker 的密碼相關
        self.ans = [4, 2, 7, 5]
        self.input = [0, 0, 0, 0]
        self.unlock = False

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'investigation'
        
# 畫作相關
class DecipherCardPuzzleCh2:
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

# TV 會用到的原件 ===========================================
class TvSwitchCh2:
    def __init__(self, x, y):
        self.image = tv_switch_btn
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.music = tv_change_channel_sound

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'switch'

class TvPowerCh2:
    def __init__(self, x, y,lock):
        self.image = tv_power_btn
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.music = tv_power_sound

        self.speaker = [""]
        self.dialog = ["打不開...\n也是，就算電視沒壞，這裡也早就沒電、沒訊號了\n電視下面的這串指令...\n還真是懷念..."]
        # 是否壞掉(第一章不可互動)
        self.lock = lock
        self.music = None # TODO : 電視按鈕聲音(機械)

        self.show = Show(self.dialog, self.speaker, None, self.music, None)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            if self.lock:
                return 'dialog'
            else:
                self.music.play()
                return 'shotdown'

class TvShowCh2:
    def __init__(self, x, y):
        self.all_show = [tv_channel_1,tv_channel_2,tv_channel_3,tv_channel_4,tv_channel_5]
        self.all_music = [tv_show_1_sound,tv_show_2_sound,0,tv_show_4_sound,tv_show_5_sound]
        self.index = 0
        self.size = len(self.all_show)
        self.image = self.all_show[self.index]
        self.music = self.all_music[self.index]
        self.power_off = tv_power_off_image
        # 影片位置起始點與長寬
        self.x = 110
        self.y = 130
        self.w = 470 # 設定影片用
        self.h = 300 # 設定影片用
        self.ispower = False
        # pygame.time.set_timer(VIDEO_EVENT, int(2000 / FPS), 0)
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
            if self.music:
                self.music.stop()
            self.music = self.all_music[self.index]
            if self.music:
                self.music.play()
    
    def power(self):
        self.ispower = not self.ispower
        if self.ispower:
            if self.music:
                self.music.play()
        else:
            if self.music:
                self.music.stop()

# 電視櫃相關 ===============================================================
class TvShelfRightDoorCh2:
    def __init__(self, x, y):
        self.image = tv_shelf_right_door_close_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.open = False
        self.open_music = little_cabinet_open_sound
        self.close_music = little_cabinet_close_sound
    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            if self.open == False:
                self.open = True
                self.image = tv_shelf_right_door_open_image
                self.open_music.play()
            else:
                self.open = False
                self.image = tv_shelf_right_door_close_image
                self.close_music.play()
            self.rect = self.image.get_rect()
            self.rect.topleft = (self.x, self.y)
            self.mask = pygame.mask.from_surface(self.image)
            return 'door'

class TvShelfLeftDoorCh2:
    def __init__(self, x, y):
        self.image = tv_shelf_left_door_close_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.open = False
        self.open_music = little_cabinet_open_sound
        self.close_music = little_cabinet_close_sound
    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            if self.open == False:
                self.open = True
                self.image = tv_shelf_left_door_open_image
                self.open_music.play()
            else:
                self.open = False
                self.image = tv_shelf_left_door_close_image
                self.close_music.play()
            self.rect = self.image.get_rect()
            self.rect.topleft = (self.x, self.y)
            self.mask = pygame.mask.from_surface(self.image)
            return 'door'
        
class TvShelfCh2:
    def __init__(self, x, y):
        self.image = tv_shelf_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

        # 入口 也就是上一層 離開調查時要回到的地方 None 代表離開調查
        self.enter = None

        self.focus = None
        self.focus_r = tv_shelf_investigation_r
        self.focus_l = tv_shelf_investigation_l
        self.object = None
        self.object_r = [ExitButton(500, 550), TvShelfRightDoorCh2(GAME_X, GAME_Y)]
        self.object_l = [ExitButton(500, 550), TvShelfLeftDoorCh2(GAME_X, GAME_Y)]


    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            # 代表右側櫃子被點到
            if x > 252:
                # 將物件與調查畫面設為右側
                self.focus = self.focus_r
                self.object = self.object_r
            else:
                # 將物件與調查畫面設為左側
                self.focus = self.focus_l
                self.object = self.object_l
            return 'investigation'
    def remove_knob(self):
        self.object = [item for item in self.object if not isinstance(item, KnobCh2)]

# 可互動物件本身 ===========================================
class TvCh2:
    def __init__(self, x, y ,lock):
        self.image = tv_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.tvshow = TvShowCh2(GAME_X, GAME_Y)
        self.mask = pygame.mask.from_surface(self.image)

        # 是否壞掉(第一章不可互動)
        self.lock = lock

        self.target_command = [pygame.K_UP, pygame.K_UP, pygame.K_DOWN, pygame.K_DOWN,
                               pygame.K_LEFT, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_RIGHT,
                               pygame.K_b, pygame.K_a]
        self.current_sequence = []
        # 玩家是否找到彩蛋
        self.easter_eggs = False

        # 入口 也就是上一層 離開調查時要回到的地方 None 代表離開調查
        self.enter = None

        # 下方要有儲存解謎進度的data
        # 點擊放大後的圖片
        self.focus = pygame.transform.scale(pygame.image.load(f"image/living_room/Tv/tv_investigation.png"), (GAME_WIDTH, GAME_HEIGHT))
        # 此圖片中可互動的物件
        self.object = [ExitButton(500,550),TvSwitchCh2(GAME_X, GAME_Y),TvPowerCh2(GAME_X, GAME_Y,self.lock),self.tvshow]

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            self.current_sequence = []
            return 'investigation'
    def input(self, input):
        self.current_sequence.append(input)
        if self.current_sequence[-len(self.target_command):] == self.target_command:
            self.cheat_code()
    def cheat_code(self):
        pass

class NewPaperCh2:
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
class LetterCh2:
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
        
# Desk ================================================================
class DeskCh2:
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

# globe =====================================================================
class GlobeCh2:
    def __init__(self, x, y):
        self.image = globe_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

        self.speaker = ["旁白","","旁白"]
        self.speaker_2 = ["旁白"]
        self.dialog = ["你轉動這個生鏽的地球儀..."," ","鏽化的輪軸發出刺耳的摩擦聲\n在你因刺耳的聲音想抵住耳朵時\n看見地球儀的轉軸上纏繞著一塊碎片"]
        self.dialog_2 = ["你不想在製造出那種恐怖的聲音"]
        # 是否互動過(獲得相片碎片
        self.lock = False
        self.give = None
        self.music = [(rust_sound,1)]

        self.show = Show(self.dialog, self.speaker, None, self.music, None)
        self.show_2 = Show(self.dialog_2, self.speaker_2, None, None, None)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x - self.rect.x, y - self.rect.y)) != 0:
            if not self.lock:
                # self.music.play()
                return 'dialog_sp'
            else:
                return 'dialog'
            
class GlobeTableCh2:
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

# chest ==================================================================================        
class ChestCh2:
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
        
class ChestKeyCh2:
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
        self.music = pick_up_items_sound

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            self.music.play()
            # 被撿起放入物品欄
            return 'take'