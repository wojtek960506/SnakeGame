from constants_snake_wz import *
from draw_pygame_wz import *
import pygame


class MainMenu:
    width = WIDTH
    height = SCREEN_HEIGHT
    next_screen = NextScreen.NONE
    normal_button_color = (0, 80, 0)
    highlighted_button_color = (0, 50, 0)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.intro = 1
        self.start_button = draw_text(self.screen, self.width / 2, int(self.height / 2), "START",
                                      self.normal_button_color, 75)
        self.settings_button = draw_text(self.screen, self.width / 2, int(self.height / 2) + 50, "SETTINGS",
                                         self.normal_button_color, 75)
        self.help_button = draw_text(self.screen, self.width / 2, int(self.height / 2) + 100, "HELP",
                                     self.normal_button_color, 75)
        self.highscores_button = draw_text(self.screen, self.width / 2, int(self.height / 2) + 150, "HIGHSCORES",
                                           self.normal_button_color, 75)
        self.quit_button = draw_text(self.screen, self.width / 2, int(self.height / 2) + 200, "QUIT",
                                     self.normal_button_color, 75)

    def get_next_screen(self):
        return self.next_screen

    def check_if_button_clicked(self, next_screen, button):
        position = pygame.mouse.get_pos()
        top = button.top
        left = button.left
        width = button.width
        height = button.height
        if (left < position[0] < left + width) & (top < position[1] < top + height):
            self.intro = 0
            self.next_screen = next_screen

    @staticmethod
    def check_position(button):
        position = pygame.mouse.get_pos()
        top = button.top
        left = button.left
        width = button.width
        height = button.height
        if (left < position[0] < left + width) & (top < position[1] < top + height):
            return True
        else:
            return False

    def draw_button(self, button, move, text):
        if self.check_position(button):
            color = self.normal_button_color
        else:
            color = self.highlighted_button_color
        draw_text(self.screen, self.width / 2, int(self.height / 2) + move, text,
                  color, 75)

    def main_menu(self):
        while self.intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.start_button is not None:
                        self.check_if_button_clicked(NextScreen.START, self.start_button)
                    if self.settings_button is not None:
                        self.check_if_button_clicked(NextScreen.SETTINGS, self.settings_button)
                    if self.help_button is not None:
                        self.check_if_button_clicked(NextScreen.HELP, self.help_button)
                    if self.highscores_button is not None:
                        self.check_if_button_clicked(NextScreen.HIGHSCORES, self.highscores_button)
                    if self.quit_button is not None:
                        self.check_if_button_clicked(NextScreen.QUIT, self.quit_button)

            self.screen.fill(BACKGROUND_COLOR)

            draw_text(self.screen, self.width / 2, int(self.height / 4), "SNAKE", (0, 150, 0), 150)

            self.draw_button(self.start_button, 0, "START")
            self.draw_button(self.settings_button, 50, "SETTINGS")
            self.draw_button(self.help_button, 100, "HELP")
            self.draw_button(self.highscores_button, 150, "HIGHSCORES")
            self.draw_button(self.quit_button, 200, "QUIT")

            draw_text(self.screen, 100, int(self.height / 1.03), "By Wojciech Zielinski", (0, 130, 40), 25)

            pygame.display.update()
