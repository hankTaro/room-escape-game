import pygame
import os
from setting import *

# pygame.mixer.init()
# pygame.mixer.music.set_volume(0.2)

# 文本

# 圖片
image_1 = pygame.transform.scale(pygame.image.load(f"image/black.png"), (WIN_WIDTH, WIN_HEIGHT))
image_2 = pygame.transform.scale(pygame.image.load(f"image/study/BookShelf/book_shelf.png"), (WIN_WIDTH, WIN_HEIGHT))
image_3 = pygame.transform.scale(pygame.image.load(f"image/study/BookShelf/book_shelf_investigation.png"), (WIN_WIDTH, WIN_HEIGHT))

# 聲音
mute = None
clicked_sound = pygame.mixer.Sound('music/clicked.wav')
rock_sound = pygame.mixer.Sound('music/rock.wav')
step_on_grass =  pygame.mixer.Sound('music/踏草地聲.mp3')
step_on_grass_and_breath =  pygame.mixer.Sound('music/草地加喘氣.mp3')
door_open_sound = pygame.mixer.Sound('music/door_open.wav')
wind_blow_leaf_sound = pygame.mixer.Sound('music/wind_blow_leaf.mp3')
fall_down_sound = pygame.mixer.Sound('music/fall_down.mp3')
fall_down_sound.set_volume(0.3)
screaming_sound = pygame.mixer.Sound('music/Crowd panic sound effect.mp3')
screaming_sound.set_volume(0.2)
earthquake_sound = pygame.mixer.Sound('music/Earthquake Inside House Sound Effect (4K Subscribers Special).mp3')
earthquake_sound.set_volume(1)
earthquake_sound_mix = pygame.mixer.Sound('music/地震加尖叫.mp3')
kid_breath_sound = pygame.mixer.Sound('music/kid_breath.mp3')
kid_breath_long_sound = pygame.mixer.Sound('music/kid_breath_long.mp3')
announcement_sound = pygame.mixer.Sound('music/announcement_long.mp3')
electrocardiogram_sound = pygame.mixer.Sound('music/electrocardiogram_long.mp3')
# electrocardiogram_sound.set_volume(0.1)
time_travel_sound = pygame.mixer.Sound('music/time_travel.mp3')
hey_sound = pygame.mixer.Sound('music/hey.mp3')
cabinet_moving_sound = pygame.mixer.Sound('music/cabinet_moving.mp3')
key_give_sound = pygame.mixer.Sound('music/key_give.mp3')
key_unlock_sound = pygame.mixer.Sound('music/key_unlock.mp3')
kid_crying_sound = pygame.mixer.Sound('music/kid_crying2.mp3')
pencil_writing_sound = pygame.mixer.Sound('music/鉛筆寫字聲.mp3')
walking_sound = pygame.mixer.Sound('music/walking sound effect.mp3')
walking_fast_sound = pygame.mixer.Sound('music/walking sound effect_fast.mp3')
radio_sound = pygame.mixer.Sound('music/Radio Static - Sound Effect for editing.mp3')


# bgm
bird_and_bug = pygame.mixer.Sound('music/ch1_background.mp3')
bird_and_bug.set_volume(0.5)

#開場
CH1_START_TEXT = ["本故事及人物純屬虛構\n如有雷同純屬巧合"," ","...\n這棟房子...\n門牌還勉強判讀，XX里10-1號...\n終於來到這裡了...\n從出發到現在也4天了...\n希望能夠找到\n希望能夠..."," "]
CH1_START_SPEAKER = ["開發者"," ","???",""]
CH1_START_IMAGE = [(image_1,0)]
CH1_START_SOUND = [(step_on_grass_and_breath,1),(mute,2),(door_open_sound,3)]
CH1_START_BGM = bird_and_bug
# 那些音效要播完
CH1_START_SOUND_WAIT = [1]

CH1_START_SHOW = (CH1_START_TEXT,CH1_START_SPEAKER,CH1_START_IMAGE,CH1_START_SOUND,CH1_START_BGM,CH1_START_SOUND_WAIT)

# 章節1結尾 (當你拚完照片)
CH1_END_TEXT = ["...\n這個是..."]
CH1_END_SPEAKER = ["男子"]
CH1_END_IMAGE = None #[(image_1,0)]
CH1_END_SOUND = None #[(time_travel_sound,1)]
CH1_END_BGM = None

CH1_END_SHOW = (CH1_END_TEXT,CH1_END_SPEAKER,CH1_END_IMAGE,CH1_END_SOUND,CH1_END_BGM)

# 章節2開場 (男人自言自語到小孩寫作業鉛筆斷掉)
CH2_START_TEXT = ["15 X 24 = ...\n(啪)\n阿!糟糕鉛筆斷掉了\n不知道削鉛筆機在哪裡...\n去找找吧!"]
CH2_START_SPEAKER = ["小男孩"]
CH2_START_IMAGE = None
CH2_START_SOUND = [(pencil_writing_sound,0)]
CH2_START_BGM = None

CH2_START_SHOW = (CH2_START_TEXT,CH2_START_SPEAKER,CH2_START_IMAGE,CH2_START_SOUND,CH2_START_BGM)


# 章節2結尾 (男孩要離開爺爺家)
CH2_END_TEXT = ["等等","怎麼了","明天你生日記得過來爺爺這邊\n我準備了一連串的解謎來給你玩，看你能不能破關找到爺爺要給你了寶藏",
                " 寶藏是甚麼啊?","哈哈哈，現在說的話就不好玩了\n"
                "等你明天來，自然就會知道了",
                "然後這個鑰匙給你，收好別用丟了\n"
                "明天解謎你會用上這個鑰匙的，好了快回家吧",
                " "] # 走路聲

CH2_END_SPEAKER = ["爺爺","小男孩","爺爺","小男孩","爺爺","爺爺",""]
CH2_END_IMAGE = None
CH2_END_SOUND = [(walking_fast_sound,0),(key_give_sound,5),(walking_sound,6)]
CH2_END_BGM = None
CH2_END_SOUND_WAIT = [0,6]

CH2_END_SHOW = (CH2_END_TEXT,CH2_END_SPEAKER,CH2_END_IMAGE,CH2_END_SOUND,CH2_END_BGM,CH2_END_SOUND_WAIT)

# 章節3開場 (結局連續動畫)
CH3_START_TEXT = ["媽媽我回來了","阿你去爺爺家寫作業喔","對阿，我寫完了","阿你明天上學的東西準備好了嗎，不要明天又要我送東西過去",
                  "我準備好了啦，我好累喔，我要去睡覺了","外頭風吹動樹葉的沙沙聲和家中母親走動的腳步聲使你慢慢進入夢鄉",
                  "...", # index = 6
                  " ", # index = 7播放地震 尖叫 倒塌音效
                  "..."
                  "胸口傳來強烈的壓迫感讓你呼吸變得困難\n"
                  "同時麻木的灼燒感也在手腳蔓延\n"
                  "你睜開眼睛，空氣中瀰漫著塵土以及磚瓦碎屑\n"
                  "睡前為你遮風擋雨的屋頂現在卻裂成了塊狀將你掩埋\n"
                  "只有些許的月光從碎片縫隙打進來...", # index = 8
                  "XX里廣播，XX里廣播\n現在正發生強烈地震\n請里民盡速前往XX小學的操場避難", # index = 9
                  "...", # index = 10
                  "小心你上面!!!","...",
                  "哇阿阿!!我的腿...我的腿!!!","...",
                  "我的小孩還在裡面阿阿!!!","...",
                  "救救我...\n我...在\n我...在這...這裡", # index = 17
                  "你嘗試大聲呼救，但光是呼吸就讓你用盡全力\n那份沉重剝奪了你發聲的能力，每一次的嘗試都只能得到微弱而短促的迴響\n隨著時間的流逝，你的意識也越來越模糊...",
                  ".\n..\n...", #index = 19
                  "嘿!這裡還有生還者，快過來幫忙!!", # index = 20
                  "...","嘿 你會沒事的，撐下去", # index = 22
                  ".\n..\n...\n....\n.....\n......",
                  "此次地震造成嚴重破壞及大規模傷亡\n"
                  "災區範圍涵蓋多個城市和鄉村，其中以南投周邊地區災情最為嚴重，許多路段已無法通行\n"
                  "救援隊伍已進入災區展開搜救工作\n"
                  "消防隊、軍隊、救護隊伍和志願者正在積極的尋找被困人員以及救助傷者，並撤離災區居民\n"
                  "搜救行動仍在進行中，請各自發救援隊加入救災頻道，FM 144.28 ...", # index = 24
                  " " # index = 25
                  ]

CH3_START_SPEAKER = ["小男孩","媽媽","小男孩","媽媽","小男孩","旁白","",
                     "", # index = 7 播放音效
                      "旁白","廣播","", # index = 10
                     "年輕男人的聲音","",
                     "老人的聲音","",
                     "女人的聲音","",
                     "小男孩", # index = 17
                     "旁白","",
                     "年輕男人的聲音",# index = 20
                     "","年輕男人的聲音",# index = 22
                     "","廣播",
                     "" #index = 25 穿越 黑畫面
                     ]
CH3_START_IMAGE = [(image_1,0)]
CH3_START_SOUND = [(door_open_sound,0),(wind_blow_leaf_sound,5),(earthquake_sound,7),(announcement_sound,9),
                   (screaming_sound,11),(kid_breath_long_sound,17),(hey_sound,20),(rock_sound,21),(electrocardiogram_sound,22),(radio_sound,24),(time_travel_sound,25)]
# 那些音效要播完
CH3_START_SOUND_WAIT = [0,7,21,25]
CH3_START_BGM = None

CH3_START_SHOW = (CH3_START_TEXT,CH3_START_SPEAKER,CH3_START_IMAGE,CH3_START_SOUND,CH3_START_BGM,CH3_START_SOUND_WAIT)

# 章節3結尾 - 1
CH3_END_TEXT = ["那真是如同煉獄般的一天...",
                "你將拚好的相片翻面\n上頭寫著:「寶藏就在我們一起做的櫃子後面」\n「By 永遠愛你的爺爺」",
                "我們...一起做的櫃子..."]
CH3_END_SPEAKER = ["男子","旁白","男子"]
CH3_END_IMAGE = None #[(image_1,0)]
CH3_END_SOUND = None #[(cabinet_moving_sound,4)]
CH3_END_BGM = None
CH3_END_SHOW = (CH3_END_TEXT,CH3_END_SPEAKER,CH3_END_IMAGE,CH3_END_SOUND,CH3_END_BGM)

# 章節3結尾 - 2
CH3_2_END_TEXT = ["你靠近地球儀下方的櫃子，看著上方粗糙的手藝...\n你抵住櫃子的底部，施力將櫃子推開...",
                " ",# index = 1
                "這個櫃子被你推開後，你發現後面牆壁竟然有個空間..." 
                "你往裡頭探去，發現了個金屬盒子\n"
                "你將箱子取出，這是一個像是工具箱的金屬盒子，扣具上頭有個鎖孔\n"
                "你將你帶來的鑰匙插進鎖孔...\n"
                "鑰匙輕易地滑了進去，大小十分契合\n"
                "你將鑰匙緩慢旋轉....", # index = 2
                " ", # index = 3 開鎖
                "扣具的鎖被你解開了\n"
                "你將蓋子打開，看見盒子裡頭放著整套木工工具、一個獅子木雕以及一張卡片\n卡片上寫著:", # index = 4
                "恭喜你破解了重重謎題，這套木工工具是送給你的生日禮物\n"
                "這樣你以後就可以和我一同做工而不必搶工具了\n"
                "另外這個木雕獅子，是作為保護和祈福的象徵，祝福你能平平安安的長大", # index = 5
                "在閱讀卡片的時候，你發覺你的視線逐漸模糊，卡片上的字也被滴落的水珠緩緩暈開...", # index = 6
                ".\n..\n...\n"
                "謝謝你...爺爺\n我很喜歡...\n然後...\n雖然已經過了10年...\n但是...我來探望你了" # index = 7
                ]
CH3_2_END_SPEAKER = ["旁白","", # index = 1
                     "旁白","", # index = 3
                     "旁白","卡片", # index = 5
                     "旁白","男子"]
CH3_2_END_IMAGE = None #[(image_1,0)]
CH3_2_END_SOUND = [(cabinet_moving_sound,1),(key_unlock_sound,3)]
CH3_2_END_BGM = None
CH3_2_END_SHOW = (CH3_2_END_TEXT,CH3_2_END_SPEAKER,CH3_2_END_IMAGE,CH3_2_END_SOUND,CH3_2_END_BGM)