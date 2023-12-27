from setting import *
# 文本

# 圖片
image_1 = pygame.transform.scale(pygame.image.load(f"image/black.png"), (WIN_WIDTH, WIN_HEIGHT))
image_2 = pygame.transform.scale(pygame.image.load(f"image/study/BookShelf/book_shelf.png"), (WIN_WIDTH, WIN_HEIGHT))
image_3 = pygame.transform.scale(pygame.image.load(f"image/study/BookShelf/book_shelf_investigation.png"), (WIN_WIDTH, WIN_HEIGHT))

#開場
CH1_START_TEXT = ["本故事人物及故事純屬虛構","(喘氣聲)\n...\n這棟房子...\n門牌還勉強判讀，XX里10-1號...\n終於來到這裡了...\n從出發到現在也4天了...\n希望能夠找到\n希望能夠..."]
CH1_START_SPEAKER = ["開發者","???"]
CH1_START_IMAGE = [(image_1,0)]

# 章節1結尾 (當你拚完照片)
CH1_END_TEXT = ["Demo版本到此結束\nDemo版本到此結束\n感謝您的遊玩\n在遊戲過程如果遇到bug或是問題\n歡迎聯絡/通知我\ngithub:https://github.com/hankTaro/room-escape-game"]
CH1_END_SPEAKER = ["開發者"]
CH1_END_IMAGE = [(image_1,0)]

# 章節2開場 (男人自言自語到小孩寫作業鉛筆斷掉)
CH2_START_TEXT = ["15 X 24 = ...\n(啪)\n阿!糟糕鉛筆斷掉了\n不知道削鉛筆機在哪裡...\n去找找吧!"]
CH2_START_SPEAKER = ["小男孩"]
CH2_START_IMAGE = [(image_1,0)]

# 章節3開場 (結局連續動畫)
CH3_START_TEXT = ["媽媽我回來了","阿你去爺爺家寫作業喔","對阿，我寫完了","阿你明天上學的東西準備好了嗎，不要明天又要我送東西過去",
                  "我準備好了啦，我好累喔，我要去睡覺了","外頭風吹動樹葉的沙沙聲和家中母親走動的腳步聲使你慢慢進入夢鄉",
                  ".\n..\n...", # index = 6
                  "...","...","...", # index = 7 8 9 播放地震 尖叫 倒塌音效
                  ".\n..\n...\n"
                  "胸口傳來強烈的壓迫感讓你呼吸變得困難\n"
                  "同時麻木的灼燒感也在手腳蔓延\n"
                  "你睜開眼睛，空氣中瀰漫著塵土以及磚瓦碎屑\n"
                  "睡前為你遮風擋雨的屋頂現在卻裂成了塊狀將你掩埋\n"
                  "只有些許的月光從碎片縫隙打進來...", # index = 10
                  "XX里廣播\nXX里廣播\n現在正發生強烈地震\n請里民盡速前往XX小學的操場避難", # index = 11
                  ".\n..\n...\n", # index = 12
                  "小心你上面!!!",".\n..\n...\n",
                  "哇阿阿!!我的腿...我的腿!!!",".\n..\n...\n",
                  "我的小孩還在裡面阿阿!!!",".\n..\n...\n",
                  "救救我...\n我...在\n我...在這...這裡", # index = 19
                  "你嘗試大聲呼救，但光是呼吸就讓你用盡全力\n那份沉重剝奪了你發聲的能力，每一次的嘗試都只能得到微弱而短促的迴響\n隨著時間的流逝，你的意識也越來越模糊..."]

CH3_START_SPEAKER = ["小男孩","媽媽","小男孩","媽媽","小男孩","旁白","",
                     "","","", # index = 7 8 9 播放音效
                      "旁白","廣播","", # index = 12
                     "年輕男人的聲音","",
                     "老人的聲音","",
                     "女人的聲音","",
                     "小男孩", # index = 19
                     "旁白"]
CH3_START_IMAGE = [(image_1,0)]