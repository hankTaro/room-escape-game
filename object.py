import os
import pygame
import cv2
import numpy as np
from user_request import *
from setting import *
from show import *


# TODO : 將所有物件的圖片匯入 並調整至合適大小

pygame.mixer.init()
pygame.mixer.music.set_volume(0.2)

# newspaper_image = pygame.transform.scale(pygame.image.load(f"image/Object/Newspaper/newspaper.png"), (int(466//3), int(260//3)))

clock_image = pygame.transform.scale(pygame.image.load(f"image/living_room/Clock/clock.png"), (GAME_WIDTH, GAME_HEIGHT))
clock_open_image = pygame.transform.scale(pygame.image.load(f"image/living_room/Clock/clock_open.png"), (GAME_WIDTH, GAME_HEIGHT))
hr_image = [pygame.transform.scale(pygame.image.load(f"image/living_room/Clock/hr/hr_{i}.png"), (int(1920//2), int(1080//2))) for i in range(0,12)]
mins_image = [pygame.transform.scale(pygame.image.load(f"image/living_room/Clock/mins/mins_{i}.png"), (int(1920//2), int(1080//2))) for i in range(0,60,5)]

right_image = pygame.transform.scale(pygame.image.load(f"image/Icon/right.png"), (int(30), int(30)))
left_image = pygame.transform.scale(pygame.image.load(f"image/Icon/left.png"), (int(30), int(30)))
menu_image = pygame.transform.scale(pygame.image.load(f"image/Icon/menu_w.png"), (int(42), int(30)))
exit_image = pygame.transform.scale(pygame.image.load(f"image/Icon/exit.png"), (int(30), int(30)))

living_room_window_image = pygame.transform.scale(pygame.image.load(f"image/living_room/window.png"), (GAME_WIDTH, GAME_HEIGHT))

door_image = pygame.transform.scale(pygame.image.load(f"image/Object/door.png"), (int(200), int(400)))
#yj
door_image_1  = pygame.transform.scale(pygame.image.load(f"image/living_room/Door/door_1.png"), (GAME_WIDTH, GAME_HEIGHT))
door_image_2  = pygame.transform.scale(pygame.image.load(f"image/living_room/Door/door_2.png"), (GAME_WIDTH, GAME_HEIGHT))
door_image_3  = pygame.transform.scale(pygame.image.load(f"image/living_room/Door/door_3.png"), (GAME_WIDTH, GAME_HEIGHT))
door_image_4  = pygame.transform.scale(pygame.image.load(f"image/living_room/Door/door_4.png"), (GAME_WIDTH, GAME_HEIGHT))
door_image_2_reverse  = pygame.transform.scale(pygame.image.load(f"image/study/door_2.png"), (GAME_WIDTH, GAME_HEIGHT))

desk_image = pygame.transform.scale(pygame.image.load(f"image/study/desk.png"), (GAME_WIDTH, GAME_HEIGHT))
book_image = pygame.transform.scale(pygame.image.load(f"image/study/book2.png"), (GAME_WIDTH, GAME_HEIGHT))
globe_image = pygame.transform.scale(pygame.image.load(f"image/study/Globe/globe.png"), (GAME_WIDTH, GAME_HEIGHT))
globe_table_image = pygame.transform.scale(pygame.image.load(f"image/study/Globe/globe_table.png"), (GAME_WIDTH, GAME_HEIGHT))
window_image = pygame.transform.scale(pygame.image.load(f"image/study/window.png"), (GAME_WIDTH, GAME_HEIGHT))
chest_image = pygame.transform.scale(pygame.image.load(f"image/living_room/TvShelf/chest.png"), (GAME_WIDTH, GAME_HEIGHT))
dropped_painting_image = pygame.transform.scale(pygame.image.load(f"image/study/dropped_painting.png"), (GAME_WIDTH, GAME_HEIGHT))
wife_1_image = pygame.transform.scale(pygame.image.load(f"image/Object/Wife/wife.png"), (GAME_WIDTH, GAME_HEIGHT))

# 繪畫相關 ============================================================
painting_i_image = pygame.transform.scale(pygame.image.load(f"image/study/painting.png"), (GAME_WIDTH, GAME_HEIGHT))

# 電視櫃相關 =================================================================================================
tv_shelf_image = pygame.transform.scale(pygame.image.load(f"image/living_room/TvShelf/tv_shelf.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_shelf_investigation_l = pygame.transform.scale(pygame.image.load(f"image/living_room/TvShelf/tv_shelf_investigation_l.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_shelf_investigation_r = pygame.transform.scale(pygame.image.load(f"image/living_room/TvShelf/tv_shelf_investigation_r.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_shelf_left_door_close_image = pygame.transform.scale(pygame.image.load(f"image/living_room/TvShelf/tv_shelf_door_close_l.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_shelf_right_door_close_image = pygame.transform.scale(pygame.image.load(f"image/living_room/TvShelf/tv_shelf_door_close_r.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_shelf_left_door_open_image = pygame.transform.scale(pygame.image.load(f"image/living_room/TvShelf/tv_shelf_door_open_l.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_shelf_right_door_open_image = pygame.transform.scale(pygame.image.load(f"image/living_room/TvShelf/tv_shelf_door_open_r.png"), (GAME_WIDTH, GAME_HEIGHT))

# TV 相關 ==================================================================================================================================
tv_image = pygame.transform.scale(pygame.image.load(f"image/living_room/Tv/tv.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_channel_1 = cv2.VideoCapture("image/living_room/Tv/TV_show/meme_1.mp4")
tv_channel_2 = cv2.VideoCapture("image/living_room/Tv/TV_show/tyler1 scream meme.mp4")
tv_channel_3 = pygame.transform.scale(pygame.image.load(f"image/living_room/Tv/TV_show/channel_1.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_channel_4 = cv2.VideoCapture("image/living_room/Tv/TV_show/Pornhub Video intro.mp4")
tv_channel_5 = cv2.VideoCapture("image/living_room/Tv/TV_show/KFC Chickendales Mother’s Day Performance.mp4")


tv_power_off_image = pygame.transform.scale(pygame.image.load(f"image/living_room/Tv/power_off.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_power_btn = pygame.transform.scale(pygame.image.load(f"image/living_room/Tv/power.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_switch_btn = pygame.transform.scale(pygame.image.load(f"image/living_room/Tv/switch.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_decipher_card_detail_image = pygame.transform.scale(pygame.image.load(f"image/living_room/Tv/tv_decipher_card.png"), (GAME_WIDTH, GAME_HEIGHT))

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

# 書架相關 ===================================================
book_shelf_image = pygame.transform.scale(pygame.image.load(f"image/living_room/book_shelf.png"), (GAME_WIDTH, GAME_HEIGHT))
book_shelf_puzzle = pygame.transform.scale(pygame.image.load(f"image/study/BookShelf/book_shelf_investigation_d.png"), (GAME_WIDTH, GAME_HEIGHT))
book_shelf_left_door_close_image = pygame.transform.scale(pygame.image.load(f"image/study/BookShelf/left_door_close.png"), (GAME_WIDTH, GAME_HEIGHT))
book_shelf_right_door_close_image = pygame.transform.scale(pygame.image.load(f"image/study/BookShelf/right_door_close.png"), (GAME_WIDTH, GAME_HEIGHT))
book_shelf_left_door_open_image = pygame.transform.scale(pygame.image.load(f"image/study/BookShelf/left_door_open.png"), (GAME_WIDTH, GAME_HEIGHT))
book_shelf_right_door_open_image = pygame.transform.scale(pygame.image.load(f"image/study/BookShelf/right_door_open.png"), (GAME_WIDTH, GAME_HEIGHT))

locker_image = pygame.transform.scale(pygame.image.load(f"image/study/Locker/locker.png"), (GAME_WIDTH, GAME_HEIGHT))
locker_setup_image = pygame.transform.scale(pygame.image.load(f"image/study/Locker/locker_setup.png"), (GAME_WIDTH, GAME_HEIGHT))
locker_open_image = pygame.transform.scale(pygame.image.load(f"image/study/Locker/locker_open.png"), (GAME_WIDTH, GAME_HEIGHT))

chest_key_image = pygame.transform.scale(pygame.image.load(f"image/study/BookShelf/chest_key.png"), (GAME_WIDTH, GAME_HEIGHT))

knob_0_image = [pygame.transform.scale(pygame.image.load(f"image/study/knob/knob_000{i}.png"), (GAME_WIDTH, GAME_HEIGHT)) for i in range(10)]
knob_1_image = [pygame.transform.scale(pygame.image.load(f"image/study/knob/knob_1_000{i}.png"), (GAME_WIDTH, GAME_HEIGHT)) for i in range(10)]
knob_2_image = [pygame.transform.scale(pygame.image.load(f"image/study/knob/knob_2_000{i}.png"), (GAME_WIDTH, GAME_HEIGHT)) for i in range(10)]
knob_3_image = [pygame.transform.scale(pygame.image.load(f"image/study/knob/knob_3_000{i}.png"), (GAME_WIDTH, GAME_HEIGHT)) for i in range(10)]
# 相框相關 ===========================================================
photo_frame_image = pygame.transform.scale(pygame.image.load(f"image/study/PhotoFrame/photo_frame.png"), (GAME_WIDTH, GAME_HEIGHT))
photo_fragments_image = [pygame.transform.scale(pygame.image.load(f"image/study/PhotoFrame/photo_{i}.png"), (GAME_WIDTH, GAME_HEIGHT)) for i in range(4)]
photo_fragments_take_image = [pygame.transform.scale(pygame.image.load(f"image/study/PhotoFrame/photo_take_{i}.png"), (GAME_WIDTH, GAME_HEIGHT)) for i in range(4)]
photo_frame_puzzle = pygame.transform.scale(pygame.image.load(f"image/study/PhotoFrame/photo_frame_puzzle.png"), (GAME_WIDTH, GAME_HEIGHT))

# 可拾取物件 ===========================================================
handle_image = pygame.transform.scale(pygame.image.load(f"image/living_room/Clock/Handle.png"), (GAME_WIDTH, GAME_HEIGHT))
password_hint_1_image = pygame.transform.scale(pygame.image.load(f"image/living_room/Clock/Password_Hint_1.png"), (GAME_WIDTH, GAME_HEIGHT))

# icon==================================================================
password_hint_1_icon = pygame.transform.scale(pygame.image.load(f"image/Icon/password_hint_1_icon.png"), (ICON_SIZE, ICON_SIZE))
handle_icon = pygame.transform.scale(pygame.image.load(f"image/Icon/handle_icon.png"), (ICON_SIZE, ICON_SIZE))
chest_key_icon = pygame.transform.scale(pygame.image.load(f"image/Icon/chest_key_icon.png"), (ICON_SIZE, ICON_SIZE))
tv_decipher_card_detail_icon = pygame.transform.scale(pygame.image.load(f"image/Icon/tv_decipher_card_detail_icon.png"), (ICON_SIZE, ICON_SIZE))
photo_fragments_icon = [pygame.transform.scale(pygame.image.load(f"image/Icon/photo_{i}_icon.png"), (ICON_SIZE, ICON_SIZE)) for i in range(4)]
cheat_code_icon = pygame.transform.scale(pygame.image.load(f"image/Icon/cheat_code_icon.png"), (ICON_SIZE, ICON_SIZE))
# 調查畫面===============================================================
password_hint_1_observe = pygame.image.load(f"image/Observe/password_hint_1_observe.png")
handle_observe = pygame.image.load(f"image/Observe/handle_observe.png")
chest_key_observe = pygame.image.load(f"image/Observe/chest_key_observe.png")
photo_fragments_observe = [pygame.image.load(f"image/Icon/photo_{i}_icon.png") for i in range(4)]
cheat_code_observe = pygame.image.load(f"image/Observe/cheat_code_observe.png")

# 彩蛋相關 ===========================================================
cheat_code_image = pygame.transform.scale(pygame.image.load(f"image/living_room/Tv/cheat_code.png"), (GAME_WIDTH, GAME_HEIGHT))
# XX相關 ===========================================================


# 待繪製物件
none_image = pygame.transform.scale(BACKGROUND_IMAGE, (100, 100))
none_icon = pygame.transform.scale(pygame.image.load(f"image/icon.png"), (ICON_SIZE, ICON_SIZE))
observe_image = pygame.transform.scale(pygame.image.load(f"image/living_room/Tv/cheat_code.png"), (GAME_WIDTH, GAME_HEIGHT))

# 開場畫面
opening_1_image = pygame.transform.scale(pygame.image.load(f"image/開場.png"), (WIN_WIDTH, WIN_HEIGHT))
opening_2_image = pygame.transform.scale(pygame.image.load(f"image/開場_2.png"), (WIN_WIDTH, WIN_HEIGHT))

# 開場畫面
class OpenMenu:
    def __init__(self, x, y):
        self.image = opening_1_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.music = door_open_sound
        self.lock = False

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.lock == False:
            self.lock = True
            self.music.play()
            self.image = opening_2_image
            return 'start'

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
# 包包換頁按鈕
class BagPageButton:
    def __init__(self):
        self.right_image = right_image
        self.left_image = left_image
        self.x_r = GAME_X + GAME_WIDTH + 70
        self.y_r = GAME_Y + GAME_HEIGHT + 25
        self.x_l = GAME_X + GAME_WIDTH + 20
        self.y_l = GAME_Y + GAME_HEIGHT + 25
        self.rect_r = self.right_image.get_rect()
        self.rect_r.topleft = (self.x_r, self.y_r)
        self.rect_l = self.left_image.get_rect()
        self.rect_l.topleft = (self.x_l, self.y_l)
        self.mask_r = pygame.mask.from_surface(self.right_image)
        self.mask_l = pygame.mask.from_surface(self.left_image)

    def clicked(self, x: int, y: int):
        if self.rect_r.collidepoint(x, y) and self.mask_r.get_at((x -  self.rect_r.x, y -  self.rect_r.y)) != 0:
            return 'right'
        if self.rect_l.collidepoint(x, y) and self.mask_l.get_at((x -  self.rect_l.x, y -  self.rect_l.y)) != 0:
            return 'left'
class RightButton:
    def __init__(self, x, y):
        self.image = right_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.music = walking_sound

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y):
            self.music.play()
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
        self.music = walking_sound

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y):
            self.music.play()
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
        self.music = door_open_sound

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            self.music.play()
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

        self.speaker = ["旁白"]
        self.dialog = ["離開房屋的門\n手把上充滿著鏽蝕與歲月痕跡\n" 
                      "在你進屋開門時，他發出了吵雜的摩擦噪音"] #\n千里迢迢來到這裡可不只是為了進來撇一眼的\n你使勁全力依然打不開他
        self.music = None#[(door_open_sound,0)]

        self.show = Show(self.dialog, self.speaker, None, self.music, None)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'dialog'
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
        self.music = door_open_sound

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            self.music.play()
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

        self.speaker = ["旁白","","旁白"]
        self.speaker_2 = ["旁白"]
        self.dialog = ["這條通往廚房的通道已經被碎石瓦礫掩埋了\n你靠近嘗試挖掘...","..." ,
                      "挖掘的好一陣子，碎石瓦礫依舊阻擋著通道\n但是你在瓦礫堆中找到了一張...膠片?"]
        self.dialog_2 = ["你看著自己紅腫刺痛的手，想想還是別再挖了好了"]
        # 是否互動過(獲得膠片
        self.lock = False
        self.give = DecipherCard(GAME_X, GAME_Y)
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


# 畫作相關
class DecipherCardPuzzle:
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
class Painting:
    def __init__(self, x, y):
        self.image = painting_i_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        # 入口 也就是上一層 離開調查時要回到的地方 None 代表離開調查
        self.enter = None
        self.focus = pygame.transform.scale(pygame.image.load(f"image/study/painting_1_investigation.png"),
                                            (GAME_WIDTH, GAME_HEIGHT))
        # TODO : 此圖片中可互動的物件
        self.object = [ExitButton(500, 550)]


    def clicked(self, x: int, y: int):
        # TODO : 連接到 user_request 若是可互動物件被點到 轉換場景 若是不可互動則說話或是
        if self.rect.collidepoint(x, y) and self.mask.get_at((x - self.rect.x, y - self.rect.y)) != 0:
            return 'investigation'

# 電視櫃相關 ===============================================================
class TvShelfRightDoor:
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

class TvShelfLeftDoor:
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



class TvShelf:
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
        self.object_r = [ExitButton(500, 550),PhotoFragmentsTake(GAME_X, GAME_Y, 1), TvShelfRightDoor(GAME_X, GAME_Y)]
        self.object_l = [ExitButton(500, 550),PhotoFragmentsTake(GAME_X, GAME_Y, 3), TvShelfLeftDoor(GAME_X, GAME_Y)]


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
        self.object = [item for item in self.object if not isinstance(item, Knob)]
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
        self.music = tv_change_channel_sound

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'switch'

class TvPower:
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

class TvShow:
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




# 可互動物件本身 ===========================================
class Tv:
    def __init__(self, x, y ,lock):
        self.image = tv_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.tvshow = TvShow(GAME_X, GAME_Y)
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
        self.object = [ExitButton(500,550),TvSwitch(GAME_X, GAME_Y),TvPower(GAME_X, GAME_Y,self.lock),self.tvshow]


    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            self.current_sequence = []
            return 'investigation'
    def input(self, input):
        self.current_sequence.append(input)
        if self.current_sequence[-len(self.target_command):] == self.target_command:
            self.cheat_code()
    def cheat_code(self):
        cheat_code_sound.play()
        self.object.append(CheatCode(GAME_X, GAME_Y))




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
        self.music = clock_hand_sound

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            self.music.play()
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
        self.music = clock_hand_sound

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            self.music.play()
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
        self.music = clock_sound
    
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
        self.music.play()



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

class LeftDoor:
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
        self.music = knob_twist_sound
    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            self.music.play()
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
        self.object = [ExitButton(500, 550), PhotoFrame(GAME_X, GAME_Y), ChestKey(GAME_X, GAME_Y), PhotoFragmentsTake(GAME_X, GAME_Y, 0),
                       Knob(GAME_X, GAME_Y, 0), Knob(GAME_X, GAME_Y, 1), Knob(GAME_X, GAME_Y, 2), Knob(GAME_X, GAME_Y, 3),
                       Locker(GAME_X, GAME_Y), RightDoor(GAME_X, GAME_Y), LeftDoor(GAME_X, GAME_Y)]
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
        self.lock = False

        # 因為碎片也是用畫面大小輸出 只是涂色位置不同 所以所有碎片對準 GAME_X, GAME_Y 就會是正確位置

    def clicked(self, x: int, y: int):
        # 除了被點到 還要確定滑鼠是按住的才能拖動 還要是未完成(lock == F)
        if self.rect.collidepoint(x, y) and self.mask.get_at((x - self.rect.x, y - self.rect.y)) != 0 and self.lock == False:
            return 'drag'
    def drag_set(self):
        self.drag = True
        # self.rect.move_ip(event.rel)
    def release(self):
        if not self.lock:
            correct_position = (GAME_X, GAME_Y)
            # 畫面重疊區域大小必需高於此
            min_intersection_width = self.rect.width * 0.95
            min_intersection_height = self.rect.height * 0.95
            self.drag = False
            if self.rect.colliderect(pygame.Rect(correct_position, self.rect.size)):
                intersection = self.rect.clip(pygame.Rect(correct_position, self.rect.size))
                if intersection.width >= min_intersection_width and intersection.height >= min_intersection_height:
                    # 鎖住 並切將其對其好
                    self.lock = True
                    self.rect.topleft = (GAME_X,GAME_Y)
                    return 'lock'

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
        self.focus = photo_frame_puzzle
        # 這裡的起始位置要手動調整，使得碎片一開始疊在向框的外面
        self.object = [ExitButton(500, 550)]
        self.fragments = [PhotoFragments(GAME_X + 400, GAME_Y + 150, 0),PhotoFragments(GAME_X + 450, GAME_Y + 150, 1),
                       PhotoFragments(GAME_X + 300, GAME_Y + 40, 2),PhotoFragments(GAME_X + 300, GAME_Y - 20, 3)]
        # 拚好的碎片數
        self.fix_num = 0
        self.music = paper_sound
    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'investigation'
    def add_fragments(self,fragment):
        self.object.append(self.fragments[fragment.num])
    def fix(self):
        self.music.play()
        self.fix_num += 1
        if self.fix_num == 4:
            return 'done'
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

        self.speaker = ["旁白","","旁白"]
        self.speaker_2 = ["旁白"]
        self.dialog = ["你轉動這個生鏽的地球儀..."," ","鏽化的輪軸發出刺耳的摩擦聲\n在你因刺耳的聲音想抵住耳朵時\n看見地球儀的轉軸上纏繞著一塊碎片"]
        self.dialog_2 = ["你不想在製造出那種恐怖的聲音"]
        # 是否互動過(獲得相片碎片
        self.lock = False
        self.give = PhotoFragmentsTake(GAME_X, GAME_Y, 2)
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
class LivingRoomWindow:
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
# class Wife_Ch1:
#     def __init__(self, x, y):
#         self.image = wife_1_image
#         self.x = x
#         self.y = y
#         self.rect = self.image.get_rect()
#         self.rect.topleft = (x, y)
#         self.mask = pygame.mask.from_surface(self.image)
#         # 對話內容
#         self.text = ["要是能回到過去該有多好⋯","你找到遺產了嗎?"]
#         self.text_index = 0
#         self.text_size = 2
#
#
#     def clicked(self, x: int, y: int):
#         # TODO : 連接到 user_request 若是可互動物件被點到 轉換場景 若是不可互動則說話或是
#         if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
#             return 'speak'


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
        self.music = pick_up_items_sound
    # TODO : 一些交互用函式
    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            self.music.play()
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
        self.music = pick_up_items_sound
    # TODO : 一些交互用函式

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            self.music.play()
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
        self.music = pick_up_items_sound

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            self.music.play()
            # 被撿起放入物品欄
            return 'take'


class DecipherCard:
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
        # 物件使用後發出的聲音
        self.music = card_collide_sound


    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            # 被撿起放入物品欄
            return 'take'

class PhotoFragmentsTake:
    def __init__(self, x, y, num):
        self.name = "相片碎片"
        self.icon = photo_fragments_icon[num]
        # 調查中此物品的樣貌
        self.observe = photo_fragments_observe[num]
        # 調查中此物品的敘述
        self.description = "一張因時間而泛黃的相片碎片\n" \
                           "裡頭似乎描繪著某個你無比熟悉的事物\n" \
                           "相片的背面有一些數字與符號\n" \
                           "但是太片段了，無法理解其含義..."

        self.num = num
        self.image = photo_fragments_take_image[num]
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.music = pick_up_items_sound
        # 物件使用後發出的聲音
        self.music = paper_sound

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x - self.rect.x, y - self.rect.y)) != 0:
            self.music.play()
            # 被撿起放入物品欄
            return 'take'

# 彩蛋物件類 =====================================
class CheatCode:
    def __init__(self, x, y):
        self.name = "魂斗羅卡帶"
        self.icon = cheat_code_icon
        # 調查中此物品的樣貌
        self.observe = cheat_code_observe
        # 調查中此物品的敘述
        self.description = "經典FC遊戲魂斗羅的卡帶\n" \
                           "輸入這串作弊碼即可獲得30條命\n" \
                           "讓你快快樂樂的闖蕩關卡\n" \
                           "不必擔心任何生命問題"

        self.image = cheat_code_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.music = pick_up_items_sound

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x - self.rect.x, y - self.rect.y)) != 0:
            self.music.play()
            # 被撿起放入物品欄
            return 'take'