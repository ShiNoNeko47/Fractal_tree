#!/usr/bin/python

import pygame
import math
import sys

def draw_tree(window, color, n, nmax, length, length_diff, angle, angle_diff, root):
    recursion = True
    if n == 0:
        pygame.display.update()
        return 0
    end = (root[0] + math.sin(angle) * length, root[1] + math.cos(angle) * length)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.draw.line(window, (color), root, end, int(n / 4 + 1))
    if recursion:
        draw_tree(window, color, n-1, nmax, length * length_diff, length_diff, angle + angle_diff, angle_diff, end)
    if recursion:
        draw_tree(window, color, n-1, nmax, length * length_diff, length_diff, angle - angle_diff, angle_diff, end)

def main():
    pygame.init()
    window = pygame.display.set_mode((800, 600))

    color = (255, 0, 0)

    loop = True
    angle_diff = math.pi / 6
    window.fill((0, 0, 0))
    while loop:
        #angle_diff -= math.pi / 512
        draw_tree(window, list(color), 15, 17, 100, .8, -math.pi, angle_diff, (400, 600))
        pygame.display.update()

if __name__ == '__main__':
    main()

