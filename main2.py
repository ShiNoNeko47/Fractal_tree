#!/usr/bin/python

import pygame
import math
import sys
import time


def draw_tree(window, color, n, i, length, length_diff, angle, angle_diff, root):
    if n == 0:
        return 0
    end = (root[0] + math.sin(angle) * length,
           root[1] + math.cos(angle) * length)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if i <= n:
        pygame.draw.line(window, (color), root, end, int((n - i) / 4 + 1))
        print(int(n - i + 1))
        if i == n:
            return 0
    draw_tree(window, color, n-1, i, length * length_diff,
              length_diff, angle + angle_diff, angle_diff, end)
    draw_tree(window, color, n-1, i, length * length_diff,
              length_diff, angle - angle_diff, angle_diff, end)


def main():
    pygame.init()
    window = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    color = (255, 0, 0)

    loop = True
    angle_diff = math.pi / 6
    while loop:
        window.fill((0, 0, 0))
        n = 15
        for i in range(n):
            clock.tick(10)
            print(i)
            draw_tree(window, list(color), n, n - i,
                      100, .8, -math.pi, angle_diff, (400, 600))
            pygame.display.update()
        time.sleep(1)


if __name__ == '__main__':
    main()
