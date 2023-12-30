import pygame
import os
from functools import partial

from object import *
from room import *
from room_ch2 import *
import random
from bag import *
from show import *
from text import *

# from menu import UpgradeMenu, BuildMenu, MainMenu
# from user_request import RequestSubject, TowerFactory, TowerSeller, TowerDeveloper, EnemyGenerator, Mute, Music, Continue, Pause
from setting import *

pick_up_items_sound = pygame.mixer.Sound('music/物品拾取聲.mp3')

# pygame.mixer.init()
# pygame.mixer.music.set_volume(0.2)

proof_of_hero = pygame.mixer.Sound('music/MH4　BGM　英雄の証.mp3')
proof_of_hero.set_volume(0.5)

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
        # 下方對話框文字
        self.dialog = None
        # 是否在調查手中物品
        self.observe = False
        # 在播的動畫
        self.show = None
        # 是否在開場畫面
        self.opening = None
        # 亮度
        self.value = 0
        # 開始變暗
        self.to_dark = False
        # 等待時間
        self.wait_time = 0

        # 第一章的包包
        self.bag_ch1 = Bag()
        # 第二章的包包
        self.bag_ch2 = Bag()
        # 物品欄
        self.bag = self.bag_ch1
        # 物品欄換頁按鈕
        self.page_bnt = BagPageButton()
        # 暫存對話完要給予的物品
        self.give_item = None

        # 存第一章的room
        self.room_ch1 = {'living_room': LivingRoom(),
                      'study': Study(),
                      'bedroom': Bedroom()}
        self.room_ch2 = {'living_room': LivingRoomCh2(),
                     'study': Study(),
                     'bedroom': Bedroom()}


        # BGM
        self.bgm = None

        # 片尾動畫
        self.ending_mp4 = None

        #動畫結束後要執行的指令
        self.continue_function = None

        # 等待結束後要執行的指令
        self.continue_function_wait = None

        # 變黑完要執行的指令
        self.continue_function_d = None

        # show 撥完後要執行的指令
        self.continue_show = None

        # 固定畫面 在全黑前 不更新畫面
        self.fix_scream_to_dark = False




        self._is_pause = None

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

        # 任何需要等待時
        if self.wait_time > 0:
            self.wait_time -= 1
            if self.wait_time <= 0:
                self.wait_time = 0
                if self.continue_function_wait is not None:
                    for func in self.continue_function_wait:
                        func()
                    self.continue_function_wait = None
            return

        # 任何需要畫面變黑時
        if self.to_dark:
            self.value += 5
            if self.value >= 255:
                self.to_dark = False
                self.fix_scream_to_dark = False
                self.value = 0
                if self.continue_function_d is not None:
                    for func in self.continue_function_d:
                        func()
                    self.continue_function_d = None
            return

        # 在開場
        if self.opening is not None:
            # 變暗過程結束
            if not self.to_dark:
                self.opening = None
                self.start_ch1()

            if events["mouse position"] is not None:
                x, y = events["mouse position"]
                common = self.opening.clicked(x, y)
                if common == 'start':
                    self.start_darking()
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
            # 檢測是否是動畫剛開始
            self.show.start()

            # 等待音效播完
            if self.show.lock:
                if self.show.wait_sound():
                    return

            if events["mouse position"] is not None:
                common = self.show.next()
                if common == 'end':
                    self.show = None
                    if self.continue_show is not None:
                        self.show = self.continue_show.pop()
                        if not self.continue_show:
                            self.continue_show = None
                        # 確保所有動畫播完才執行function
                        return
                    # show 播完要連續執行的指令
                    if self.continue_function is not None:
                        for func in self.continue_function:
                            func()
                        self.continue_function = None


            return

        # 如果在對話 執行對話功能 並讓後面部分不執行
        if self.dialog is not None:
            # 檢測是否是動畫剛開始
            self.dialog.start()

            # 等待音效播完
            if self.dialog.lock:
                if self.dialog.wait_sound():
                    return

            if events["mouse position"] is not None:
                common = self.dialog.next()
                if common == 'end':
                    if self.give_item is not None:
                        # 給玩家物品
                        pick_up_items_sound.play()
                        self.bag.save_item(self.give_item)
                        self.give_item = None
                    # 動畫播完要連續執行的指令
                    if self.continue_function is not None:
                        for func in self.continue_function:
                            func()
                        self.continue_function = None

                    self.dialog = None

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
                    if isinstance(self.investigation_item, Tv) or isinstance(self.investigation_item, TvCh2):
                        self.tv_select(x, y)
                    elif isinstance(self.investigation_item, Painting):
                        self.painting_select(x, y, 'down')
                    elif isinstance(self.investigation_item, TvShelf) or isinstance(self.investigation_item, TvShelfCh2):
                        self.tv_shelf_select(x, y)
                    elif isinstance(self.investigation_item, BookShelf) or isinstance(self.investigation_item, BookShelfCh2):
                        self.book_shelf_select(x, y)
                    elif isinstance(self.investigation_item, Clock) or isinstance(self.investigation_item, BookShelfCh2):
                        self.clock_select(x, y)
                    elif isinstance(self.investigation_item, Desk) or isinstance(self.investigation_item, DeskCh2):
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
        # BGM 檢測
        if self.bag.hold.name == "天上天下天地無雙筆":
            proof_of_hero.play()
    def end_observe(self):
        self.observe = False
        if self.bag.hold.name == "天上天下天地無雙筆":
            proof_of_hero.stop()



    def painting_select(self, mouse_x: int, mouse_y: int, events):
        for item in reversed(self.investigation_item.object):
            if events == 'down':
                common = item.clicked(mouse_x, mouse_y)
                if common == 'stop_investigation':
                    self.stop_investigation()
                elif common == 'drag':
                    item.drag_set()
                    break
                # 點擊畫作 如果手上有膠片 就放上去
                elif  self.investigation_item.rect.collidepoint(mouse_x, mouse_y) and isinstance(self.bag.hold, DecipherCard):
                    self.bag.hold.music.play()
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
                self.stop_investigation()
            elif common == 'door':
                break
            elif common == 'take':
                self.bag.save_item(item)
                self.investigation_item.object.remove(item)
            elif common == 'investigation':
                item.enter = self.investigation_item
                self.investigation_item = item
            elif common == 'sharp':
                if isinstance(self.bag.hold,Pencil):
                    self.dialog = item.show
                    if self.bag.hold.level < 10:
                        self.bag.hold.sharp()
                        if self.bag.hold.is_sharp:
                            item.sharp()
                    # 設定爺爺對話的改變
                    self.cur_room.bedroom_door.pencil_sharp(self.bag.hold.level)



            else:
                pass

    def tv_select(self, mouse_x: int, mouse_y: int):
        for item in reversed(self.investigation_item.object):
            common = item.clicked(mouse_x, mouse_y)
            if common == 'stop_investigation':
                if self.investigation_item.tvshow.music:
                    self.investigation_item.tvshow.music.stop()
                self.stop_investigation()

            elif common == 'switch':
                self.investigation_item.tvshow.switch()
            elif common == 'watch':
                self.investigation_item.tvshow.switch()
                #播放男孩的講話
                self.dialog = item.show

                # 將等待的保存起來 講完話再漸暗
                self.continue_function = [partial(self.waiting,7)]
                # 將漸暗的函式保存起來 等待完再漸暗
                self.continue_function_wait = [partial(self.start_darking),partial(self.investigation_item.tvshow.music.fadeout,3000)]
                # 將漸暗完後要執行的函式保存起來
                self.continue_function_d = [partial(self.investigation_item.power_switch),
                                          partial(self.investigation_item.lock_on),
                                          partial(self.stop_investigation),partial(self.set_dialog,self.cur_room.tv.show)]
                # 解鎖大門
                self.cur_room.exit_door.unlock()
                # 改變和阿公的對話
                self.cur_room.bedroom_door.finsh_tv()

            elif common == 'shutdown':
                self.investigation_item.power_switch()
            elif common == 'dialog':
                self.dialog = item.show
            elif common == 'take':
                self.bag.save_item(item)
                self.investigation_item.object.remove(item)

            else:
                pass


    def book_shelf_select(self, mouse_x: int, mouse_y: int):
        for item in reversed(self.investigation_item.object):
            common = item.clicked(mouse_x, mouse_y)
            if common == 'stop_investigation':
                self.stop_investigation()
            elif common == 'door':
                break
            elif common == 'close':
                if isinstance(self.bag.hold, Handle):
                    item.add_handle()
                    self.bag.remove_hold_item()
                else:
                    self.dialog = Show(["沒有把手轉不動"],[""],None,None,None)
                    # self.text = "沒有把手轉不動"
                break
            elif common == 'check':
                if self.investigation_item.unlock:
                    item.open = True
                    item.unlock()
                    self.investigation_item.remove_knob()
                else:
                    self.dialog = Show(["咬的緊緊的...轉不開"],[""],None,None,None)
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
            elif common == 'dialog':
                self.dialog = item.show
            elif common == 'dialog_sp':
                self.dialog = item.show
                item.show = item.show_2
                # 相要給的物品先存起來 對話完再給
                self.give_item = item.give
            else:
                pass

    def clock_select(self, mouse_x: int, mouse_y: int):
        for item in reversed(self.investigation_item.object):
            # 回傳是哪個物件被點選 進而做出不同反應
            common = item.clicked(mouse_x, mouse_y)
            # 退出調查畫面
            if common == 'stop_investigation':
                self.stop_investigation()
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
                pass
            elif common == 'take':
                self.bag.save_item(item)
                self.investigation_item.object.remove(item)
            elif common == 'dialog':
                self.dialog = item.show
            elif common == 'dialog_sp':
                self.dialog = item.show
                item.show = item.show_2
                # 相要給的物品先存起來 對話完再給
                self.give_item = item.give
            else:
                pass

    # TODO : 完成他
    def desk_select(self, mouse_x: int, mouse_y: int):
        for item in reversed(self.investigation_item.object):
            # TODO : 若是可互動物件被點到 轉換場景 若是不可互動則說話或是
            # 回傳是哪個物件被點選 進而做出不同反應
            common = item.clicked(mouse_x, mouse_y)
            # 退出調查畫面
            if common == 'stop_investigation':
                self.stop_investigation()
            elif common == 'dialog':
                self.dialog = item.show
            elif common == 'homework':
                if isinstance(self.bag.hold,Pencil):
                    if  self.bag.hold.is_sharp:
                        # 解鎖電視
                        self.cur_room.tv.unlock()
                        # 和爺爺對話的改變
                        self.cur_room.bedroom_door.finsh_homework()
                        # 進入對話框
                        self.dialog = item.show_doing
                        # 將代辦函式存起來 對話完再執行
                        self.continue_function = [partial(item.done)]
                    else:
                        self.dialog = item.show_undone
            else:
                pass

    def photo_frame_select(self, mouse_x: int, mouse_y: int, events):
        for item in reversed(self.investigation_item.object):
            if events == 'down':
                if isinstance(self.bag.hold, PhotoFragmentsTake) and self.investigation_item.rect.collidepoint(mouse_x, mouse_y):
                    self.bag.hold.music.play()
                    self.investigation_item.add_fragments(self.bag.hold)
                    self.bag.remove_hold_item()
                    return
                common = item.clicked(mouse_x, mouse_y)
                if common == 'stop_investigation':
                    self.stop_investigation()
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
        for item in reversed(self.cur_room.wall[str(self.wall)].object):
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
                self.dialog = item.show
                break
            elif common == 'dialog_sp':
                self.dialog = item.show
                item.show = item.show_2
                # 相要給的物品先存起來 對話完再給
                self.give_item = item.give
            elif common == 'done':
                if self.chapter == 2:
                    self.start_ch3()
            elif common == 'find treasure':
                # 播放最後動畫與結局
                self.show = Show(*CH3_2_END_SHOW)
                # 鎖定畫面 漸暗
                self.continue_function = [self.fix_scream_to_dark_set,self.start_darking]
                # 漸暗完將播放影片
                self.continue_function_d = [self.play_end_mp4]
                pass

            elif common == 'none':
                pass
            else:
                pass


    # TODO : 章節初始化
    # 開始畫面點選開始就先做第一章起始化
    # 第一張結束後自動執行第二張初始化 依此類推
    # TODO : 初始化需要依照 room 的架構方式來考慮是否要清除舊物件
    #  若每一章的房間為獨立物件 則不一定要清除 但清掉會比較好 乾淨嘛 也比較不肥 也不容易 memory leak 大專案就一定要清
    def start_ch0(self):
        self.opening = OpenMenu(0,0)

    def start_ch1(self):
        # TODO :　建立房間/物品/可互動元素
        self.room = self.room_ch1

        self.cur_room = self.room['living_room']

        # 第一章的BMG
        pygame.mixer.music.load('music/ch1_background.mp3')
        pygame.mixer.music.play(-1)  # 無限播放

        # 起始物品
        self.bag.save_item(ChestKey(GAME_X,GAME_Y))

        # 開場動畫
        self.show = Show(*CH1_START_SHOW)

        pass
    def start_ch2(self):

        # 當前章節
        self.chapter = 2
        # 本章節會用到的所有房間
        self.room = self.room_ch2
        # 當前房間
        self.cur_room = self.room['living_room']
        # 當前牆面
        self.wall = 4
        # 是否有在調查物件
        self.investigation = True
        # 在調查哪個物件
        self.investigation_item = self.cur_room.desk
        # 是否在轉場
        self.switch = False
        # 對話框文字
        self.text = ""
        # 文字位置(尚未使用)
        self.text_pos = (0, 0)
        # 下方對話框
        self.dialog = Show(*CH2_START_SHOW)
        # 是否在調查手中物品
        self.observe = False
        # 物品欄
        self.bag = self.bag_ch2

        # 起始物品
        self.bag.save_item(Pencil(GAME_X, GAME_Y))


        # 撥放章節1結束劇情
        self.show = Show(*CH1_END_SHOW)
        # 延遲一小段時間
        for i in range(5000):
            a = i
        pass


    def start_ch3(self):
        # 開場動畫
        # self.show = Show(*CH2_END_SHOW)
        # self.continue_show = [Show(*CH3_START_SHOW)]

        # 當前章節
        self.chapter = 3
        # 本章節會用到的所有房間
        self.room = self.room_ch1
        # 當前房間
        self.cur_room = self.room['living_room']
        # 當前牆面
        self.wall = 2
        # 是否有在調查物件
        self.investigation = True
        # 在調查哪個物件
        self.investigation_item = self.cur_room.book_shelf.photo_frame
        # 是否在轉場
        self.switch = False
        # 下方對話框
        self.dialog = Show(*CH3_END_SHOW)
        # 是否在調查手中物品
        self.observe = False
        # 物品欄
        self.bag = self.bag_ch1
        # 將地球儀櫃子解鎖
        self.cur_room.globe_table.unlock()

        # 對話結束後獲得相片 以及 將相框移除
        self.give_item = AssembledPhoto(GAME_X,GAME_Y)
        self.continue_function = [self.cur_room.book_shelf.photo_frame.clear]


        # self.show = Show(*CH3_START_SHOW)

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

    def start_switching(self):
        self.switch = True
    def start_darking(self):
        self.to_dark = True
    def stop_investigation(self):
        self.investigation_item = self.investigation_item.enter
        if not self.investigation_item:
            self.investigation = False
        self.switch = True
    def waiting(self,sec):
        self.wait_time = sec*FPS
    def set_show(self,show):
        self.show = show
    def set_dialog(self,show):
        self.dialog = show
    def play_end_mp4(self):
        self.ending_mp4 = cv2.VideoCapture("image/living_room/Tv/TV_show/tyler1 scream meme.mp4")
    def fix_scream_to_dark_set(self):
        self.fix_scream_to_dark = True


    @property
    def is_pause(self):
        return self._is_pause