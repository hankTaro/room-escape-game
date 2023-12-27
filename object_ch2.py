import os
import pygame
import cv2
import numpy as np
from user_request import *
from setting import *

# TODO : 將所有物件的圖片匯入 並調整至合適大小
# 同個物件 不同狀況(像是開啟/關閉)可以用相同名字，後面用tv-1 tv-2 做區分
# tv_image = [pygame.transform.scale(pygame.image.load(f"image/Object/Tv/tv-{i}.png"), (int(201), int(211))) for i in range(1)]
pygame.mixer.init()
pygame.mixer.music.set_volume(0.2)

# 聲音
tv_show_1_sound = pygame.mixer.Sound('music/meme_1.wav')
tv_show_2_sound = pygame.mixer.Sound('music/tyler1 scream meme.wav')
tv_show_4_sound = pygame.mixer.Sound('music/Pornhub Video intro.wav')
tv_show_5_sound = pygame.mixer.Sound('music/KFC Chickendales Mother’s Day Performance.wav')
clock_sound = pygame.mixer.Sound('music/clock.wav')
clock_hand_sound = pygame.mixer.Sound('music/clock_hand.wav')
walking_sound = pygame.mixer.Sound('music/walking.wav')
door_open_sound = pygame.mixer.Sound('music/door_open.wav')
tv_change_channel_sound = pygame.mixer.Sound('music/tv_change_channel.wav')
tv_power_sound = pygame.mixer.Sound('music/tv_change_channel.wav')
knob_twist_sound = pygame.mixer.Sound('music/knob_twist.wav')
knob_open_sound = pygame.mixer.Sound('music/knob_open.wav')
locker_setup_sound = pygame.mixer.Sound('music/locker_setup.wav')
locker_open_sound = pygame.mixer.Sound('music/locker_open.wav')
little_cabinet_open_sound = pygame.mixer.Sound('music/little_cabinet_open.wav')
little_cabinet_close_sound = pygame.mixer.Sound('music/little_cabinet_close.wav')
cheat_code_sound = pygame.mixer.Sound('music/cheat_code.mp3')



door_image_1  = pygame.transform.scale(pygame.image.load(f"image/living_room/Door/door_1.png"), (GAME_WIDTH, GAME_HEIGHT))

class DoorToExitCh2:
    def __init__(self, x, y):
        self.image = door_image_1
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

        self.speaker = "旁白"
        self.dialog = "離開房屋的門\n手把上充滿著鏽蝕與歲月痕跡\n" \
                      "在你進屋開門時，他發出了吵雜的摩擦噪音" #\n千里迢迢來到這裡可不只是為了進來撇一眼的\n你使勁全力依然打不開他
        self.music = door_open_sound

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'done'
        else:
            return 0