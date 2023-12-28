import pygame
from setting import *
from object import *
import cv2
import numpy as np

# pygame.mixer.init()
# pygame.mixer.music.set_volume(0.2)



class GameView:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.font_size = 30
        self.font = pygame.font.Font("文鼎中特標準宋體.TTF", self.font_size)
        self.font_item = pygame.font.Font("文鼎中特毛楷.ttf", 24)
        self.font_name = pygame.font.Font("文鼎中特毛楷.ttf", 32)
        self.font_description = pygame.font.Font("文鼎中特毛楷.TTF", 19)
        self.font_dialog = pygame.font.Font("文鼎中特毛楷.TTF", 20)
        self.font_speaker = pygame.font.Font("文鼎中特毛楷.TTF", 24)
        self.font_tip = pygame.font.Font("文鼎中特毛楷.TTF", 16)
        self.bg = None
        self.black = pygame.transform.scale(pygame.image.load(f"image/black.png"), (GAME_WIDTH, GAME_HEIGHT))
        self.black_b = pygame.transform.scale(pygame.image.load(f"image/black.png"), (WIN_WIDTH, WIN_HEIGHT))
        self.transparency = 0
        # 對話框
        self.dialog_box_image = pygame.transform.scale(pygame.image.load(f"image/對話背景.png"), (GAME_WIDTH, GAME_HEIGHT))
        # 對話框說話者位置
        self.speaker_x = GAME_X + 20
        self.speaker_y = GAME_Y + GAME_HEIGHT - 70 - self.font_dialog.get_linesize() - 10
        # 對話框文字位置
        self.dialog_x = GAME_X + 50
        self.dialog_y = GAME_Y + GAME_HEIGHT - 25 - self.font_dialog.get_linesize() - 10
        # 調查畫面圖片框
        self.observe_rect = pygame.Rect(GAME_X + 25, GAME_Y + 25, GAME_WIDTH//2 - 50 , GAME_HEIGHT - 50)
        # 調查畫面文字起始點
        self.description_x = GAME_X + 0 + GAME_WIDTH//2
        self.description_y = GAME_Y + 100

        # 劇情對話框
        self.show_dialog_box_image = pygame.transform.scale(pygame.image.load(f"image/對話背景.png"),
                                                       (WIN_WIDTH, WIN_HEIGHT))
        # 劇情對話框說話者位置
        self.speaker_show_x = GAME_X + 20
        self.speaker_show_y = GAME_Y + GAME_HEIGHT - 70 - self.font_dialog.get_linesize()

        # 文字置中
        # WIN_WIDTH // 2 - word.get_width() // 2

    def draw_bg(self):
        self.win.blit(BACKGROUND_IMAGE, (0, 0))

    def draw_menu_button(self, btn):
        self.win.blit(btn.image, btn.rect)

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
        for item in investigation_item.object:
            if isinstance(item, TvShow):
                if item.ispower:
                    # 檢測是相片還是MP4
                    if isinstance(item.image, pygame.Surface):
                        self.win.blit(item.image, item.rect)
                    else:
                        ret, frame = item.image.read() #ret判斷結束了沒
                        if not ret:
                            item.image.set(cv2.CAP_PROP_POS_FRAMES, 0) # 結束將影片重製
                            # 當影片重製時，音樂也重新撥放
                            item.music.stop()
                            item.music.play()
                            # TODO :　解決重播會閃一下的問題
                            break

                        frame = cv2.resize(frame,(item.w,item.h)) #設定大小
                        frame = cv2.flip(frame, 1) # 做左右向反
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # 換成彩色
                        frame = pygame.surfarray.make_surface((np.rot90(frame)))  # 轉90度 畫在畫面上
                        self.win.blit(frame, (item.x, item.y)) #設定化的位置
                        pygame.time.delay(int(200 / (item.image.get(cv2.CAP_PROP_FPS)))) # 延遲畫面更新

        # 讓電視框可以遮住超出範圍的節目畫面
        self.win.blit(investigation_item.focus, (GAME_X, GAME_Y))
        for item in investigation_item.object:
            if isinstance(item, TvShow):
                if not item.ispower:
                    self.win.blit(item.power_off, item.rect)
            else:
                self.win.blit(item.image, item.rect)


    # TODO : 可以輸入文字位置
    def speak(self,text, pos):
        word = self.font.render(text, True, (255, 255, 255))  # 渲染文字
        self.win.blit(word, (WIN_WIDTH // 2 - word.get_width() // 2, WIN_HEIGHT // 2 - word.get_height() // 2))

    def murmur(self, show):
        # 畫背景
        if show.display is not None:
            self.win.blit(show.display, (GAME_X, GAME_Y))

        # 畫出對話框(灰色漸層)
        self.win.blit(self.dialog_box_image, (GAME_X, GAME_Y))

        # 說話者
        title = self.font_speaker.render(show.speaker[show.index], True, (255, 255, 255))  # 渲染文字
        self.win.blit(title, (self.speaker_x, self.speaker_y))
        # 內容
        word = self.font_dialog.render(show.cur_text, True, (255, 255, 255))  # 渲染文字
        self.win.blit(word, (self.dialog_x, self.dialog_y))

        # 操作說明
        tip = self.font_tip.render("點擊滑鼠以繼續...", True, (255, 255, 255))  # 渲染文字
        self.win.blit(tip, (GAME_X + GAME_WIDTH - tip.get_width() - 10, GAME_Y + GAME_HEIGHT - tip.get_height() - 10))

        # # 畫出對話框(灰色漸層)
        # self.win.blit(self.dialog_box_image, (GAME_X, GAME_Y))
        #
        # # 說話者
        # title = self.font_speaker.render(speaker, True, (255, 255, 255))  # 渲染文字
        # self.win.blit(title, (self.speaker_x, self.speaker_y))
        # # 內容
        # word = self.font_dialog.render(text, True, (255, 255, 255))  # 渲染文字
        # self.win.blit(word, (self.dialog_x, self.dialog_y))
        #
        # # 操作說明
        # tip = self.font_tip.render("點擊滑鼠以繼續...", True, (255, 255, 255))  # 渲染文字
        # self.win.blit(tip, (GAME_X + GAME_WIDTH - tip.get_width() - 10, GAME_Y + GAME_HEIGHT - tip.get_height() - 10))

    def draw_bag(self, bag):
        # 依照頁數輸出此頁的物品格
        for blank in bag.blank[6 * (bag.page - 1): 6 * bag.page]:
            if blank.item == bag.hold and blank.item != None:
                # 高亮物品格背景
                self.win.blit(blank.selected_image, blank.rect)
                # 顯示物品名稱
                word = self.font_item.render(blank.item.name, True, (255, 255, 255))
                rect = word.get_rect()
                rect.topright = (860, 80)
                self.win.blit(word, rect)

                # 操作說明
                tip = self.font_tip.render("點擊[F]以調查物品...", True, (255, 255, 255))  # 渲染文字
                self.win.blit(tip, (GAME_X + GAME_WIDTH - tip.get_width() - 10, GAME_Y + GAME_HEIGHT - tip.get_height() - 10))


            else:
                self.win.blit(blank.image, blank.rect)
            if blank.item != None:
                self.win.blit(blank.item.icon, (blank.x + ICON_POS, blank.y + ICON_POS))

    def draw_bag_page(self, bnt):
        self.win.blit(bnt.right_image, bnt.rect_r)
        self.win.blit(bnt.left_image, bnt.rect_l)
    def draw_observe(self, item):
        # 畫面灰化
        black_surface = self.black
        black_surface.set_alpha(150)
        self.win.blit(black_surface, (GAME_X, GAME_Y))

        # 顯示圖片
        scaled_image = self.scale_image_to_rect(item.observe, self.observe_rect)
        rect = scaled_image.get_rect()
        # 讓圖片中央的Y對其self.observe_rect 這樣不管圖片形狀 都會置中
        rect.midleft = self.observe_rect.midleft
        self.win.blit(scaled_image, rect.topleft)

        # 顯示文字
        text = item.description
        lines = text.splitlines()

        # 顯示物品名字
        name = self.font_name.render(item.name, True, (255, 255, 255))  # 渲染文字
        self.win.blit(name, (GAME_X + GAME_WIDTH//2 - name.get_width()//2, GAME_Y + 40))

        # 用於使文字框置中
        # y = WIN_HEIGHT // 2 - sum(self.font.get_linesize() for _ in lines) // 2

        # 使文字固定從這個 y 開始
        y = self.description_y

        for line in lines:
            word = self.font_description.render(line, True, (255, 255, 255))
            self.win.blit(word, (self.description_x, y))
            y += self.font_description.get_linesize() + 2 # 增加行距

        # 操作說明
        tip = self.font_tip.render("點擊[F]退出調查", True, (255, 255, 255))  # 渲染文字
        self.win.blit(tip, (GAME_X + (GAME_WIDTH - tip.get_width())//2, GAME_Y + GAME_HEIGHT - tip.get_height() - 10))

    def draw_show(self, show):
        # 畫背景
        if show.display is not None:
            self.win.blit(show.display,(0,0))


        # 畫出對話框(灰色漸層)
        self.win.blit(self.show_dialog_box_image, (0, 0))

        # 說話者
        title = self.font_speaker.render(show.speaker[show.index], True, (255, 255, 255))  # 渲染文字
        self.win.blit(title, (self.speaker_x, self.speaker_y))
        # 內容
        word = self.font_dialog.render(show.cur_text, True, (255, 255, 255))  # 渲染文字
        self.win.blit(word, (self.dialog_x, self.dialog_y))

        # 操作說明
        tip = self.font_tip.render("點擊滑鼠以繼續...", True, (255, 255, 255))  # 渲染文字
        self.win.blit(tip, (WIN_WIDTH - tip.get_width() - 30, WIN_HEIGHT - tip.get_height() - 30))



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

    def draw_opening(self,opening,value):
        # 畫背景
        self.win.blit(opening.image, (0, 0))
        black_surface = self.black_b
        black_surface.set_alpha(value)
        self.win.blit(black_surface, (0, 0))

    # 聲音部分
    # 背景聲音
    def pause_bg(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
    def unpause_bg(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.unpause()



