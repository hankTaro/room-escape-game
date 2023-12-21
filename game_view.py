import pygame
from setting import *
from object import *
import cv2
import numpy as np

class GameView:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.font_size = 30
        self.font = pygame.font.Font("文鼎中特標準宋體.TTF", self.font_size)
        self.font_item = pygame.font.Font("金梅書法豆豆字體.ttf", 24)
        self.font_description = pygame.font.Font("文鼎中特毛楷.TTF", 24)
        self.bg = None
        self.black = pygame.transform.scale(pygame.image.load(f"image/black.png"), (GAME_WIDTH, GAME_HEIGHT))
        self.transparency = 0
        # 調查畫面圖片框
        self.observe_rect = pygame.Rect(GAME_X + 25, GAME_Y + 25, GAME_WIDTH//2 - 50 , GAME_HEIGHT//2 - 50)
        # 調查畫面文字起始點
        self.description_x = GAME_X + 25 + GAME_WIDTH//2
        self.description_y = GAME_Y + 25

    def draw_bg(self):
        self.win.blit(BACKGROUND_IMAGE, (0, 0))

    # TODO : 畫出不同房間與牆面的布局 裏頭要有個判別式 以便選擇背景
    # 依照 room 中的 layout data 將物品畫出
    def draw_room(self, room,wall):
        self.win.blit(room.bg_image[wall-1], (GAME_X, GAME_Y))
        for item in room.wall[str(wall)].object:
            self.win.blit(item.image, item.rect)
    # TODO : 畫出調查物件的畫面
    def draw_item(self, investigation_item):
        self.win.blit(investigation_item.focus, (GAME_X, GAME_Y))
        for item in investigation_item.object:
            self.win.blit(item.image, item.rect)

    def draw_tv_item(self, investigation_item):
        self.win.blit(investigation_item.focus, (GAME_X, GAME_Y))
        for item in investigation_item.object:
            if isinstance(item, TvShow):
                if item.ispower:
                    ret, frame = item.image.read() #ret判斷結束了沒
                    if not ret:
                        item.image.set(cv2.CAP_PROP_POS_FRAMES, 0) # 結束將影片重製
                        return
                    frame = cv2.resize(frame,(item.w,item.h)) #設定大小
                    frame = cv2.flip(frame, 1) # 做左右向反
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # 換成彩色
                    frame = pygame.surfarray.make_surface((np.rot90(frame)))  # 轉90度 畫在畫面上
                    self.win.blit(frame, (item.x, item.y)) #設定化的位置
                else:
                    self.win.blit(item.power_off, item.rect)
            else:
                self.win.blit(item.image, item.rect)

    # TODO : 可以輸入文字位置
    def speak(self,text, pos):
        word = self.font.render(text, True, (255, 255, 255))  # 渲染文字
        self.win.blit(word, (WIN_WIDTH // 2 - word.get_width() // 2, WIN_HEIGHT // 2 - word.get_height() // 2))

    def draw_bag(self, bag):
        # self.win.blit(bag.image, (bag.x, bag.y))
        for blank in bag.blank:
            if blank.item == bag.hold and blank.item != None:
                self.win.blit(blank.selected_image, blank.rect)
                word = self.font_item.render(blank.item.name, True, (255, 255, 255))
                rect = word.get_rect()
                rect.topright = (860, 80)
                self.win.blit(word, rect)
            else:
                self.win.blit(blank.image, blank.rect)
            if blank.item != None:
                self.win.blit(blank.item.icon, (blank.x + ICON_POS, blank.y + ICON_POS))
    def draw_observe(self, item):
        # 畫面灰化
        black_surface = self.black
        black_surface.set_alpha(150)
        self.win.blit(black_surface, (GAME_X, GAME_Y))

        # 顯示圖片
        scaled_image = self.scale_image_to_rect(item.observe, self.observe_rect)
        self.win.blit(scaled_image, self.observe_rect.midleft)

        # 顯示文字
        text = item.description
        lines = text.splitlines()

        y = WIN_HEIGHT // 2 - sum(self.font.get_linesize() for _ in lines) // 2

        for line in lines:
            word = self.font_description.render(line, True, (255, 255, 255))
            self.win.blit(word, (WIN_WIDTH // 2 - word.get_width() // 2, y))
            y += self.font_description.get_linesize()



    def scale_image_to_rect(self, image, rect):
        # 等比縮放圖片至符合方形
        aspect_ratio = image.get_width() / image.get_height()
        target_width = rect.width
        target_height = int(target_width / aspect_ratio)
        scaled_image = pygame.transform.scale(image, (target_width, target_height))
        return scaled_image



    def fade_out(self,transparency):
        black_surface = self.black
        black_surface.set_alpha(transparency)
        self.win.blit(black_surface, (GAME_X, GAME_Y))
        if transparency <= 0:
            return 'end'
        else:
            return 0

