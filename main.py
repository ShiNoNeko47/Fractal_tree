#!/usr/bin/python

import pygame
import math

def draw_tree(window, color, n, length, length_diff, angle, angle_diff, root):
    if n == 0:
        return 0
    end = (root[0] + math.sin(angle) * length, root[1] + math.cos(angle) * length)
    pygame.draw.line(window, color, root, end, int(n / 2))
    draw_tree(window, color, n-1, length * length_diff, length_diff, angle + angle_diff, angle_diff, end)
    draw_tree(window, color, n-1, length * length_diff, length_diff, angle - angle_diff, angle_diff, end)

def main():
    pygame.init()
    window = pygame.display.set_mode((800, 600))

    loop = True
    angle_diff = math.pi / 4
    while loop:
        window.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_PLUS:
                    angle_diff += .025
                if event.key == pygame.K_MINUS:
                    angle_diff -= .025
        angle_diff -= math.pi / 512
        draw_tree(window, (0, 255, 0), 13, 100, .8, -math.pi, angle_diff, (400, 600))
        pygame.display.update()

if __name__ == '__main__':
    main()
