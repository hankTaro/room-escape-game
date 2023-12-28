import pygame
from game_controller import GameController
from game_model import GameModel
from game_view import GameView
from setting import FPS


class Game:
    def run(self):
        # initialization
        pygame.init()
        game_model = GameModel()  # core of the game (database, game logic...)
        game_view = GameView()  # render everything
        game_control = GameController(game_model, game_view)  # deal with the game flow and user request


        quit_game = False
        pause = False

        game_model.start_ch1()
        # game_model.test_init()

        #背景音樂
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.load('music/background.mp3')
        pygame.mixer.music.play(-1) #無限播放

        while not quit_game:
            pygame.time.Clock().tick(FPS)  # control the frame rate
            game_control.receive_user_input()  # receive user input
            # game_control.update_user_request() # update the user request
            pause = game_control.is_pause
            if not pause:
                game_control.update_model()  # update the model
                game_control.update_view()  # update the view
                pygame.display.update()
            quit_game = game_control.quit_game

