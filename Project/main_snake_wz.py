# import my other files for this game
from start_game_snake_wz import *
from main_menu_snake_wz import *
from settings_snake_wz import *
from help_snake_wz import *
from highscores_snake_wz import *


def main():

    speed = SNAKE_SPEED
    wall = WallCollision.NO  # by default there is no collision with wall

    while True:

        menu = MainMenu()
        menu.main_menu()

        next_screen = menu.get_next_screen()

        if next_screen == NextScreen.START:
            game = StartGame(speed, wall)
            game.start()

        elif next_screen == NextScreen.QUIT:
            pygame.quit()
            quit()

        elif next_screen == NextScreen.SETTINGS:
            settings = Settings(speed, wall)
            settings.start()
            speed = settings.get_speed()
            wall = settings.get_wall()

        elif next_screen == NextScreen.HELP:
            help = Help()
            help.start()

        elif next_screen == NextScreen.HIGHSCORES:
            highscores = Highscores()
            highscores.start()


if __name__ == '__main__':
    main()
