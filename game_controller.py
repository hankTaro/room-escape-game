import pygame
from object import *

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
        # update event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.events["game quit"] = True
            # player press action
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # 叫出選單
                    self.events["keyboard key"] = pygame.K_ESCAPE
                elif event.key == pygame.K_f:
                    # 調查手中物件
                    self.events["keyboard key"] = pygame.K_f
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
        # render background
        self.view.draw_bg()


        # TODO : 各房間的場景切換
        if not self.model.investigation:
            self.view.draw_room(self.model.cur_room, self.model.wall)
        else:
            if isinstance(self.model.investigation_item, Tv):
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

        # 劃出對話框 (依照位置)
        if self.model.text != "":
            self.view.speak(self.model.text, self.model.text_pos)

        # 劃出對話框(下方固定位置)
        if self.model.dialog != "":
            self.view.murmur(self.model.speaker, self.model.dialog.splitlines()[self.model.dialog_index], self.model.dialog_index)

        # 畫出手中物品調查頁面
        if self.model.observe:
            self.view.draw_observe(self.model.bag.hold)




    @property
    def quit_game(self):
        return self.events["game quit"]

    @property
    def is_pause(self):
        return self.events["pause"]