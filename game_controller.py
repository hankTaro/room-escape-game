import pygame
from object import *
from object_ch2 import *

# controller
class GameController:
    def __init__(self, game_model, game_view):
        self.model = game_model
        self.view = game_view
        self.events = {"game quit": False,
                       "mouse position": [0, 0],
                       "keyboard key": 0,
                       "pause": False
                       }
        self.fade_count = 255


        self.request = None  # response of user input

        # 檢查BGM是否被暫停
        self.bgm_paused = False

    def update_model(self):
        """update the model and the view here"""
        self.model.get_request(self.events)
        pass


    # def update_user_request(self):
    #     self.request = self.model.get_request(self.events)
    #     self.model.user_request(self.request)
    #     self.model.call_menu()

    # 在 game loop 裡跑的
    def receive_user_input(self):
        """receive user input from the events"""
        # event initialization
        self.events = {"game quit": False,
                       "mouse position": None,
                       "keyboard key": None,
                       "pause": False,
                       "mouse motion":None,
                       "release button":False
                       }

        #在第二章關閉
        # if self.model.chapter == 2 and self.model.show == None:
        #     self.events["game quit"] = True

        # 當你進入第二章 並且還沒播放過 self.model.cur_room.show_1 時播放
        # if self.model.chapter == 2 and self.model.show == None and self.model.cur_room.show_1 is not None:
        #     self.model.show = self.model.cur_room.show_1
        #     self.model.cur_room.show_1 = None

        # update event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.events["game quit"] = True
            # player press action
            if event.type == pygame.KEYDOWN:
                if event.key is not None:
                    self.events["keyboard key"] = event.key
                # if event.key == pygame.K_ESCAPE:
                #     # 叫出選單
                #     self.events["keyboard key"] = pygame.K_ESCAPE
                # elif event.key == pygame.K_f:
                #     # 調查手中物件
                #     self.events["keyboard key"] = pygame.K_f
            # player click action
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                self.events["mouse position"] = [x, y]

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # 左鍵釋放
                    self.events["release button"] = True

            if event.type == pygame.MOUSEMOTION:
                self.events["mouse motion"] = event.rel





        if self.model.is_pause:
            self.events["pause"] = True
        else:
            self.events["pause"] = False

    def update_view(self):
        # 如果沒有鎖定螢幕 才可以更新畫面
        if not self.model.fix_scream_to_dark:
            # render background
            self.view.draw_bg()

            if self.model.opening is not None:
                self.view.draw_opening(self.model.opening)
                return

            # 播最後動畫
            if self.model.ending_mp4 is not None:
                common = self.view.draw_ending(self.model.ending_mp4)
                if common == 'over':
                    self.model.ending_mp4 = None
                    # 關閉遊戲
                    self.events["game quit"] = True
                return

            # # 畫出選單按鈕
            # self.view.draw_menu_button(self.model.btn)

            # 在播動畫
            if self.model.show is not None:
                # 動畫時暫停BGM
                if not self.bgm_paused:
                    pygame.mixer.music.pause()
                    self.bgm_paused = True
                self.view.draw_show(self.model.show)
                # 畫出選單按鈕
                self.view.draw_menu_button(self.model.btn)
                # 如果在播動畫 不執行下面
                return

            # 畫出選單按鈕
            self.view.draw_menu_button(self.model.btn)

            # TODO : 各房間的場景切換
            if not self.model.investigation:
                self.view.draw_room(self.model.cur_room, self.model.wall)
            else:
                if isinstance(self.model.investigation_item, Tv) or isinstance(self.model.investigation_item, TvCh2):
                    self.view.draw_tv_item(self.model.investigation_item)
                else:
                    self.view.draw_item(self.model.investigation_item)
                pass

            # 轉場檢測
            if self.model.switch == True:
                common = self.view.fade_out(self.fade_count)
                if common == 'end':
                    self.model.switch = False
                    self.fade_count = 255
                else:
                    self.fade_count -= 20
            # 畫出物品欄
            self.view.draw_bag(self.model.bag)
            # 劃出物品頁面切換鍵
            self.view.draw_bag_page(self.model.page_bnt)

            # 劃出對話文字 (依照位置) 目前沒再用
            # if self.model.text != "":
            #     self.view.speak(self.model.text, self.model.text_pos)

            # 劃出對話框(下方固定位置)
            if self.model.dialog is not None:
                # 對話時暫停BGM
                if not self.bgm_paused:
                    pygame.mixer.music.pause()
                    self.bgm_paused = True
                self.view.murmur(self.model.dialog)

            # 畫出手中物品調查頁面
            if self.model.observe:
                self.view.draw_observe(self.model.bag.hold)

            #如果當前沒有對話 沒有動畫則繼續播放BGM
            if  self.model.dialog is None and self.model.show is None:
                if self.bgm_paused:
                    pygame.mixer.music.unpause()
                    self.bgm_paused = False
        # 畫漸暗
        if self.model.to_dark:
            self.view.draw_dark(self.model.value)




    @property
    def quit_game(self):
        return self.events["game quit"]

    @property
    def is_pause(self):
        return self.events["pause"]