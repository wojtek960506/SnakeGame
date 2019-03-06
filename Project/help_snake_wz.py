from constants_snake_wz import *
from draw_pygame_wz import *
from help_text_snake_wz import *


class Help:

    def __init__(self):
        self.width = WIDTH
        self.height = SCREEN_HEIGHT
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.running = 1

    def start(self):
        while self.running:

            self.screen.fill(BACKGROUND_COLOR)

            normal_color = (0, 80, 0)
            highlighted_color = (0, 50, 0)

            draw_text_2(self.screen, self.width / 2, int(self.height / 4), "HELP", (0, 150, 0), 100)

            draw_text_2(self.screen, self.width / 2, int(self.height / 2)-80, str(help_text0), (0, 150, 0), 35)
            draw_text_2(self.screen, self.width / 2, int(self.height / 2)-55, str(help_text1), (0, 150, 0), 25)
            draw_text_2(self.screen, self.width / 2, int(self.height / 2)-30, str(help_text2), (0, 150, 0), 25)
            draw_text_2(self.screen, self.width / 2, int(self.height / 2)-10, str(help_text3), (0, 150, 0), 25)

            draw_text_2(self.screen, self.width / 2, int(self.height / 2)+40, str(help_text4), (0, 150, 0), 35)
            draw_text_2(self.screen, self.width / 2, int(self.height / 2)+65, str(help_text5), (0, 150, 0), 25)
            draw_text_2(self.screen, self.width / 2, int(self.height / 2)+90, str(help_text6), (0, 150, 0), 25)
            draw_text_2(self.screen, self.width / 2, int(self.height / 2)+120, str(help_text7), (0, 150, 0), 25)
            draw_text_2(self.screen, self.width / 2, int(self.height / 2)+145, str(help_text8), (0, 150, 0), 25)
            draw_text_2(self.screen, self.width / 2, int(self.height / 2)+170, str(help_text9), (0, 150, 0), 25)

            draw_text_2(self.screen, self.width / 2, int(self.height / 2)+220, str(help_text10), (0, 150, 0), 25)

            back_button = draw_button(self.screen, self.width / 1.25, int(self.height / 1.05), "MAIN MENU", normal_color,
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
