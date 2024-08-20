from math import floor

import pygame
from settings import get_settings
from grid import Grid

import pygame.freetype

settings = get_settings()

screen_size = int(settings['screen-size'])
grid_size = int(settings['grid-size'])
background_color = settings['background-color']

padding = int(settings['padding'])
margin = int(settings['margin'])
inner_padding = int(settings['inner-padding'])
border_radius = int(settings['border-radius'])

number_colors = settings['number-colors']

box_size = floor((screen_size - (margin * 2 + padding * (grid_size - 1))) / grid_size)

pygame.init()
pygame.font.init()

game_font = pygame.font.Font("ClearSans-Bold.ttf", box_size - inner_padding * 2)

screen = pygame.display.set_mode((screen_size, screen_size))
clock = pygame.time.Clock()
running = True

grid = Grid(grid_size)
grid.spawn_random()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                grid.move_up()
                grid.spawn_random()
            if event.key == pygame.K_a:
                grid.move_left()
                grid.spawn_random()
            if event.key == pygame.K_s:
                grid.move_down()
                grid.spawn_random()
            if event.key == pygame.K_d:
                grid.move_right()
                grid.spawn_random()

    screen.fill(background_color)

    x = margin
    y = margin
    for i in range(grid_size):
        x = margin
        for j in range(grid_size):
            val = str(grid.grid[i][j])
            r = pygame.Rect(x, y, box_size, box_size)
            pygame.draw.rect(screen, number_colors['background'][val], r, border_radius=border_radius)

            text_surface = game_font.render(val, True, number_colors['text'][val])

            text_width, text_height = text_surface.get_size()
            text_x = x + (box_size - text_width) / 2
            text_y = y + (box_size - text_height) / 2

            screen.blit(text_surface, (text_x, text_y))

            x += box_size + padding
        y += box_size + padding

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
