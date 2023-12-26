import pygame
import os


from object import *
from room import *
import random
from bag import *
from show import *
from text import *

# from menu import UpgradeMenu, BuildMenu, MainMenu
# from user_request import RequestSubject, TowerFactory, TowerSeller, TowerDeveloper, EnemyGenerator, Mute, Music, Continue, Pause
from setting import *


class GameModel:
    def __init__(self):
        # data
        # 基礎背景(全黑)
        self.bg_image = pygame.transform.scale(BACKGROUND_IMAGE, (WIN_WIDTH, WIN_HEIGHT))
        # 選單按鈕
        self.btn = MenuButton(910, 50)
        # 當前章節
        self.chapter = 1
        # 本章節會用到的所有房間
        self.room = None
        # 當前房間
        self.cur_room = None
        # 當前牆面
        self.wall = 1
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
        # 對話框的說話者
        self.speaker = ""
        # 下方對話框文字
        self.dialog = ""
        # 下方對話框文字的index
        self.dialog_index = 0
        # 是否在調查手中物品
        self.observe = False
        # 在播的動畫
        self.show = None

        # 第一章的包包
        self.bag_ch1 = Bag()
        # 第二章的包包
        self.bag_ch2 = Bag()
        # 物品欄
        self.bag = self.bag_ch1
        # 物品欄換頁按鈕
        self.page_bnt = BagPageButton()




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


    # 在 update_model 裡()
    def get_request(self, events: dict):
        """get keyboard response or button response"""
        # initial

        # 叫出選單
        if events["keyboard key"] == pygame.K_ESCAPE:
            # TODO : 叫出暫停選單
            pass
            return

        # 檢查 menu btn
        if events["mouse position"] is not None:
            x, y = events["mouse position"]
            if self.btn.clicked(x, y) == 'menu':
                # TODO : 叫出暫停選單
                pass
                return

        if self.switch:
            # 讓後面部分不執行
            return

        if self.show is not None:
            # 在播動畫 後面不執行
            if events["mouse position"] is not None:
                common = self.show.next()
                if common == 'end':
                    self.show = None

            return


        # 如果在對話 執行對話功能 並讓後面部分不執行
        if self.dialog != "":
            if events["mouse position"] is not None:
                # 點擊以下一句
                self.dialog_index += 1

                # 代表話說完了 對話結束 做初始化
                if len(self.dialog.splitlines()) == self.dialog_index:
                    self.dialog_index = 0
                    self.dialog = ""

            # 讓後面部分不執行
            return

        # 調查手中物件
        # 如果在轉場 或是對話中 無法執行操作
        if events["keyboard key"] == pygame.K_f and self.observe == False and self.bag.hold is not None:
            # 跳出調查手中物品畫面
            self.start_observe()
        elif events["keyboard key"] == pygame.K_f and self.observe:
            self.end_observe()
        # 電視輸入指令彩蛋
        elif events["keyboard key"] is not None and isinstance(self.investigation_item, Tv) and self.investigation_item.easter_eggs == False:
            self.investigation_item.input(events["keyboard key"])
            pass


        # 點擊物件 調查 解謎
        # 如果在轉場中 或是調查手中物品時 或是對話中 無法執行操作
        if not self.observe:
            if events["mouse position"] is not None:
                x, y = events["mouse position"]
                # 重製對話
                self.text = ""
                # 檢查物品欄
                self.bag.clicked(x, y)
                # 物品欄切換
                page = self.page_bnt.clicked(x, y)
                if page == 'right' and self.bag.page < 2:
                    self.bag.page += 1
                elif page == 'left' and self.bag.page > 1:
                    self.bag.page -= 1

                if self.investigation:
                    if isinstance(self.investigation_item, Tv):
                        self.tv_select(x, y)
                    elif isinstance(self.investigation_item, Painting):
                        self.painting_select(x, y, 'down')
                    elif isinstance(self.investigation_item, TvShelf):
                        self.tv_shelf_select(x, y)
                    elif isinstance(self.investigation_item, BookShelf):
                        self.book_shelf_select(x, y)
                    elif isinstance(self.investigation_item, Clock):
                        self.clock_select(x, y)
                    elif isinstance(self.investigation_item, Desk):
                        self.desk_select(x, y)
                    elif isinstance(self.investigation_item, PhotoFrame):
                        self.photo_frame_select(x, y, 'down')
                    else:
                        pass
                elif not self.investigation :
                    self.basic_function(x, y)
                else:
                    pass
            if events["mouse motion"] is not None:
                if self.investigation:
                    if isinstance(self.investigation_item, PhotoFrame):
                        self.photo_frame_select(0, 0, events["mouse motion"])
                    elif isinstance(self.investigation_item, Painting):
                        self.painting_select(0, 0, events["mouse motion"])
            if events["release button"]:
                if self.investigation:
                    if isinstance(self.investigation_item, PhotoFrame):
                        self.photo_frame_select(0, 0, 'up')
                    elif isinstance(self.investigation_item, Painting):
                        self.painting_select(0, 0, 'up')





    def start_observe(self):
        self.observe = True
    def end_observe(self):
        self.observe = False

    def painting_select(self, mouse_x: int, mouse_y: int, events):
        for item in reversed(self.investigation_item.object):
            if events == 'down':
                common = item.clicked(mouse_x, mouse_y)
                if common == 'stop_investigation':
                    self.investigation_item = self.investigation_item.enter
                    if not self.investigation_item:
                        self.investigation = False
                    self.switch = True
                elif common == 'drag':
                    item.drag_set()
                    break
                # 點擊畫作 如果手上有膠片 就放上去
                elif  self.investigation_item.rect.collidepoint(mouse_x, mouse_y) and isinstance(self.bag.hold, DecipherCard):
                    self.bag.remove_hold_item()
                    # 故意不讓他是對準好的
                    self.investigation_item.object.append(DecipherCardPuzzle(GAME_X + 190, GAME_Y + 90))


                else:
                    pass
            elif not isinstance(item,DecipherCardPuzzle):
                pass
            elif events == 'up':
                item.release()
            else:
                item.move(events)

    def tv_shelf_select(self, mouse_x: int, mouse_y: int):
        for item in reversed(self.investigation_item.object):
            common = item.clicked(mouse_x, mouse_y)
            if common == 'stop_investigation':
                self.investigation_item = self.investigation_item.enter
                if not self.investigation_item:
                    self.investigation = False
                self.switch = True
            elif common == 'door':
                break
            elif common == 'take':
                self.bag.save_item(item)
                self.investigation_item.object.remove(item)
            elif common == 'investigation':
                item.enter = self.investigation_item
                self.investigation_item = item
            else:
                pass

    def tv_select(self, mouse_x: int, mouse_y: int):
        for item in reversed(self.investigation_item.object):
            common = item.clicked(mouse_x, mouse_y)
            if common == 'stop_investigation':
                if self.investigation_item.tvshow.music:
                    self.investigation_item.tvshow.music.stop()
                self.investigation_item = self.investigation_item.enter
                if not self.investigation_item:
                    self.investigation = False
                self.switch = True

            elif common == 'switch':
                self.investigation_item.tvshow.switch()
                if self.investigation_item.tvshow.ispower:
                    item.music.play()

            elif common == 'shotdown':
                self.investigation_item.tvshow.power()
            elif common == 'dialog':
                self.dialog = item.dialog
                self.speaker = item.speaker
            elif common == 'take':
                self.bag.save_item(item)
                self.investigation_item.object.remove(item)
            else:
                pass


    def book_shelf_select(self, mouse_x: int, mouse_y: int):
        for item in reversed(self.investigation_item.object):
            common = item.clicked(mouse_x, mouse_y)
            if common == 'stop_investigation':
                self.investigation_item = self.investigation_item.enter
                if not self.investigation_item:
                    self.investigation = False
                self.switch = True
            elif common == 'door':
                break
            elif common == 'close':
                if isinstance(self.bag.hold, Handle):
                    item.add_handle()
                    self.bag.remove_hold_item()
                else:
                    self.dialog = "沒有把手轉不動"
                    # self.text = "沒有把手轉不動"
                break
            elif common == 'check':
                if self.investigation_item.unlock:
                    item.open = True
                    item.unlock()
                    self.investigation_item.remove_knob()
                else:
                    self.dialog = "咬的緊緊的...轉不開"
                    # self.text = "咬的緊緊的...轉不開"
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
            elif common == 'investigation':
                item.enter = self.investigation_item
                self.investigation_item = item
            else:
                pass

    def clock_select(self, mouse_x: int, mouse_y: int):
        for item in reversed(self.investigation_item.object):
            # 回傳是哪個物件被點選 進而做出不同反應
            common = item.clicked(mouse_x, mouse_y)
            # 退出調查畫面
            if common == 'stop_investigation':
                self.investigation_item = self.investigation_item.enter
                if not self.investigation_item:
                    self.investigation = False
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
                self.dialog = "指針好像卡死了..."
                # self.text = "指針好像卡死了..."
            elif common == 'take':
                self.bag.save_item(item)
                self.investigation_item.object.remove(item)
            else:
                pass

    # TODO : 完成他
    def desk_select(self, mouse_x: int, mouse_y: int):
        for item in reversed(self.investigation_item.object):
            # TODO : 若是可互動物件被點到 轉換場景 若是不可互動則說話或是
            # 回傳是哪個物件被點選 進而做出不同反應
            common = item.clicked(mouse_x, mouse_y)
            if common == 0:
                pass
            # 退出調查畫面
            elif common == 'stop_investigation':
                self.investigation_item = self.investigation_item.enter
                if not self.investigation_item:
                    self.investigation = False
                self.switch = True
            else:
                pass

    def photo_frame_select(self, mouse_x: int, mouse_y: int, events):
        for item in reversed(self.investigation_item.object):
            if events == 'down':
                if isinstance(self.bag.hold, PhotoFragmentsTake) and self.investigation_item.rect.collidepoint(mouse_x, mouse_y):
                    self.investigation_item.add_fragments(self.bag.hold)
                    self.bag.remove_hold_item()
                    return
                common = item.clicked(mouse_x, mouse_y)
                if common == 'stop_investigation':
                    self.investigation_item = self.investigation_item.enter
                    if not self.investigation_item:
                        self.investigation = False
                    self.switch = True
                # 除了被點到 還要確定滑鼠是按住的才能拖動
                elif common == 'drag':
                    item.drag_set()
                    # 避免重疊的一起點到
                    break
                else:
                    pass
            elif not isinstance(item,PhotoFragments):
                pass
            elif events == 'up':
                common = item.release()
                if common == 'lock':
                    common = self.investigation_item.fix()
                    if common == 'done':
                        print("拚好了 進CH2")
                        self.start_ch2()
            else:
                item.move(events)


    def basic_function(self, mouse_x: int, mouse_y: int):
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

            # 回傳的是可調查物件的 self
            elif common == 'investigation':
                self.investigation = True
                self.investigation_item = item
                pass

            elif common == 'take':
                self.bag.save_item(item)
                self.cur_room.wall[str(self.wall)].object.remove(item)
            elif common == 'speak':
                # TODO : 考慮不同文字出現位置
                # self.text_pos
                self.text = item.text[item.text_index]
                item.text_index += 1
                if item.text_index == item.text_size:
                    item.text_index = 0
            elif common == 'dialog':
                self.dialog = item.dialog
                self.speaker = item.speaker

            elif common == 'none':
                pass
            else:
                pass


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

        # 開場動畫
        # self.show = Show(CH1_START_TEXT,CH1_START_SPEAKER,CH1_START_IMAGE)

        pass
    def start_ch2(self):
        # TODO :　清除上一章的物件(可選)
        # TODO :　建立房間/物品/可互動元素
        # 當前章節
        self.chapter = 2
        # 本章節會用到的所有房間
        self.room = {'living_room': LivingRoom(),
                     'study': Study(),
                     'bedroom': Bedroom()}
        # 當前房間
        self.cur_room = self.room['living_room']
        # 當前牆面
        self.wall = 1
        # 是否有在調查物件
        self.investigation = False
        # 在調查哪個物件
        self.investigation_item = None
        # 是否在轉場
        self.switch = False
        # 對話框文字
        self.text = ""
        # 文字位置(尚未使用)
        self.text_pos = (0, 0)
        # 對話框的說話者
        self.speaker = ""
        # 下方對話框文字
        self.dialog = ""
        # 下方對話框文字的index
        self.dialog_index = 0
        # 是否在調查手中物品
        self.observe = False
        # 物品欄
        self.bag = self.bag_ch2

        self.show = Show(CH2_START_TEXT, CH2_START_SPEAKER, CH2_START_IMAGE)
        pass
    def start_ch3(self):
        # TODO :　清除上一章的物件(可選)
        # TODO :　建立房間/物品/可互動元素
        pass
    def start_ch4(self):
        # TODO :　清除上一章的物件(可選)
        # TODO :　建立房間/物品/可互動元素
        pass
    def test_init(self):
        self.room = {'living_room': LivingRoom(),
                     'study': Study(),
                     'bedroom': Bedroom()}
        self.cur_room = self.room['living_room']
        self.investigation = True
        self.investigation_item = PhotoFrame(GAME_X, GAME_Y)



    @property
    def is_pause(self):
        return self._is_pause