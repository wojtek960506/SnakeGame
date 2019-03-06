import pygame
from constants_snake_wz import *


# class for every single block of snake
class Block:
    direction = Direction.RIGHT
    size = SNAKE_BLOCK_SIZE

    def __init__(self, position_x, position_y, color=SNAKE_BLOCK_COLOR):
        self.position_x = int(position_x)
        self.position_y = int(position_y)
        self.color = color

    def get_size(self):
        return self.size

    def set_direction(self, direction):
        self.direction = direction

    def get_direction(self):
        return self.direction

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_position_x(self, position_x):
        self.position_x = position_x

    def get_position_x(self):
        return self.position_x

    def set_position_y(self, position_y):
        self.position_y = position_y

    def get_position_y(self):
        return self.position_y

    def draw_block(self, screen):
        pygame.draw.rect(screen, self.color, [self.position_x, self.position_y, self.size, self.size])


# to store information about snake and move it
class Snake:

    def __init__(self):
        self.blocks = []
        self.spots_of_turn = []
        self.head = Block(WIDTH / 2, HEIGHT / 2, SNAKE_HEAD_COLOR)
        self.blocks.append(self.head)
        b = 1  # to create blocks in proper positions
        for i in range(SNAKE_INIT_LENGTH):
            block = Block(self.head.get_position_x() - self.head.get_size() * b, self.head.get_position_y())
            self.blocks.append(block)
            b += 1
        self.tail = self.blocks[-1]

    def get_blocks(self):
        return self.blocks

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def add_spot_of_turn(self, spot):
        self.spots_of_turn.append(spot)

    def get_without_head(self):
        return self.blocks[1:]

    # return True if there was collision of head with
    def move(self, wall):
        for block in self.blocks:
            pos_x = block.get_position_x()
            pos_y = block.get_position_y()
            dir = block.get_direction()

            for spot in self.spots_of_turn:
                if (spot.get("pos_x") == pos_x) & (spot.get("pos_y") == pos_y):
                    dir = spot.get("dir")
                    block.set_direction(dir)
                    if block == self.tail:
                        self.spots_of_turn.remove(spot)

            if dir == Direction.UP:
                block.set_position_y(pos_y - SNAKE_BLOCK_SIZE)
                if wall == WallCollision.NO:
                    if block.get_position_y() < 0:
                        block.set_position_y(HEIGHT - SNAKE_BLOCK_SIZE)

            elif dir == Direction.DOWN:
                block.set_position_y(pos_y + SNAKE_BLOCK_SIZE)
                if wall == WallCollision.NO:
                    if block.get_position_y() >= HEIGHT:
                        block.set_position_y(0)

            elif dir == Direction.LEFT:
                block.set_position_x(pos_x - SNAKE_BLOCK_SIZE)
                if wall == WallCollision.NO:
                    if block.get_position_x() < 0:
                        block.set_position_x(WIDTH - SNAKE_BLOCK_SIZE)

            elif dir == Direction.RIGHT:
                block.set_position_x(pos_x + SNAKE_BLOCK_SIZE)
                if wall == WallCollision.NO:
                    if block.get_position_x() >= WIDTH:
                        block.set_position_x(0)

            # check if head didn't collide with wall (this option is set in settings)
            if wall == WallCollision.YES:
                if self.head.get_position_x() < 0:
                    return True

                elif self.head.get_position_x() >= WIDTH:
                    return True

                elif self.head.get_position_y() < 0:
                    return True

                elif self.head.get_position_y() >= HEIGHT:
                    return True

        return False

    def after_eating(self):
        tail_pos_x = self.tail.get_position_x()
        tail_pos_y = self.tail.get_position_y()
        tail_dir = self.tail.get_direction()

        if tail_dir == Direction.RIGHT:
            tail_pos_x -= SNAKE_BLOCK_SIZE
        if tail_dir == Direction.LEFT:
            tail_pos_x += SNAKE_BLOCK_SIZE
        if tail_dir == Direction.UP:
            tail_pos_y += SNAKE_BLOCK_SIZE
        if tail_dir == Direction.DOWN:
            tail_pos_y -= SNAKE_BLOCK_SIZE

        block = Block(tail_pos_x, tail_pos_y)
        block.set_direction(tail_dir)
        self.tail = block
        self.blocks.append(block)

    def draw(self, screen):
        for block in self.blocks:
            block.draw_block(screen)


# class to store information about 'food' in the game
class Food:
    color = FOOD_COLOR
    size = SNAKE_BLOCK_SIZE

    def __init__(self):

        pos_x = int(WIDTH / 4)
        pos_y = int(HEIGHT / 4)

        if pos_x % SNAKE_BLOCK_SIZE != 0:
            pos_x = pos_x + (pos_x % SNAKE_BLOCK_SIZE)
        if pos_y % SNAKE_BLOCK_SIZE != 0:
            pos_y = pos_y + (pos_y % SNAKE_BLOCK_SIZE)

        self.position_x = pos_x
        self.position_y = pos_y

    def set_position_x(self, position_x):
        self.position_x = position_x

    def get_position_x(self):
        return self.position_x

    def set_position_y(self, position_y):
        self.position_y = position_y

    def get_position_y(self):
        return self.position_y

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.position_x, self.position_y, self.size, self.size])