import pygame
import cv2
import numpy as np

WIN_WIDTH = 1024
WIN_HEIGHT = 600
FPS = 60
BLACK = (0, 0, 0)
VIDEO_EVENT = pygame.USEREVENT + 1  # Custom event for video playback

pygame.init()
pygame.mixer.init()

class Game:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.font_size = 30
        self.font = pygame.font.Font("New-Super-Mario-Font-U-1.ttf", self.font_size)
        self.movie = cv2.VideoCapture("image/TV_show/meme_1.mp4")
        self.playing_video = False
        # pygame.time.set_timer(VIDEO_EVENT, int(2000 / FPS), 0)  # Set timer event for video playback
        pygame.mixer.music.load("image/TV_show/meme_1.mp3")

    def draw_bg(self, surf):
        pygame.draw.rect(surf, BLACK, [0, 0, WIN_WIDTH, WIN_HEIGHT], 0)

    def play_video(self):
        # ret:bool判斷是否結束 frame每一格rgb值
        ret, frame = self.movie.read()

        if not ret:
            self.movie.set(cv2.CAP_PROP_POS_FRAMES, 0) # 結束將影片重製
            self.playing_video = False
            return

        # frame = cv2.resize(frame,(100,100))
        frame = cv2.flip(frame, 1) # 做左右向反
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # 換成彩色
        frame = pygame.surfarray.make_surface((np.rot90(frame)))  # 轉90度 畫在畫面上
        self.win.blit(frame, (100, 90))

    def game_run(self):
        run = True
        self.draw_bg(self.win)
        pygame.time.set_timer(VIDEO_EVENT, int(2000 / FPS), 0)
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing_video = False
                    self.movie.release()
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        # Toggle video play/pause
                        self.playing_video = not self.playing_video
                        if self.playing_video:
                            pygame.mixer.music.play()
                        else:
                            pygame.mixer.music.stop()

                elif event.type == VIDEO_EVENT and self.playing_video:
                    self.play_video()

            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.game_run()