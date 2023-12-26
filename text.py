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

# 章節2開場 (當你拚完照片)
CH2_START_TEXT = ["Demo版本到此結束\nDemo版本到此結束\n感謝您的遊玩\n在遊戲過程如果遇到bug或是問題\n歡迎聯絡/通知我\ngithub:https://github.com/hankTaro/room-escape-game"]
CH2_START_SPEAKER = ["開發者"]
CH2_START_IMAGE = [(image_1,0)]