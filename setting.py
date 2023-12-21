import pygame
import os

# game window
WIN_WIDTH = 1024
WIN_HEIGHT = 600

# 解謎視窗大小
# TODO : 大小待訂
GAME_WIDTH = 820 # WIN_WIDTH * 0.8
GAME_HEIGHT = 480  # WIN_HEIGHT * 0.8

# 解謎視窗對準點
GAME_X = 50
GAME_Y = 50

# 物品欄大小(ICON可能就-5)
BLANK_SIZE = 70
ICON_SIZE = 50

# ICON 座標
ICON_POS = (BLANK_SIZE - ICON_SIZE) // 2


# Frame Per Second
FPS = 60

# base
BASE = pygame.Rect(740, 30, 270, 100)
BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("image", "black.png")), (1024, 600))
VIDEO_EVENT = pygame.USEREVENT + 1

# 關卡布局
