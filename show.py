from setting import *


# 現在可以讓傳入的 images,sounds = None 以利物件敘述做使用
class Show:
    def __init__(self,text,speaker,images,sounds,bgm): # sounds = [(sound_1, 1), (sound_2, 2)]  images = [(BLACK, 0), (WHITE, 3)]
        self.speaker = speaker  # ["Tom", "Tom2", "John", "John2"]
        self.images = []  # [BLACK, WHITE]
        self.sounds = []  # [sound_1,sound_2]
        self.text = text  # ["111111111\n????\n######", "22222222222", "0000000000", "!!!!!!!!\n#####"]
        self.images_check =[] #[0,3]
        self.sounds_check = [] #[1,2]
        self.bgm = bgm
        self.first_time = True
        if images is not None:
            for a,b  in images:
                self.images.append(a)
                self.images_check.append(b)
        if sounds is not None:
            for a,b  in sounds:
                self.sounds.append(a)
                self.sounds_check.append(b)

        # 永遠達不到的條件 防止存取錯誤
        self.images_check.append(99999999)
        self.sounds_check.append(99999999)

        # 文字index
        self.index = 0
        # 在一段台詞中的第幾句
        self.dialog_index = 0
        # 目前背景index
        self.image_check_index = 0
        # 目前音效index
        self.sound_check_index = 0
        # 人物當前所有台詞
        self.text_lines = self.text[self.index].splitlines()

        # 目前人物說的話
        self.cur_text = self.text_lines[self.dialog_index]
        # 當前在播放的音效
        self.playing = None
        # 當前顯示的圖片
        self.display = None



    def __del__(self):
        # 執行清理工作
        pass

    def start(self):
        if self.first_time:
            self.first_time = False
            # 如果一進入show就有音效要播放 則先播出來 然後  self.sound_check_index +=1
            if self.sounds_check[0] == 0:
                self.playing = self.sounds[self.sound_check_index]
                self.playing.play()
                self.sound_check_index += 1


            # 如果一進入show就有圖片要顯示 則先顯示出來 然後  self.image_check_index +=1
            if self.images_check[0] == 0:
                self.display = self.images[self.image_check_index]
                self.image_check_index += 1

            # 播放bgm
            if self.bgm is not None:
                self.bgm.play(-1)
                self.bgm_play = True

    def next(self):
        # 等待音效播完
        # if self.playing is not None:
        #     pygame.time.delay(int(self.playing.get_length() * 1000))
        #     self.playing = None

        # 檢查一段台詞是否已經到了最後一句
        if self.dialog_index == len(self.text_lines) - 1:
            self.index += 1
            # 檢查self.index 是否超過現有台詞的數量 為Ture 就結束動畫
            if self.index == len(self.text):
                if self.playing is not None:
                    # 停止當前音效
                    self.playing.stop()
                if self.bgm is not None:
                    # 停止BGM
                    self.bgm.stop()
                # 將內部數值初始化
                self.index = 0
                self.dialog_index = 0
                self.image_check_index = 0
                self.sound_check_index = 0
                # 目前人物說的話
                self.cur_text = self.text_lines[self.dialog_index]
                # 當前在播放的音效
                self.playing = None
                # 當前顯示的圖片
                self.display = None
                self.first_time = True
                return 'end'
            # 初始化
            self.dialog_index = 0
            self.text_lines = self.text[self.index].splitlines()
            self.cur_text = self.text_lines[self.dialog_index]
            # 檢查畫面是否要變動
            if self.index == self.images_check[self.image_check_index]: # 確認是否要切到下個
                self.display = self.images[self.image_check_index]
                self.image_check_index += 1
                # 檢查音樂是否要變動
            if self.index == self.sounds_check[self.sound_check_index]:  # 確認是否要切到下個
                # 先停止先前沒播完的聲音
                if self.playing is not None:
                    self.playing.stop()
                # 在切換當前要播放的音效
                self.playing = self.sounds[self.sound_check_index]
                if self.playing is not None:
                    self.playing.play()
                self.sound_check_index += 1



        else:
            self.dialog_index += 1
            self.cur_text = self.text_lines[self.dialog_index]
            return 'continue'

# class Dialog:
#     def __init__(self,text,speaker,sounds):
#         self.speaker = speaker  # ["Tom", "Tom2", "John", "John2"]
#         self.sounds = []  # [(sound_1, 0), (sound_2, 3)]
#         self.text = text  # ["111111111\n????\n######", "22222222222", "0000000000", "!!!!!!!!\n#####"]
#         self.sounds_check =[]
#         for a,b  in sounds:
#             self.sounds.append(a)
#             self.sounds_check.append(b)
#
#         # 永遠達不到的條件 防止存取錯誤
#         self.sounds_check.append(99999999)
#
#         # 文字index
#         self.index = 0
#         # 在一段台詞中的第幾句
#         self.dialog_index = 0
#         # 目前音效index
#         self.check_index = 0
#         # 人物當前所有台詞
#         self.text_lines = self.text[self.index].splitlines()
#
#         # 目前人物說的話
#         self.cur_text = self.text_lines[self.dialog_index]
#
#     def __del__(self):
#         # 執行清理工作
#         pass
#
#     def next(self):
#         # 檢查一段台詞是否已經到了最後一句
#         if self.dialog_index == len(self.text_lines) - 1:
#             self.index += 1
#             # 檢查self.index 是否超過現有台詞的數量 為Ture 就結束動畫
#             if self.index == len(self.text):
#                 return 'end'
#             # 初始化
#             self.dialog_index = 0
#             self.text_lines = self.text[self.index].splitlines()
#             self.cur_text = self.text_lines[self.dialog_index]
#             # 檢查音樂是否要變動
#             if self.index == self.sounds_check[self.check_index + 1]: # 確認是否要切到下個
#                 self.check_index += 1
#
#         else:
#             self.dialog_index += 1
#             self.cur_text = self.text_lines[self.dialog_index]
#             return 'continue'