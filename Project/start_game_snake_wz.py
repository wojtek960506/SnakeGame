import os
import random
import datetime
from pathlib import Path

from snake_snake_wz import *


class StartGame:
    width, height = WIDTH, SCREEN_HEIGHT
    score = 0
    pause = 0
    running = 1
    total_time = ""
    pause_time = 0
    game_over_check = 0

    def __init__(self, speed, wall):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.snake = Snake()
        self.food = Food()
        self.current_direction = Direction.RIGHT
        self.time_elapsed_since_last_action = 0
        self.clock = pygame.time.Clock()
        self.snake_speed = speed
        self.wall = wall
        self.events = []

    def get_score(self):
        return self.score

    def move(self):
        dt = self.clock.tick()
        self.time_elapsed_since_last_action += dt

        # movement of snake every timelaps
        if self.time_elapsed_since_last_action > 500 / self.snake_speed:

            if len(self.events) > 0:
                self.do_event(self.events[0])
                del self.events[0]

            if self.snake.move(self.wall):
                self.game_over()

            # to check if sneak don't eat itself
            self.check_collision()

            # to check if snake is eating
            self.check_eating()

            self.time_elapsed_since_last_action = 0  # reset before next movement

    def check_eating(self):
        head_pos_x = self.snake.get_head().get_position_x()
        head_pos_y = self.snake.get_head().get_position_y()

        food_pos_x = self.food.get_position_x()
        food_pos_y = self.food.get_position_y()

        if (head_pos_x == food_pos_x) & (head_pos_y == food_pos_y):
            while True:

                # check if new position of food is not inside snake
                new_food_pos_x = random.randint(0, int(WIDTH / SNAKE_BLOCK_SIZE) - 1) * SNAKE_BLOCK_SIZE
                new_food_pos_y = random.randint(0, int(HEIGHT / SNAKE_BLOCK_SIZE) - 1) * SNAKE_BLOCK_SIZE

                flag = 0

                for block in self.snake.get_blocks():
                    block_pos_x = block.get_position_x()
                    block_pos_y = block.get_position_y()

                    if (block_pos_x == new_food_pos_x) & (block_pos_y == new_food_pos_y):
                        flag = 1

                if flag == 1:
                    continue
                else:
                    break

            self.food.set_position_x(new_food_pos_x)
            self.food.set_position_y(new_food_pos_y)

            self.snake.after_eating()
            self.score += self.snake_speed

    def check_collision(self):
        snake_without_head = self.snake.get_without_head()

        head_pos_x = self.snake.get_head().get_position_x()
        head_pos_y = self.snake.get_head().get_position_y()

        # check if head coordinates are the same as coordinates of any part of snake
        for block in snake_without_head:
            block_pos_x = block.get_position_x()
            block_pos_y = block.get_position_y()

            if (head_pos_x == block_pos_x) & (head_pos_y == block_pos_y):
                self.game_over()

    def draw_text(self, pos_x, pos_y, text, text_color, font_size):
        font = pygame.font.Font(None, font_size)
        button_text = font.render(str(text), True, text_color)
        button_text_rect = button_text.get_rect()
        button_text_rect.center = (pos_x, pos_y)
        self.screen.blit(button_text, button_text_rect)
        return button_text_rect

    def game_over(self):

        while True:
            self.screen.fill(GAME_OVER_SCREEN)
            self.draw_text(self.width / 2, self.height / 2, "GAME OVER !!!", BLACK_COLOR, 100)
            self.draw_text(self.width / 2, self.height / 1.5, str("Score : ") + str(self.score), BLACK_COLOR, 50)
            self.draw_text(self.width / 2, self.height / 1.5 + 50, str(self.total_time), BLACK_COLOR, 50)
            self.draw_text(self.width / 2, self.height - 25, "Press B to go back to Main Menu", BLACK_COLOR, 50)
            self.finish_pause(False)

            pygame.display.update()

            if self.running == 0:
                self.game_over_check = 1
                break

    def draw(self):
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        pygame.draw.rect(self.screen, GREEN_COLOR, [0, HEIGHT, WIDTH, SCREEN_HEIGHT - HEIGHT])
        if self.pause:
            self.draw_text(self.width / 2 + 100, 620, str("Pause. Press P to continue"), BLACK_COLOR, 30)

    def get_events(self):
        for event in pygame.event.get():
            if len(self.events) < 3:
                if event.type == pygame.KEYDOWN:
                    e_k = event.key
                    if e_k in AVAILABLE_KEYS:
                        self.events.append(event)
                if event.type == pygame.QUIT:
                    self.events.append(event)

    def finish_pause(self, pause=True):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            if event.type == pygame.KEYDOWN:
                if pause:
                    if event.key == K_p:
                        if self.pause == 0:
                            self.pause = 1
                        else:
                            self.pause = 0

                if event.key == K_b:
                    if pause:
                        self.are_you_sure()
                    else:
                        self.running = 0

    def do_event(self, event):
        if True:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            if event.type == pygame.KEYDOWN:

                def add_spot_of_turn(direction):
                    pos_x = self.snake.get_head().get_position_x()
                    pos_y = self.snake.get_head().get_position_y()
                    dir = direction
                    dict = {
                        "pos_x": pos_x,
                        "pos_y": pos_y,
                        "dir": dir
                    }
                    self.snake.add_spot_of_turn(dict)

                if event.key == K_w:
                    if (self.current_direction != Direction.UP) & (self.current_direction != Direction.DOWN):
                        add_spot_of_turn(Direction.UP)
                    self.current_direction = Direction.UP

                elif event.key == K_a:
                    if (self.current_direction != Direction.RIGHT) & (self.current_direction != Direction.LEFT):
                        add_spot_of_turn(Direction.LEFT)
                    self.current_direction = Direction.LEFT

                elif event.key == K_s:
                    if (self.current_direction != Direction.UP) & (self.current_direction != Direction.DOWN):
                        add_spot_of_turn(Direction.DOWN)
                    self.current_direction = Direction.DOWN

                elif event.key == K_d:
                    if (self.current_direction != Direction.RIGHT) & (self.current_direction != Direction.LEFT):
                        add_spot_of_turn(Direction.RIGHT)
                    self.current_direction = Direction.RIGHT

                elif event.key == K_p:
                    if self.pause == 0:
                        self.pause = 1
                    else:
                        self.pause = 0

                elif event.key == K_b:
                    self.are_you_sure()

    def are_you_sure(self):
        not_stop = 1
        while not_stop:

            pygame.draw.rect(self.screen, WHITE_COLOR, [WIDTH / 4, HEIGHT / 4 + 10, WIDTH / 2, HEIGHT / 3])
            pygame.draw.rect(self.screen, BLUE_COLOR, [WIDTH / 4, HEIGHT / 4 + 10, WIDTH / 2, 30])

            self.draw_text(self.width / 2, self.height / 2 - 100, str("ARE YOU SURE"), BLACK_COLOR, 40)
            self.draw_text(self.width / 2, self.height / 2 - 70, str("TO END THE GAME ?"), BLACK_COLOR, 40)
            self.draw_text(self.width / 2, self.height / 2 , str("(Y)es or (N)o"), BLACK_COLOR, 50)



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

                if event.type == pygame.KEYDOWN:
                    if event.key == K_y:
                        self.running = 0
                        not_stop = 0
                    if event.key == K_n:
                        self.running = 1
                        not_stop = 0

            pygame.display.update()

            if not_stop == 0:
                break

    def start(self):
        while True:
            self.screen.fill(BACKGROUND_COLOR)
            self.draw()
            self.draw_text(self.height / 2, 620, str("Press D to start"), BLACK_COLOR, 40)

            pygame.display.update()
            flag = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

                if event.type == pygame.KEYDOWN:
                    if event.key == K_d:
                        flag = 1

                    elif event.key == K_b:
                        self.are_you_sure()

            if self.running == 0:
                break

            if flag == 1:
                break

        # to count time from the moment when we actually start to play
        start_time = pygame.time.get_ticks()
        while self.running:
            self.screen.fill(BACKGROUND_COLOR)
            self.draw()

            if self.pause == 0:
                self.move()
            else:
                self.finish_pause()

            self.get_events()

            self.draw_text(70, 620, str("Score : ") + str(self.score), BLACK_COLOR, 40)

            self.draw_text(560, 620, str(int((pygame.time.get_ticks() - start_time) / 60000)) + ":"
                           + str(int((pygame.time.get_ticks() - start_time) / 1000 % 60)).zfill(2), BLACK_COLOR, 40)

            self.total_time = str("Total Time -> ") + str(int((pygame.time.get_ticks() - start_time) / 60000)) \
                              + ":" + str(int((pygame.time.get_ticks() - start_time) / 1000 % 60)).zfill(2)

            pygame.display.update()

        if self.game_over_check:
            self.save_score()

    def save_score(self):
        if not os.path.exists("./"+FILE_NAME):
            file = open(FILE_NAME, "w+")

        file = open(FILE_NAME, "r")
        scores = []
        if file.mode == 'r':
            content = file.readlines()
        file.close()



        scores = [int(x) for x in content]
        scores.append(int(self.score))

        #we want to have orders stored sorted in descendent order
        scores.sort(reverse=True)

        if len(scores) > 10:
            scores = scores[:10]

        file = open(FILE_NAME, "w")

        for score in scores:
            file.write(str(score)+"\n")
