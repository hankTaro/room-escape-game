import pygame
import os


from object import *
from room import *
import random
from bag import *

# from menu import UpgradeMenu, BuildMenu, MainMenu
# from user_request import RequestSubject, TowerFactory, TowerSeller, TowerDeveloper, EnemyGenerator, Mute, Music, Continue, Pause
from setting import *


class GameModel:
    def __init__(self):
        # data
        # 基礎背景(全黑)
        self.bg_image = pygame.transform.scale(BACKGROUND_IMAGE, (WIN_WIDTH, WIN_HEIGHT))
        # 當前章節
        self.chapter = 1
        # 本章節會用到的所有房間
        self.room = None
        # 當前房間
        self.cur_room = None
        # 當前牆面
        self.wall = 1
        # 玩家點選的物件
        self.selected_button = None
        # 選單按鈕
        self.btn = MenuButton(900,50)
        # 是否有在調查物件
        self.investigation = False
        # 在調查哪個物件
        self.investigation_item = None
        # 是否在轉場
        self.switch = False
        # 對話框文字
        self.text = ""
        #文字位置(尚未使用)
        self.text_pos = (0,0)

        # 物品欄
        self.bag = Bag()




        self._is_pause = False

    # 使用 chapter, wall 與 room 的數值來判斷要畫出甚麼畫面(思考是否要用這方法，而非直接讓不同房間的移動按鈕指向不同房間)

    # 叫出esc選單
    def call_menu(self):
        #TODO : 完成選單
        pass

    # TODO : 轉場淡入淡出(原本的畫面>逐漸全黑>黑逐漸消失>新房間) 可以用透明度作
    # (不用)在這段期間要讓所有物件無法被互動 目前想法是做一個 empty room 轉場時讓 cur_room 指向他 才不會有物件
    def switch_scene(self, target_room):


        surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
        transparency = 120

        pygame.draw.rect(surface, (0, 0, 0, transparency), (0,0))
        pass




    # TODO : 轉換房間/牆面/與切換調查物件視角 底線為牆面編號 也就是第幾號牆
    # TODO : 將各物件初始化好(需要儲存玩家動過的東西，不能從新進去出來東西就reset)
    def to_living_room(self):
        self.switch = True
        if self.cur_room == self.room['bedroom'] or self.cur_room == self.room['study']:
            self.wall = 2
        else:
            self.wall = 3 #連接廚房的牆

        self.cur_room = self.room['living_room']
    def to_study(self):
        self.switch = True
        self.wall = 1
        self.cur_room = self.room['study']
    def to_kitchen(self):
        self.switch = True
        pass
    def to_bedroom(self):
        self.switch = True
        self.wall = 1
        self.cur_room = self.room['bedroom']

    # 前往右手邊的牆
    def switch_r_wall(self):
        self.switch = True
        self.wall = (self.wall % self.cur_room.wall_size) + 1
        # self.cur_room.bg_image[self.wall - 1]

    # 前往左手邊的牆
    def switch_l_wall(self):
        self.switch = True
        if self.wall == 1:
            self.wall = self.cur_room.wall_size
        else:
            self.wall -= 1


    # 要預先儲存是在哪個房間點擊這個物件的，以便回到原本點擊的地方 (可選)
    def to_newspaper(self):
        pass



    # 在 update_model 裡()
    def get_request(self, events: dict):
        """get keyboard response or button response"""
        # initial
        self.selected_button = None
        # key event
        if events["keyboard key"] == pygame.K_ESCAPE:
            # TODO : 叫出暫停選單
            pass
        # mouse event
        if events["mouse position"] is not None:
            x, y = events["mouse position"]
            # 如果在轉場中 無法點擊物件
            if self.switch == True:
                pass
            else:
                self.select(x, y)

    # TODO : 判別是哪一個物件被點到
    def select(self, mouse_x: int, mouse_y: int) -> None:
        """change the state of whether the items are selected"""

        # 重製對話
        self.text = ""
        # TODO : 在調查中就不檢查房間物件是否被點擊 反之在房間中就不檢查物件調查畫面的點擊
        # if the item is clicked, select the item

        # 檢查物品欄
        self.bag.clicked(mouse_x, mouse_y)

        if self.investigation:
            # TODO : 看看要不要對應不同調查物件設立不同判斷式
            if isinstance(self.investigation_item, Tv):
                for item in self.investigation_item.object:
                    # TODO : 若是可互動物件被點到 轉換場景 若是不可互動則說話或是
                    # 回傳是哪個物件被點選 進而做出不同反應
                    common = item.clicked(mouse_x, mouse_y)
                    if common == 0:
                        pass
                    # 退出調查畫面
                    elif common == 'stop_investigation':
                        self.investigation = False
                        self.investigation_item = None
                        self.switch = True
                    else:
                        pass
            elif isinstance(self.investigation_item, BookShelf):
                for item in reversed(self.investigation_item.object):
                    common = item.clicked(mouse_x, mouse_y)
                    if common == 'stop_investigation':
                        self.investigation = False
                        self.investigation_item = None
                        self.switch = True
                    elif common == 'door':
                        break
                    elif common == 'close':
                        if isinstance(self.bag.hold, Handle):
                            item.add_handle()
                        else:
                            self.text = "沒有把手轉不動"
                        break
                    elif common == 'check':
                        if self.investigation_item.unlock:
                            item.open = True
                            item.unlock()
                            self.investigation_item.remove_knob()
                        else:
                            self.text = "咬的緊緊的...轉不開"
                        break
                    elif common == 'take':
                        self.bag.save_item(item)
                        self.investigation_item.object.remove(item)
                    elif common == 'knob':
                        self.investigation_item.input[item.num] = item.index
                        if self.investigation_item.ans == self.investigation_item.input:
                            self.investigation_item.unlock = True
                        else:
                            self.investigation_item.unlock = False
                        break


                    else:
                        pass
            elif isinstance(self.investigation_item, Clock):
                for item in reversed(self.investigation_item.object):
                    # 回傳是哪個物件被點選 進而做出不同反應
                    common = item.clicked(mouse_x, mouse_y)
                    # 退出調查畫面
                    if common == 'stop_investigation':
                        self.investigation = False
                        self.investigation_item = None
                        self.switch = True
                    elif common == 'move':
                        # 檢查指針是否對應到答案
                        if item.index == item.ans:
                            if isinstance(item, Hr):
                                self.investigation_item.hr_right = True
                            else:
                                self.investigation_item.min_right = True
                        else:
                            if isinstance(item, Hr):
                                self.investigation_item.hr_right = False
                            else:
                                self.investigation_item.min_right = False
                        if self.investigation_item.min_right == True and self.investigation_item.hr_right == True:
                            self.investigation_item.open()
                            self.investigation = False
                            self.investigation_item = None

                        break
                    elif common == 'lock':
                        self.text = "指針好像卡死了..."
                    elif common == 'take':
                        self.bag.save_item(item)
                        self.investigation_item.object.remove(item)
                    else:
                        pass
            elif isinstance(self.investigation_item, Desk):
                for item in reversed(self.investigation_item.object):
                    # TODO : 若是可互動物件被點到 轉換場景 若是不可互動則說話或是
                    # 回傳是哪個物件被點選 進而做出不同反應
                    common = item.clicked(mouse_x, mouse_y)
                    if common == 0:
                        pass
                    # 退出調查畫面
                    elif common == 'stop_investigation':
                        self.investigation = False
                        self.investigation_item = None
                        self.switch = True
                    else:
                        pass
            else:
                pass


        else:
            for item in self.cur_room.wall[str(self.wall)].object:
                # TODO : 若是可互動物件被點到 轉換場景 若是不可互動則說話或是
                # 回傳是哪個物件被點選 進而做出不同反應
                common = item.clicked(mouse_x, mouse_y)
                if common == 0:
                    pass
                elif common == 'right':
                    # 往右
                    self.switch_r_wall()
                elif common == 'left':
                    self.switch_l_wall()
                elif common == 'bedroom':
                    self.to_bedroom()
                elif common == 'living_room':
                    self.to_living_room()
                elif common == 'study':
                    self.to_study()

                # # 退出調查畫面
                # elif common == 'stop_investigation':
                #     self.investigation = False
                #     self.investigation_item = None

                # 回傳的是可調查物件的 self
                elif common == 'investigation':
                    self.investigation = True
                    self.investigation_item = item
                    pass
                elif common == 'speak':
                    # TODO : 考慮不同文字出現位置
                    # self.text_pos
                    self.text = item.text[item.text_index]
                    item.text_index += 1
                    if item.text_index == item.text_size:
                        item.text_index = 0
                elif common == 'none':
                    pass
                else:
                    pass

        # menu btn
        self.btn.clicked(mouse_x, mouse_y)

    # TODO : 章節初始化
    # 開始畫面點選開始就先做第一章起始化
    # 第一張結束後自動執行第二張初始化 依此類推
    # TODO : 初始化需要依照 room 的架構方式來考慮是否要清除舊物件
    #  若每一章的房間為獨立物件 則不一定要清除 但清掉會比較好 乾淨嘛 也比較不肥 也不容易 memory leak 大專案就一定要清
    def start_ch1(self):
        # TODO :　建立房間/物品/可互動元素
        self.room = {'living_room': LivingRoom(),
                      'study': Study(),
                      'bedroom': Bedroom()}
        self.cur_room = self.room['living_room']

        pass
    def start_ch2(self):
        # TODO :　清除上一章的物件(可選)
        # TODO :　建立房間/物品/可互動元素
        pass
    def start_ch3(self):
        # TODO :　清除上一章的物件(可選)
        # TODO :　建立房間/物品/可互動元素
        pass
    def start_ch4(self):
        # TODO :　清除上一章的物件(可選)
        # TODO :　建立房間/物品/可互動元素
        pass



    @property
    def is_pause(self):
        return self._is_pause