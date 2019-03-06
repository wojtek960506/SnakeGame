import os

from constants_snake_wz import *
from draw_pygame_wz import *
from help_text_snake_wz import *


class Highscores:

    def __init__(self):
        self.width = WIDTH
        self.height = SCREEN_HEIGHT
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.running = 1

    @staticmethod
    def get_scores():
        if not os.path.exists("./" + FILE_NAME):
            return []

        file = open(FILE_NAME, "r")
        if file.mode == 'r':
            content = file.readlines()

        file.close()



        scores = [int(x) for x in content]

        return scores

    def start(self):
        while self.running:

            self.screen.fill(BACKGROUND_COLOR)

            normal_color = (0, 80, 0)
            highlighted_color = (0, 50, 0)

            draw_text_2(self.screen, self.width / 2, int(self.height / 4), "HIGHSCORES", (0, 150, 0), 100)

            scores = self.get_scores()
            move = 0
            i = 1

            if len(scores) == 0:
                draw_text_2(self.screen, self.width / 2, int(self.height / 2), str("No scores stored yet"),
                            (0, 150, 0), 70)
            else:
                for score in scores:
                    tmp_str = str(i) + ". " + str(score)

                    if len(str(score)) < 4:
                        tmp_score_str = str(score) + " " * (4 - len(str(score)))
                        tmp_str = str(i) + ". " + tmp_score_str

                    while len(tmp_str) < 10:

                        tmp_str = " " + tmp_str

                    draw_text_2(self.screen, self.width / 2, int(self.height / 2.75) + move, str(tmp_str),
                                (0, 150, 0), 50)
                    move += 35
                    i += 1

            back_button = draw_button(self.screen, self.width / 1.25, int(self.height / 1.05), "MAIN MENU",
                                      normal_color,
                                      highlighted_color, 50)

            draw_text(self.screen, 100, int(self.height / 1.03), "By Wojciech Zielinski", (0, 130, 40), 25)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if check_if_button_clicked(back_button):
                        self.running = 0

            pygame.display.update()
