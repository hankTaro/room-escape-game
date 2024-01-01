import os
import pygame
import cv2
import numpy as np
from user_request import *
from setting import *
from show import *
from object import ExitButton


pygame.mixer.init()
pygame.mixer.music.set_volume(0.2)

# 圖片
black_image = pygame.transform.scale(pygame.image.load(os.path.join("image", "black.png")), (GAME_WIDTH,GAME_HEIGHT))

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
homework_image = [pygame.transform.scale(pygame.image.load(f"image/Ch2/Desk/homework_{i}.png"), (GAME_WIDTH, GAME_HEIGHT)) for i in range(2)]
# 日曆 ======================================================================================================
calendar_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/calendar/calendar.png"), (GAME_WIDTH, GAME_HEIGHT))
# 垃圾桶 ======================================================================================================
trashcan_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/Trashcan/trashcan.png"), (GAME_WIDTH, GAME_HEIGHT))
# 電視櫃相關 =================================================================================================
tv_shelf_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/TvShelf/tv_shelf.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_shelf_investigation_l = pygame.transform.scale(pygame.image.load(f"image/Ch2/TvShelf/tv_shelf_investigation_l.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_shelf_investigation_r = pygame.transform.scale(pygame.image.load(f"image/Ch2/TvShelf/tv_shelf_investigation_r.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_shelf_left_door_close_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/TvShelf/tv_shelf_door_close_l.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_shelf_right_door_close_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/TvShelf/tv_shelf_door_close_r.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_shelf_left_door_open_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/TvShelf/tv_shelf_door_open_l.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_shelf_right_door_open_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/TvShelf/tv_shelf_door_open_r.png"), (GAME_WIDTH, GAME_HEIGHT))
# 削鉛筆機 ==================================================================================================
pencil_sharper_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/TvShelf/Pencil sharpener.png"), (GAME_WIDTH, GAME_HEIGHT))
# 電視相關 ==================================================================================================
tv_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/Tv/tv.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_power_off_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/Tv/power_off.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_power_btn = pygame.transform.scale(pygame.image.load(f"image/Ch2/Tv/power.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_switch_btn = pygame.transform.scale(pygame.image.load(f"image/Ch2/Tv/switch.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_decipher_card_detail_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/Tv/tv_decipher_card.png"), (GAME_WIDTH, GAME_HEIGHT))
tv_channel_1 = cv2.VideoCapture("image/Ch2/Tv/TV_show/Sequence.mp4")
tv_channel_2 = cv2.VideoCapture("image/Ch2/Tv/TV_show/tyler1 scream meme.mp4")
tv_channel_3 = cv2.VideoCapture("image/Ch2/Tv/TV_show/Pornhub Video intro.mp4")
tv_channel_4 = cv2.VideoCapture("image/Ch2/Tv/TV_show/KFC Chickendales Mother’s Day Performance.mp4")
tv_channel_5 = cv2.VideoCapture("image/Ch2/Tv/TV_show/EVA.mp4")
# 寶箱 =====================================================================================================
chest_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/TvShelf/chest.png"), (GAME_WIDTH, GAME_HEIGHT))
# 地球儀 ===================================================================================================
globe_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/Globe/globe.png"), (GAME_WIDTH, GAME_HEIGHT))
globe_table_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/Globe/globe_table.png"), (GAME_WIDTH, GAME_HEIGHT))
# 繪畫
painting_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/Painting/painting.png"), (GAME_WIDTH, GAME_HEIGHT))
# 書架相關 =================================================================================================
book_shelf_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/BookShelf/book_shelf.png"), (GAME_WIDTH, GAME_HEIGHT))
book_shelf_puzzle = pygame.transform.scale(pygame.image.load(f"image/Ch2/BookShelf/book_shelf_investigation.png"), (GAME_WIDTH, GAME_HEIGHT))
book_shelf_left_door_close_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/BookShelf/left_door_close.png"), (GAME_WIDTH, GAME_HEIGHT))
book_shelf_right_door_close_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/BookShelf/right_door_close.png"), (GAME_WIDTH, GAME_HEIGHT))
book_shelf_left_door_open_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/BookShelf/left_door_open.png"), (GAME_WIDTH, GAME_HEIGHT))
book_shelf_right_door_open_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/BookShelf/right_door_open.png"), (GAME_WIDTH, GAME_HEIGHT))
# 書
book_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/BookShelf/books.png"), (GAME_WIDTH, GAME_HEIGHT))

# 書櫃鑰匙 ================================================================================================
chest_key_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/BookShelf/chest_key.png"), (GAME_WIDTH, GAME_HEIGHT))
# 紙箱 ===================================================================================================
box_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/Box/boxs.png"), (GAME_WIDTH, GAME_HEIGHT))
# 報紙
newspaper_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/Newspaper/newspaper.png"), (GAME_WIDTH, GAME_HEIGHT))
# 可拾取物件 ==============================================================================================
top_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/TvShelf/陀螺.png"), (GAME_WIDTH, GAME_HEIGHT))
beer_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/Beer/beer.png"), (GAME_WIDTH, GAME_HEIGHT))
# icon ===================================================================================================
chest_key_icon = pygame.transform.scale(pygame.image.load(f"image/Icon/chest_key_icon.png"), (ICON_SIZE, ICON_SIZE))
shit_icon = pygame.transform.scale(pygame.image.load(f"image/Icon/shit.png"), (ICON_SIZE, ICON_SIZE))
pencil_icon = [pygame.transform.scale(pygame.image.load(f"image/Icon/penceil_{i}.png"), (ICON_SIZE, ICON_SIZE)) for i in range(3)]
bamboo_hat_icon = pygame.transform.scale(pygame.image.load(f"image/Icon/shit.png"), (ICON_SIZE, ICON_SIZE))
top_icon = pygame.transform.scale(pygame.image.load(f"image/Icon/top_icon.png"), (ICON_SIZE, ICON_SIZE))
beer_icon = pygame.transform.scale(pygame.image.load(f"image/Icon/beer_icon.png"), (ICON_SIZE, ICON_SIZE))
kmt_icon = pygame.transform.scale(pygame.image.load(f"image/Icon/kmt_icon.png"), (ICON_SIZE, ICON_SIZE))
# 調查畫面===============================================================
chest_key_observe = pygame.image.load(f"image/Observe/chest_key_observe.png")
shit_observe = pygame.image.load(f"image/Observe/shit.png")
pencil_observe = [pygame.image.load(f"image/Icon/penceil_{i}.png") for i in range(3)]
bamboo_hat_observe = pygame.image.load(f"image/Observe/shit.png")
top_observe = pygame.image.load(f"image/Icon/top_icon.png")
beer_observe = pygame.image.load(f"image/Icon/beer_icon.png")
kmt_observe = pygame.image.load(f"image/Icon/kmt_icon.png")
# 聲音
mute = None
tv_show_1_sound = pygame.mixer.Sound('music/Sequence.mp3')
tv_show_1_sound.set_volume(0.6)
tv_show_2_sound = pygame.mixer.Sound('music/tyler1 scream meme.wav')
tv_show_3_sound = pygame.mixer.Sound('music/Pornhub Video intro.wav')
tv_show_4_sound = pygame.mixer.Sound('music/KFC Chickendales Mother’s Day Performance.wav')
tv_show_5_sound = pygame.mixer.Sound('music/EVA.mp3')
clock_sound = pygame.mixer.Sound('music/clock.wav')
clock_hand_sound = pygame.mixer.Sound('music/clock_hand.wav')
walking_sound = pygame.mixer.Sound('music/walking.wav')
door_open_sound = pygame.mixer.Sound('music/door_open.wav')
tv_change_channel_sound = pygame.mixer.Sound('music/tv_change_channel.wav')
tv_power_sound = pygame.mixer.Sound('music/clicked.wav')
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
pencil_writing_sound = pygame.mixer.Sound('music/鉛筆寫字聲.mp3')
sharping_sound = pygame.mixer.Sound('music/削鉛筆聲_削鉛筆機.mp3')
item_found_rarest_sound = pygame.mixer.Sound('music/MH - Item Found (rarest).mp3')
Knock_door_sound = pygame.mixer.Sound('music/敲門聲.mp3')


# 門 ===========================================================================
class DoorToExitCh2:
    def __init__(self, x, y):
        self.image = door_image_1
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        # 要等作完作業和看完電視才能離開
        self.can_exit = False

        self.speaker = ["小男孩"]
        self.dialog = ["媽媽還沒回家，先待在阿公家吧"] #\n千里迢迢來到這裡可不只是為了進來撇一眼的\n你使勁全力依然打不開他
        self.music = door_open_sound

        self.show = Show(self.dialog, self.speaker, None, None, None)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            if self.can_exit:
                return 'done'
            else:
                return 'dialog'
    def unlock(self):
        self.can_exit = True



class DoorToBedRoomCh2:
    def __init__(self, x, y):
        self.image = door_image_3
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.lock = False
        self.speaker = ["旁白","","小男孩","爺爺","小男孩"]
        self.dialog = ["你站在門前，你聽到裏頭傳來在削東西的聲音"," ","阿公，削鉛筆機在哪裡?","削鉛筆機喔...，我好像放在...\n你去電視櫃那邊找找看吧",
                       "奇怪，阿公在房間裡幹嘛阿，平常這時候他不都會在客廳看電視嗎?\n算了 趕快去把筆削一削吧"]

        self.speaker_1 = ["", "小男孩", "爺爺"]
        self.dialog_1 = [" ", "阿公，我削好鉛筆了", "很好啊，那趕快去寫作業吧，等等阿公就出來陪你玩"]

        self.speaker_2 = ["", "小男孩", "爺爺"]
        self.dialog_2 = [" ", "阿公，我削好鉛筆了", "很好啊，那趕快去寫作業吧\n不過你剛剛真的是在削鉛筆嗎?\n"
                        "為什麼我剛剛好像聽到氣刃兜割的聲音?"]

        self.speaker_3 = ["", "小男孩", "爺爺"]
        self.dialog_3 = [" ", "阿公，我功課寫完了，我要去看電視了喔", "真乖，去看吧，抱歉阿公還在忙，不能陪你玩..."]

        self.speaker_4 = ["", "小男孩", "旁白"]
        self.dialog_4 = [" ", "阿公，我要回家了喔", "...\n沒有回應，應該是睡著了"]

        self.music = [(Knock_door_sound,1)]
        self.music_1 = [(Knock_door_sound,0)]

        self.show = Show(self.dialog, self.speaker, None, self.music, None)
        self.show_1 = Show(self.dialog_1, self.speaker_1, None, self.music_1, None)
        self.show_2 = Show(self.dialog_2, self.speaker_2, None, self.music_1, None)
        self.show_3 = Show(self.dialog_3, self.speaker_3, None, self.music_1, None)
        self.show_4 = Show(self.dialog_4, self.speaker_4, None, self.music_1, None)


    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'dialog'
        else:
            return 0
    def pencil_sharp(self,level):
        if level == 10:
            self.show = self.show_2
        else:
            self.show = self.show_1
    def finsh_homework(self):
        self.show = self.show_3
    def finsh_tv(self):
        self.show = self.show_4

class DoorToKitchenCh2:
    def __init__(self, x, y):
        self.image = door_image_4
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

        self.speaker = ["小男孩"]
        # self.speaker_2 = ["旁白"]
        self.dialog = ["後面是廚房和爺爺的倉庫\n倉庫裏頭都是爺爺的木工作品，我平常都會在旁邊看爺爺工作"]
        # self.dialog_2 = ["你看著自己紅腫刺痛的手，想想還是別再挖了好了"]
        # 已獲得膠片
        self.lock = False
        self.give = None
        self.music = None # [(rock_sound,1)]

        self.show = Show(self.dialog, self.speaker, None, self.music, None)
        # self.show_2 = Show(self.dialog_2, self.speaker_2, None, None, None)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'dialog'
        #     if not self.lock:
        #         self.lock = True
        #         return 'dialog_sp'
        #     else:
        #         return 'dialog'
        # else:
        #     return 0

# 窗戶 ==================================================================================================
class LivingRoomWindowCh2:
    def __init__(self, x, y):
        self.image = living_room_window_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

        self.music = None#[(glass_sound,0)]

        self.speaker = ["旁白","小男孩"]
        self.dialog = ["往外探出去，外頭黑鴉鴉的\n除了幾戶人家的燈火，其餘的東西都看不清楚","隔壁的大哥哥，總是一天到晚的在說什麼，未來要蓋一個愛情摩天輪\n神經病..."]
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

        self.speaker = ["小男孩"]
        self.dialog = ["阿公自己做的時鐘，不知道為什麼今天他一直停在12點"]
        self.music = [(clock_sound,0)]

        self.show = Show(self.dialog, self.speaker, None, self.music, None)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x - self.rect.x, y - self.rect.y)) != 0:
            return 'dialog'
        else:
            return 0


class PaintingCh2:
    def __init__(self, x, y):
        self.image = painting_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

        self.speaker = ["小男孩"]
        self.dialog = ["阿公前陣子換上去的新畫，好醜喔..."]
        self.music = None#[(clock_sound, 0)]

        self.show = Show(self.dialog, self.speaker, None, self.music, None)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x - self.rect.x, y - self.rect.y)) != 0:
            return 'dialog'
        else:
            return 0

class TrashCanCh2:
    def __init__(self, x, y):
        self.image = trashcan_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

        self.counter = 0
        self.give = AbandonedProject(GAME_X, GAME_Y)
        self.lock = False

        self.speaker = ["旁白"]
        self.speaker_2 = ["旁白"]
        self.dialog = ["你翻找著垃圾桶...\n除了垃圾你甚麼都沒找到..."]
        self.dialog_2 = ["裡頭真的只剩垃圾了..."]
        self.dialog_3 = ["你翻找著垃圾桶...\n等等...\n你看見一個比較特別的東西，你將她撿了起來"]
        self.music = None#[(clock_sound, 0)]

        self.show = Show(self.dialog, self.speaker, None, self.music, None)
        self.show_2 = Show(self.dialog_2, self.speaker_2, None, self.music, None)
        self.show_3 = Show(self.dialog_3, self.speaker_2, None, self.music, None)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x - self.rect.x, y - self.rect.y)) != 0:
            if self.lock:
                return 'dialog'
            if self.counter < 2:
                self.counter += 1
                return 'dialog'
            elif self.counter == 2:
                self.show = self.show_3
                self.lock = True
                return 'dialog_sp'

        else:
            return 0

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

        self.speaker = ["小男孩"]
        self.dialog = ["鎖住了...打不開"]
        self.music = [(door_locked_sound,0)]

        self.show = Show(self.dialog, self.speaker, None, self.music, None)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x - self.rect.x, y - self.rect.y)) != 0:
            return 'dialog'
        else:
            return 0



# 書  ===================================================================================================
class Books:
    def __init__(self, x, y):
        self.image = book_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

        self.speaker = ["旁白"]
        self.dialog = ["上頭擺滿木工相關的書籍，許多書籍都被翻到十分破舊了"]
        self.music = None

        self.show = Show(self.dialog, self.speaker, None, self.music, None)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x - self.rect.x, y - self.rect.y)) != 0:
            return 'dialog'
        else:
            return 0

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
        self.object = [ExitButton(500, 550),
                       RightDoorCh2(GAME_X, GAME_Y), LeftDoorCh2(GAME_X, GAME_Y)]
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
        self.is_power = False
        self.index = 0

        self.speaker = ["小男孩"]
        self.dialog = ["好耶，剛好趕上新世紀福音戰士\n我也好想駕駛初號機喔..."]

        self.show = Show(self.dialog, self.speaker, None, None, None)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            if self.is_power:
                self.music.play()
                self.index += 1
            # 當轉到要看的台時 回傳訊號觸發劇情 先假設要看的台是5號(index==4)
            if self.index == 4:
                return 'watch'
            else:
                return 'switch'
    def power(self):
        self.is_power = not self.is_power

class TvPowerCh2:
    def __init__(self, x, y,lock):
        self.image = tv_power_btn
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.music = [(tv_power_sound,0)]

        self.speaker = ["小男孩"]
        self.dialog = ["爺爺說作業寫完後才可以看電視"]
        # 是否壞掉(第一章不可互動)
        self.lock = lock
        self.music_dialog = tv_power_sound

        self.show = Show(self.dialog, self.speaker, None, None, None)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            if self.lock:
                return 'dialog'
            else:
                self.music_dialog.play()
                return 'shutdown'

class TvShowCh2:
    def __init__(self, x, y):
        self.all_show = [tv_channel_1,tv_channel_2,tv_channel_3,tv_channel_4,tv_channel_5]
        self.all_music = [tv_show_1_sound,tv_show_2_sound,tv_show_3_sound,tv_show_4_sound,tv_show_5_sound]
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
            self.image.set(cv2.CAP_PROP_POS_FRAMES, 0) # 關電視後將影片重製
            if self.music:
                self.music.stop()

# 可互動物件本身 ===========================================
class TvCh2:
    def __init__(self, x, y):
        self.image = tv_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.tvshow = TvShowCh2(GAME_X, GAME_Y)
        self.mask = pygame.mask.from_surface(self.image)

        # 是否鎖起來不給用(寫完作業前不可互動)
        self.lock = True
        # 看完電視就鎖起來不可再互動
        self.lock_2 = False

        self.target_command = [pygame.K_UP, pygame.K_UP, pygame.K_DOWN, pygame.K_DOWN,
                               pygame.K_LEFT, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_RIGHT,
                               pygame.K_b, pygame.K_a]
        self.current_sequence = []
        # 玩家是否找到彩蛋
        self.easter_eggs = False

        # 入口 也就是上一層 離開調查時要回到的地方 None 代表離開調查
        self.enter = None

        self.power_button = TvPowerCh2(GAME_X, GAME_Y, self.lock)
        self.switch_button = TvSwitchCh2(GAME_X, GAME_Y)

        # 下方要有儲存解謎進度的data
        # 點擊放大後的圖片
        self.focus = pygame.transform.scale(pygame.image.load(f"image/living_room/Tv/tv_investigation.png"), (GAME_WIDTH, GAME_HEIGHT))
        # 此圖片中可互動的物件
        self.object = [ExitButton(500,550),self.switch_button,self.power_button,self.tvshow]

        self.speaker = ["小男孩"]
        self.dialog = ["阿，看完了\n9點了...媽媽應該已經回來了，該回家了..."]
        self.music = None  # [(clock_sound, 0)]

        self.show = Show(self.dialog, self.speaker, None, self.music, None)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            if self.lock_2:
                return 'dialog'
            else:
                self.current_sequence = []
                return 'investigation'
    def input(self, input):
        self.current_sequence.append(input)
        if self.current_sequence[-len(self.target_command):] == self.target_command:
            self.cheat_code()
    def power_switch(self):
        self.tvshow.power()
        self.switch_button.power()
    def cheat_code(self):
        pass
    def unlock(self):
        self.power_button.lock = False
    def lock_on(self):
        self.lock_2 = True

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
        self.object_l = [ExitButton(500, 550), PencilSharpener(GAME_X, GAME_Y),Top(GAME_X, GAME_Y),TvShelfLeftDoorCh2(GAME_X, GAME_Y)]


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

class PencilSharpener:
    def __init__(self, x, y):
        self.image = pencil_sharper_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

        self.speaker = ["旁白","小男孩"]
        self.speaker_1 = ["旁白"]
        self.dialog = ["你把鉛筆削尖了","這樣就行了，快回去把作業寫完吧"]
        self.dialog_1 = ["鉛筆被你越削越尖..."]
        self.dialog_2 = ["鉛筆已經削到尖到不能再尖了\n他現在的銳利度彷彿能屠龍"]
        self.music = None  # [(clock_sound, 0)]
        self.level = 0

        self.show = Show(self.dialog, self.speaker, None, self.music, None)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x - self.rect.x, y - self.rect.y)) != 0:
            return 'sharp'
        else:
            return 0
    def sharp(self):
        self.level += 1
        if self.level == 1:
            self.show = Show(self.dialog_1, self.speaker_1, None, self.music, None)
        elif self.level == 10:
            self.show = Show(self.dialog_2, self.speaker, None, self.music, None)






        
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

        self.homework = Homework(GAME_X,GAME_Y)


        self.focus = pygame.transform.scale(pygame.image.load(f"image/Ch2/Desk/desk_investigation.png"), (GAME_WIDTH, GAME_HEIGHT))

        self.object = [ExitButton(500,550),self.homework]

    def clicked(self, x: int, y: int):
        # TODO : 連接到 user_request 若是可互動物件被點到 轉換場景 若是不可互動則說話或是
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'investigation'

class Homework:
    def __init__(self, x, y):
        self.image = homework_image[0]
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

        self.speaker_undone = ["小男孩"]
        self.dialog_undone = ["鉛筆斷掉了沒辦法寫，要先去找削鉛筆機才行\n問問阿公鉛筆機在哪好了，阿公應該在臥室裡面"]

        self.speaker_doing = ["","小男孩"]
        self.dialog_doing = [" ","總算寫完了，來去看電視摟~\n現在新世紀福音戰士要開播了"]

        self.speaker = ["小男孩"]
        self.dialog = ["別再管功課了，來去看新世紀福音戰士摟~"]

        self.music = [(pencil_writing_sound,0),(mute,1)]
        self.show_image = [(black_image,0)]

        self.show_doing = Show(self.dialog_doing, self.speaker_doing, self.show_image, self.music, None)
        self.show_undone = Show(self.dialog_undone, self.speaker_undone, None, None, None)

        self.show = Show(self.dialog, self.speaker, None, None, None)

        self.is_done = False

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            if not self.is_done:
                return 'homework'
            else:
                return 'dialog'
    def done(self):
        self.is_done = True
        self.image = homework_image[1]
class CalendarCh2:
    def __init__(self, x, y):
        self.image = calendar_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

        self.speaker = ["小男孩"]
        self.dialog = ["我最喜歡每天撕日曆，在日曆後面畫畫了"]
        self.music = None

        self.show = Show(self.dialog, self.speaker, None, self.music, None)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'dialog'

# globe =====================================================================
class GlobeCh2:
    def __init__(self, x, y):
        self.image = globe_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

        self.speaker = ["旁白"]
        self.dialog = ["你轉動這個地球儀...\n你看到了台灣，中國，日本，美國在你眼前轉過"]

        self.show = Show(self.dialog, self.speaker, None, None, None)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x - self.rect.x, y - self.rect.y)) != 0:
            return 'dialog'

class BoxCh2:
    def __init__(self,x,y):
        self.image = box_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

        self.speaker = ["旁白","","旁白"]
        self.speaker_2 = ["旁白"]
        self.dialog = ["你翻找著這些紙箱堆..."," ","裡面好像藏了些甚麼\n有了\n是一個黨徽"]
        self.dialog_2 = ["紙箱已經被你翻得亂七八糟了\n裡頭好多無辜陶器都被你用碎了\n紙箱裡面都被碎片染成白色，有夠恐怖\n別再翻了"]
        # 是否互動過(獲得黨徽
        self.lock = False
        self.give = Kmt(GAME_X, GAME_Y)

        self.show = Show(self.dialog, self.speaker, None, None, None)
        self.show_2 = Show(self.dialog_2, self.speaker_2, None, None, None)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x - self.rect.x, y - self.rect.y)) != 0:
            if not self.lock:
                self.lock = True
                return 'dialog_sp'
            else:
                return 'dialog'
            
class Newspaper:
    def __init__(self, x, y):
        self.image = newspaper_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

        self.speaker = ["1999年9月份的報紙"]
        self.index = 0
        self.dialogs = [
                        ["一名陳姓中國男子，因小孩驗血驗出B型而非A+型\n因而對小孩失望透頂進而腦中風"],
                        ["英國研究指出，十次車禍七次快\n一次飛碟\n一次阿北\n一次英文報告"],
                        ["廣告版面出租"],
                        ["今早一名男性青年，在過馬路時被大卡車撞飛\n目擊民眾表示，當時聽見有人大喊「麥可!!」\n隨後就看到車禍男子被撞飛了5層樓高、100米遠"],
                        ["\"破壞之王\"上映後票房大受好評，其中的經典台詞更是受到許多人的喜愛\n*以下是劇照的截圖\n「不是...不要誤會，我不是針對你」\n「我是說在座的各位...」\n「都是垃圾」"],
                        ["一名南部大學學生，因對其他組別的作品說出\"破壞之王\"經典台詞，因而引發各組圍毆\n最終造成4人輕傷"]
                        ]
        self.dialog = self.dialogs[self.index]
        self.music = None

        self.show = Show(self.dialog, self.speaker, None, self.music, None)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x - self.rect.x, y - self.rect.y)) != 0:
            self.index += 1
            if self.index == len(self.dialogs):
                self.index = 0
            self.dialog = self.dialogs[self.index]
            self.show.text = self.dialog
            return 'dialog'
        else:
            return 0
            
class GlobeTableCh2:
    def __init__(self, x, y):
        self.image = globe_table_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

        self.speaker = ["小男孩"]
        self.dialog = ["這個櫃子是我和爺爺一起做的\n爺爺答應我說等我再大一點，要教我做更厲害的木製家具"]
        self.music = None  # [(clock_sound, 0)]

        self.show = Show(self.dialog, self.speaker, None, self.music, None)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x - self.rect.x, y - self.rect.y)) != 0:
            return 'dialog'
        else:
            return 0

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
        
class Pencil:
    def __init__(self, x, y):
        self.name = "筆芯斷掉的鉛筆"
        self.icon = pencil_icon[1]
        # 調查中此物品的樣貌
        self.observe = pencil_observe[1]
        # 調查中此物品的敘述
        self.description = "一定是掉到地上，又或者是受潮後寫的太用力\n才會讓筆芯斷掉"

        self.is_sharp = False
        self.level = 0
        self.music = sharping_sound

    def sharp(self):
        self.music.stop()
        if not self.is_sharp:
            self.music.play()
            self.is_sharp = True
            self.name = "削尖的鉛筆"
            self.icon = pencil_icon[0]
            # 調查中此物品的樣貌
            self.observe = pencil_observe[0]
            # 調查中此物品的敘述
            self.description = "千萬不要拿削好的鉛筆戳自己的大腿\n有時候筆芯會斷在肉裡，超級痛\n也不要拿上面的橡皮擦來用\n" \
                               "用了你的紙張會直接毀滅"
        elif self.level < 10:
            self.music.play()
            self.level += 1
            self.name = "削尖的鉛筆 +"  + str(self.level)
            if self.level == 10:
                self.music.stop()
                item_found_rarest_sound.play()
                # self.icon = pencil_icon[2]
                self.observe = pencil_observe[2]
                self.name = "天上天下天地無雙筆"
                self.description = "追求最強之名而生的豪傑之筆。\n強者皆敗，彼亦神隱。\n" \
                                   "他擁有最高的白色斬味\n可以輕易刺穿世界上的一切物質\n" \
                                   "將魔物斷尾、破角、大卸八塊更是不在話下\n" \
                                   "當然也包括你的作業本...\n\n\n\n\n\n\n\n\n                      BGM:英雄之証"
                
class BambooHat:
    def __init__(self, x, y):
        self.name = "斗笠"
        self.icon = bamboo_hat_icon
        # 調查中此物品的樣貌
        self.observe = bamboo_hat_observe
        # 調查中此物品的敘述
        self.description = "以深色的竹子編織而成，經歷了風吹日曬雨淋\n" \
                           "如今已退色，剩下殘留在上頭的汗味"

        self.x = x
        self.y = y
        self.music = pick_up_items_sound



class Top:
    def __init__(self, x, y):
        self.name = "陀螺"
        self.image = top_image
        # 放入物品欄後顯示的圖示
        self.icon = top_icon
        # 調查中此物品的樣貌
        self.observe = top_observe
        # 調查中此物品的敘述
        self.description = "老舊的陀螺，有一定的重量\n" \
                           "在抓到訣竅前很難將其轉動"
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
        
class Beer:
    def __init__(self, x, y):
        self.name = "空啤酒瓶"
        self.image = beer_image
        # 放入物品欄後顯示的圖示
        self.icon = beer_icon
        # 調查中此物品的樣貌
        self.observe = beer_observe
        # 調查中此物品的敘述
        self.description = "台灣啤酒的空瓶\n" \
                           "沁涼的啤酒適合搭配著熱炒一起享用\n" \
                           "在炎熱的夏天，阿公晚上偶爾會開一瓶來喝\n" \
                           "\n" \
                           "(歡迎台灣啤酒冠名贊助 :) )"

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

class Kmt:
    def __init__(self, x, y):
        self.name = "國民黨黨徽"
        self.image = beer_image
        # 放入物品欄後顯示的圖示
        self.icon = kmt_icon
        # 調查中此物品的樣貌
        self.observe = kmt_observe
        # 調查中此物品的敘述
        self.description = "這個黨徽有一天不小心被紅色油漆潑到\n" \
                           "所以變成紅色的了\n" \
                           "我有嘗試把油漆清掉，但怎麼清也清不乾淨\n" \
                           "反而把沒沾到油漆的部分刮花，讓他繡成全紅"
        self.music = pick_up_items_sound

# 彩蛋物件類 =====================================
class AbandonedProject:
    def __init__(self, x, y):
        self.name = "專案磁碟"
        self.icon = shit_icon
        # 調查中此物品的樣貌
        self.observe = shit_observe
        # 調查中此物品的敘述
        self.description = "過於狗屎導致無人使用，進而荒廢已久的專案\n" \
                           "由祖傳程式碼撰寫而成\n" \
                           "其特色是: 換皮、改變數、做工粗糙\n" \
                           "背面還刻著一行文字\n" \
                           "「一年抄一年;年年做大便」"

        self.music = pick_up_items_sound