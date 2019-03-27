import pygame
from Logic import *
from Pieces import *
import sys
import Stack
import random
import time

pygame.init()
size = int(input("How many tiles would you like in the maze?\n"))
piece_size = 75+2
screen = pygame.display.set_mode((size*piece_size, size*piece_size), pygame.RESIZABLE)

def set_grid(grid_size):
    grid = []
    for x in range(size):
        row = []
        for y in range(size):
            row.append(0)
        grid.append(row)
    return grid

def print_grid(grid):
    for row in grid:
        print(row)

def rendering(grid, screen):
    for row in grid:
        for element in row:
            try:
                element.render(screen)
            except AttributeError:
                pass

def testing():
    screen.fill((255, 255, 255))
    grid = set_grid(size)
    for x in range(size):
        for y in range(size):
            name = match_piece([], [])
            grid[x][y] = make_piece(name)

    update_locations(grid, piece_size)
    rendering(grid, screen)



test = False
real = True
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            test = True

    if test:
        testing()
        test = False
        pygame.display.flip()
    if real:
        screen.fill((255, 255, 255))
        grid = set_grid(size)
        grid,  startPoint = determing_Start_location(grid, size)
        pygame.display.flip()
        update_locations(grid, piece_size)
        rendering(grid, screen)
        generate_path(startPoint, grid,  False)
        update_locations(grid, piece_size)
        rendering(grid, screen)
        pygame.display.flip()
        real = False


