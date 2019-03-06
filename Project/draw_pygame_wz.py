import pygame


def draw_text(screen, pos_x, pos_y, text, text_color, font_size):
    font = pygame.font.Font(None, font_size)
    button_text = font.render(str(text), True, text_color)
    button_text_rect = button_text.get_rect()
    button_text_rect.center = (pos_x, pos_y)
    screen.blit(button_text, button_text_rect)
    return button_text_rect


def draw_text_2(screen, pos_x, pos_y, text, text_color, font_size):
    font = pygame.font.Font(None, font_size)
    button_text = font.render(str(text), True, text_color)
    button_text_rect = button_text.get_rect()
    button_text_rect.center = (pos_x, pos_y)
    screen.blit(button_text, button_text_rect)


def draw_button(screen, pos_x, pos_y, text, color_1, color_2, font_size,color_button=False):
    font = pygame.font.Font(None, font_size)
    button_text = font.render(str(text), True, color_1)
    button_text_rect = button_text.get_rect()
    button_text_rect.center = (pos_x, pos_y)

    if check_position(button_text_rect):
        button_text = font.render(str(text), True, color_2)

    screen.blit(button_text, button_text_rect)

    return button_text_rect

def check_if_button_clicked(button):
    position = pygame.mouse.get_pos()
    top = button.top
    left = button.left
    width = button.width
    height = button.height
    if (left < position[0] < left + width) & (top < position[1] < top + height):
        return True
    else:
        return False

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
