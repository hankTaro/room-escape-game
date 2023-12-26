from setting import *
# 文本

# 圖片
image_1 = pygame.transform.scale(pygame.image.load(f"image/study/BookShelf/book_shelf_investigation.png"), (WIN_WIDTH, WIN_HEIGHT))
image_2 = pygame.transform.scale(pygame.image.load(f"image/study/BookShelf/book_shelf.png"), (WIN_WIDTH, WIN_HEIGHT))
image_3 = pygame.transform.scale(pygame.image.load(f"image/study/BookShelf/book_shelf_investigation.png"), (WIN_WIDTH, WIN_HEIGHT))

#開場
CH1_START_TEXT = ["test1\ntest2\ntest3","test1\ntest2\ntest3","test1\ntest2\ntest3","test1\ntest2\ntest3","test1\ntest2\ntest3"]
CH1_START_SPEAKER = ["A","B","C","D","E"]
CH1_START_IMAGE = [(image_1,0),(image_2,2),(image_3,4)]

# 章節2開場 (當你拚完照片)
CH2_START_TEXT = ["test1\ntest2\ntest3","test1\ntest2\ntest3","test1\ntest2\ntest3","test1\ntest2\ntest3","test1\ntest2\ntest3"]
CH2_START_SPEAKER = ["A","B","C","D","E"]
CH2_START_IMAGE = [(image_1,0),(image_2,2),(image_3,4)]