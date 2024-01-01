import pygame
from pygame.locals import *

pygame.init()

# 創建一個窗口
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('英文按鍵檢測')

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # 獲取當前按鍵狀態
    keys = pygame.key.get_pressed()

    # 判斷特定英文按鍵是否被按下
    if keys[K_a]:
        print('按下了 A 鍵')

    if keys[K_b]:
        print('按下了 B 鍵')

    # 其他按鍵判斷...

    pygame.display.flip()

pygame.quit()