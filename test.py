import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Slow Fade Transition")

# 設定顏色和透明度
black = (0, 0, 0)
alpha = 0  # 初始透明度

# 創建全黑的 Surface
black_surface = pygame.Surface((width, height))
black_surface.fill(black)

clock = pygame.time.Clock()

running = True
fading_in = True  # 起始狀態是淡入

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # 填充白色背景

    # 根據淡入淡出的狀態更新透明度
    if fading_in:
        alpha += 10  # 較慢的透明度增加速度
        if alpha >= 255:
            alpha = 255
            fading_in = False  # 開始淡出
    else:
        alpha -= 10  # 較慢的透明度減少速度
        if alpha <= 0:
            alpha = 0
            fading_in = True  # 開始淡入

    # 設定透明度並繪製全黑 Surface
    black_surface.set_alpha(alpha)
    screen.blit(black_surface, (0, 0))

    pygame.display.flip()
    clock.tick(60)  # 較低的速率，增加轉場時間

pygame.quit()
sys.exit()