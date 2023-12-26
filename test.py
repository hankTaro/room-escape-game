

a = "111\n2\n3"
# b = len(a.splitlines())
print(a.splitlines()[0])
# 測試對話功能
import pygame
import time
from setting import *

FPS = 60
RED = '#FF0000'
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 200, 200)

# initialization
pygame.init()

# 視窗標題
pygame.display.set_caption("My Game")

class Game:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.font_size = 30
        self.font = pygame.font.Font("文鼎中特標準宋體.TTF", self.font_size)
        self.font_item = pygame.font.Font("金梅書法豆豆字體.ttf", 24)
        self.font_description = pygame.font.Font("文鼎中特毛楷.TTF", 20)
        self.font_dialog = pygame.font.Font("文鼎中特毛楷.TTF", 24)
        self.font_speaker = pygame.font.Font("文鼎中特毛楷.TTF", 24)
        self.font_tip = pygame.font.Font("文鼎中特毛楷.TTF", 16)
        self.bg = None
        self.black = pygame.transform.scale(pygame.image.load(f"image/black.png"), (GAME_WIDTH, GAME_HEIGHT))
        self.transparency = 0
        # 對話框
        self.dialog_box_image = pygame.transform.scale(pygame.image.load(f"image/對話背景.png"), (GAME_WIDTH, GAME_HEIGHT))
        # 對話框說話者位置
        self.speaker_x = GAME_X + 20
        self.speaker_y = GAME_Y + GAME_HEIGHT - 70 - self.font_dialog.get_linesize()
        # 對話框文字位置
        self.dialog_x = GAME_X + 50
        self.dialog_y = GAME_Y + GAME_HEIGHT - 25 - self.font_dialog.get_linesize()
        # 調查畫面圖片框
        self.observe_rect = pygame.Rect(GAME_X + 25, GAME_Y + 25, GAME_WIDTH//2 - 50 , GAME_HEIGHT - 50)
        # 調查畫面文字起始點
        self.description_x = GAME_X + 0 + GAME_WIDTH//2
        self.description_y = GAME_Y + 100

        self.speaker = ["Tom","Tom2","John","John2"]
        self.images = [(BLACK,2),(WHITE,3)]
        self.text = ["111111111\n????\n######","22222222222","0000000000", "!!!!!!!!\n#####"]
        # 目前人物說的話
        self.disp_text = ""
        # 第幾位人物
        self.index = 0
        # 人物台詞第幾句
        self.dialog_index = 0
        # 目前背景
        self.images_index = 0
        # 該更換背景的時機
        self.images_change_index = self.images[self.images_index][1]
        # 人物所有台詞分據
        self.text_lines = self.text[self.index].splitlines()

    # draw background
    def draw_bg(self, surf):
        pygame.draw.rect(surf, BLACK, [0, 0, WIN_WIDTH, WIN_HEIGHT], 0)

    
    def murmur(self, speaker, text, image):
        #畫畫面
        pygame.draw.rect(self.win, image, [0, 0, WIN_WIDTH, WIN_HEIGHT], 0)

        # 畫出對話框(灰色漸層)
        self.win.blit(self.dialog_box_image, (GAME_X, GAME_Y))

        # 說話者
        title = self.font_speaker.render(speaker, True, (255, 255, 255))  # 渲染文字
        self.win.blit(title, (self.speaker_x, self.speaker_y))
        # 內容
        word = self.font_dialog.render(text, True, (255, 255, 255))  # 渲染文字
        self.win.blit(word, (self.dialog_x, self.dialog_y))

        # 操作說明
        tip = self.font_tip.render("點擊滑鼠以繼續...", True, (255, 255, 255))  # 渲染文字
        self.win.blit(tip, (GAME_X + GAME_WIDTH - tip.get_width() - 10, GAME_Y + GAME_HEIGHT - tip.get_height() - 10)) 

    # 更新顯示文字
    def update(self):
        if self.text_lines:
            if len(self.disp_text) < len(self.text_lines[self.dialog_index]):
                self.disp_text = self.text_lines[self.dialog_index][:len(self.disp_text)+1]
            self.murmur(self.speaker[self.index], self.disp_text, self.images[self.images_index][0])


    def game_run(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            # define FPS
            clock.tick(FPS)
            self.draw_bg(self.win)

            # press x to quit the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.dialog_index += 1
                    self.disp_text = ""
                    if self.dialog_index == len(self.text_lines):
                        self.dialog_index = 0
                        self.index += 1
                        if self.index == len(self.speaker):
                            self.index = 0
                            self.images_index = 0
                        self.text_lines = self.text[self.index].splitlines()
                        if self.index == self.images_change_index:
                            self.images_index += 1


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.text_lines = ""
                        self.disp_text = ""
                        print("quite")

            self.update()
            # update the window
            pygame.display.update()
        pygame.quit()


if __name__ == "__main__":
    start_time = time.time()
    game = Game()
    game.game_run()
        