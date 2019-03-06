from pygame.locals import *
from enum import Enum

# constants
WIDTH = 600
HEIGHT = 600
SCREEN_HEIGHT = 640
SNAKE_INIT_LENGTH = 3
SNAKE_BLOCK_SIZE = 30
SNAKE_SPEED = 5

# in case of press key which is not in this list, nothing will happen
AVAILABLE_KEYS = [K_w, K_a, K_s, K_d, K_b, K_p]

WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (30, 30, 30)
SNAKE_HEAD_COLOR = (125, 125, 125)
SNAKE_BLOCK_COLOR = (200, 200, 200)
FOOD_COLOR = (139, 0, 0)  # dark red, normal red is with 255
GREEN_COLOR = (0, 200, 0)
GAME_OVER_SCREEN = (100, 0, 0)
BLUE_COLOR = (0, 50, 150)

FILE_NAME = "scores_snake_wz.txt"

# to check collision with wall
class WallCollision(Enum):
    YES = "YES"
    NO = "NO"

    def __str__(self):
        return str(self.value)


# direction of snake
class Direction(Enum):
    RIGHT = "right"
    LEFT = "left"
    UP = "up"
    DOWN = "down"

    def __str__(self):
        return str(self.value)


# to check into which screen change
class NextScreen(Enum):
    START = "START"
    SETTINGS = "SETTINGS"
    HELP = "HELP"
    HIGHSCORES = "HIGHSCORES"
    QUIT = "QUIT"
    NONE = "NONE"

    def __str__(self):
        return str(self.value)
