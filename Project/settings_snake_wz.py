from constants_snake_wz import *
from draw_pygame_wz import *


class Settings:

    def __init__(self, speed, wall):
        self.buttons = []
        self.width = WIDTH
        self.height = SCREEN_HEIGHT
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.running = 1
        self.speed = speed
        self.wall = wall

    def get_speed(self):
        return self.speed

    def get_wall(self):
        return self.wall

    def start(self):
        while self.running:

            self.screen.fill(BACKGROUND_COLOR)

            normal_color = (0, 80, 0)
            highlighted_color = (0, 50, 0)

            draw_text_2(self.screen, self.width / 2, int(self.height / 4), "SETTINGS", (0, 150, 0), 100)

            back_button = draw_button(self.screen, self.width / 1.25, int(self.height / 1.05), "MAIN MENU", normal_color,
                                      highlighted_color, 50)

            draw_text_2(self.screen, self.width / 2, int(self.height / 2), str("SPEED OF SNAKE : ")
                        + str(self.speed), (0, 150, 0), 50)

            speed_up_button = draw_button(self.screen, self.width - 80, self.height / 2 - 8, "+", normal_color,
                                          highlighted_color, 100)
            speed_down_button = draw_button(self.screen, self.width - 45, self.height / 2 - 5, "-", normal_color,
                                            highlighted_color, 100)

            draw_text_2(self.screen, self.width / 2, self.height / 2 + 70, str("COLLISION WITH WALL : "),
                        (0, 150, 0), 50)

            if self.wall == WallCollision.YES:
                wall_yes_button = draw_button(self.screen, self.width - 45, self.height / 2 + 70, "YES", normal_color,
                                              highlighted_color, 50)

            elif self.wall == WallCollision.NO:
                wall_no_button = draw_button(self.screen, self.width - 45, self.height / 2 + 70, "NO", normal_color,
                                              highlighted_color, 50)

            draw_text(self.screen, 100, int(self.height / 1.03), "By Wojciech Zielinski", (0, 130, 40), 25)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if check_if_button_clicked(back_button):
                        self.running = 0

                    if check_if_button_clicked(speed_down_button):
                        if self.speed > 1:
                            self.speed -= 1

                    if check_if_button_clicked(speed_up_button):
                        if self.speed < 9:
                            self.speed += 1

                    if self.wall == WallCollision.YES:
                        if check_if_button_clicked(wall_yes_button):
                            self.wall = WallCollision.NO
                    elif self.wall == WallCollision.NO:
                        if check_if_button_clicked(wall_no_button):
                            self.wall = WallCollision.YES

            pygame.display.update()
