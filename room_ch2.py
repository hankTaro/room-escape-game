from wall import *
from object_ch2 import *
from show import *
from text import *

living_room_1_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/Wall/wall_1.png"), (GAME_WIDTH, GAME_HEIGHT))
living_room_2_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/Wall/wall_2.png"), (GAME_WIDTH, GAME_HEIGHT))
living_room_3_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/Wall/wall_3.png"), (GAME_WIDTH, GAME_HEIGHT))
living_room_4_image = pygame.transform.scale(pygame.image.load(f"image/Ch2/Wall/wall_4.png"), (GAME_WIDTH, GAME_HEIGHT))
bedroom_1_image = pygame.transform.scale(pygame.image.load(f"image/black.png"), (GAME_WIDTH, GAME_HEIGHT))
bedroom_2_image = pygame.transform.scale(pygame.image.load(f"image/black.png"), (GAME_WIDTH, GAME_HEIGHT))
bedroom_3_image = pygame.transform.scale(pygame.image.load(f"image/black.png"), (GAME_WIDTH, GAME_HEIGHT))
bedroom_4_image = pygame.transform.scale(pygame.image.load(f"image/black.png"), (GAME_WIDTH, GAME_HEIGHT))
study_1_image = pygame.transform.scale(pygame.image.load(f"image/study/Wall/study_1.png"), (GAME_WIDTH, GAME_HEIGHT))
study_2_image = pygame.transform.scale(pygame.image.load(f"image/study/Wall/study_2.png"), (GAME_WIDTH, GAME_HEIGHT))
study_3_image = pygame.transform.scale(pygame.image.load(f"image/study/Wall/study_3.png"), (GAME_WIDTH, GAME_HEIGHT))

# 章節1的所有房間/牆面
#yj
class LivingRoomCh2:
    def __init__(self):
        # data
        # 房間背景
        self.bg_image = [living_room_1_image, living_room_2_image, living_room_3_image, living_room_4_image]

        # 房間牆面數
        self.wall_size = 4

        # 切換畫面鍵
        self.right_button = RightButton(GAME_X + GAME_WIDTH + 20,WIN_HEIGHT/2) # RightButton(WIN_WIDTH - 50,WIN_HEIGHT/2)
        self.left_button = LeftButton(20,WIN_HEIGHT/2)

        # 物件
        # 起始畫面的書桌
        self.desk = DeskCh2(GAME_X, GAME_Y)

        # 用於判定的電視與大門
        self.tv = TvCh2(GAME_X, GAME_Y)
        self.exit_door = DoorToExitCh2(GAME_X, GAME_Y)

        # 劇情差異的臥室門
        self.bedroom_door = DoorToBedRoomCh2(GAME_X, GAME_Y)


        # 此房間在不同牆面有的物品/座標 (包括移動鍵)
        # 牆面1有這些東西
        self.__object_1 = [self.right_button,self.left_button,
                           self.exit_door,LivingRoomWindowCh2(GAME_X, GAME_Y),BoxCh2(GAME_X, GAME_Y)]
        # 牆面2有這些東西
        self.__object_2 = [self.right_button,self.left_button,
                           self.bedroom_door,ClockCh2(GAME_X, GAME_Y),BookShelfCh2(GAME_X, GAME_Y),Books(GAME_X, GAME_Y),Beer(GAME_X,GAME_Y)]
        # 牆面3有這些東西
        self.__object_3 = [self.right_button,self.left_button,DoorToKitchenCh2(GAME_X, GAME_Y),
                           self.tv,TvShelfCh2(GAME_X, GAME_Y), PaintingCh2(GAME_X, GAME_Y),GlobeCh2(GAME_X, GAME_Y),GlobeTableCh2(GAME_X, GAME_Y)]
        self.__object_4 = [self.right_button, self.left_button,
                           self.desk,TrashCanCh2(GAME_X, GAME_Y),CalendarCh2(GAME_X, GAME_Y),Newspaper(GAME_X, GAME_Y)]

        # 當前牆面/建立此房間的牆面
        # 不同房間的牆面數會不一樣 要注意
        self.wall = {'1': Wall(self.bg_image,self.__object_1),
                     '2': Wall(self.bg_image,self.__object_2),
                     '3': Wall(self.bg_image,self.__object_3),
                     '4': Wall(self.bg_image, self.__object_4)}