import pygame
from setting import *


class GameView:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.font_size = 30
        self.font = pygame.font.Font("New-Super-Mario-Font-U-1.ttf", self.font_size)
        self.bg = None

    def draw_bg(self):
        self.win.blit(BACKGROUND_IMAGE, (0, 0))

    # TODO : 畫出不同房間與牆面的布局 裏頭要有個判別式 以便選擇背景
    # 依照 room 中的 layout data 將物品畫出
    def draw_living_room(self, room,wall):
        self.win.blit(room.bg_image, (50, 50))
        for item in room.wall[str(wall)].object:
            self.win.blit(item.image, item.rect)
        pass
    # def draw_living_room_2(self):
    #     pass
    # def draw_living_room_3(self):
    #     pass
    # def draw_living_room_4(self):
    #     pass
    def draw_study_1(self):
        pass
    def draw_study_2(self):
        pass
    def draw_study_3(self):
        pass
    def draw_study_4(self):
        pass
    def draw_newspaper(self):
        pass