import pygame
from setting import *


class GameView:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.font_size = 30
        self.font = pygame.font.Font("文鼎中特標準宋體.TTF", self.font_size)
        self.bg = None
        self.black = pygame.transform.scale(pygame.image.load(f"image/black.png"), (GAME_WIDTH, GAME_HEIGHT))
        self.transparency = 0

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

    # TODO : 可以輸入文字位置
    def speak(self,text, pos):
        word = self.font.render(text, True, (255, 255, 255))  # 渲染文字
        self.win.blit(word, (WIN_WIDTH // 2 - word.get_width() // 2, WIN_HEIGHT // 2 - word.get_height() // 2))

    def draw_bag(self, bag):
        # self.win.blit(bag.image, (bag.x, bag.y))
        for blank in bag.blank:
            if blank.item == bag.hold and blank.item != None:
                self.win.blit(blank.selected_image, blank.rect)
            else:
                self.win.blit(blank.image, blank.rect)
            if blank.item != None:
                self.win.blit(blank.item.icon, (blank.x + ICON_POS, blank.y + ICON_POS))

    # def fade_in(self):
    #     # 定義截圖區域的矩形範圍 (x, y, width, height)
    #     capture_rect = pygame.Rect(GAME_X, GAME_Y, GAME_WIDTH, GAME_HEIGHT)
    #
    #     # 使用 subsurface() 創建限定範圍的子表面
    #     cropped_surface = self.win.subsurface(capture_rect)
    #
    #     # 將子表面的像素數據轉換為字串
    #     screenshot_data = pygame.image.tostring(cropped_surface, 'RGB')
    #
    #     # 創建新的 Surface
    #     new_surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
    #
    #     # 將 screenshot_data 轉換為 Surface
    #     pygame.image.fromstring(screenshot_data, (GAME_WIDTH, GAME_HEIGHT), 'RGB').convert(new_surface)
    #
    #     transparency = 0
    #
    #     black_surface = self.black
    #     if transparency < 255:
    #         transparency += 1
    #         if transparency >= 255:
    #             transparency = 255
    #         black_surface.set_alpha(transparency)
    #         self.win.blit(new_surface, (GAME_X, GAME_Y))
    #         self.win.blit(black_surface, (0, 0))

    def fade_out(self,transparency):
        black_surface = self.black
        black_surface.set_alpha(transparency)
        self.win.blit(black_surface, (GAME_X, GAME_Y))
        if transparency <= 0:
            return 'end'
        else:
            return 0

