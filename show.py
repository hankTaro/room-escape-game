from setting import *

class Show:
    def __init__(self,text,speaker,images):
        self.speaker = speaker  # ["Tom", "Tom2", "John", "John2"]
        self.images = []  # [(BLACK, 0), (WHITE, 3)]
        self.text = text  # ["111111111\n????\n######", "22222222222", "0000000000", "!!!!!!!!\n#####"]
        self.images_check =[]
        for a,b  in images:
            self.images.append(a)
            self.images_check.append(b)

        # 永遠達不到的條件 防止存取錯誤
        self.images_check.append(99999999)

        # 文字index
        self.index = 0
        # 在一段台詞中的第幾句
        self.dialog_index = 0
        # 目前背景index
        self.check_index = 0
        # 人物當前所有台詞
        self.text_lines = self.text[self.index].splitlines()

        # 目前人物說的話
        self.cur_text = self.text_lines[self.dialog_index]

    def __del__(self):
        # 執行清理工作
        pass

    def next(self):
        # 檢查一段台詞是否已經到了最後一句
        if self.dialog_index == len(self.text_lines) - 1:
            self.index += 1
            # 檢查self.index 是否超過現有台詞的數量 為Ture 就結束動畫
            if self.index == len(self.text):
                return 'end'
            # 初始化
            self.dialog_index = 0
            self.text_lines = self.text[self.index].splitlines()
            self.cur_text = self.text_lines[self.dialog_index]
            # 檢查畫面是否要變動
            if self.index == self.images_check[self.check_index + 1]: # 確認是否要切到下個
                self.check_index += 1

        else:
            self.dialog_index += 1
            self.cur_text = self.text_lines[self.dialog_index]
            print(self.dialog_index)
            return 'continue'