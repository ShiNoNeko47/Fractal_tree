#!/usr/bin/python

import pygame
import math
import sys

def draw_tree(window, color, n, nmax, i, length, length_diff, angle, angle_diff, root):
    if n == 0:
        return 0
    end = (root[0] + math.sin(angle) * length, root[1] + math.cos(angle) * length)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    r, g, b = color
    r = 255 * (i / nmax)
    if i == n:
        pygame.draw.line(window, (r, g, b), root, end, int(i / 4 + 1))
    draw_tree(window, color, n-1, nmax, i, length * length_diff, length_diff, angle + angle_diff, angle_diff, end)
    draw_tree(window, color, n-1, nmax, i, length * length_diff, length_diff, angle - angle_diff, angle_diff, end)

def main():
    pygame.init()
    window = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    color = (255, 0, 0)

    loop = True
    angle_diff = math.pi / 6
    n = 15
    for i in range(n):
        clock.tick(10)
        print(i)
        draw_tree(window, list(color), n, n, i + 1, 100, .8, -math.pi, angle_diff, (400, 600))
    pygame.display.update()
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

if __name__ == '__main__':
    main()

