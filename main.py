import pygame
from math import pi, sin, cos
from pygame.locals import *
from pygame_tools import *

#theta = i/self.density * 3.14159265
#x = 16 * pow(sin(theta), 3)
#x = int(self.scale * x + self.pos[0])
#y = 13 * cos(theta) - 5 * cos(2 * theta) - 2 * cos(3 * theta) - cos(4 * theta)
#y = -int(self.scale * y - self.pos[1])

class Heart:
    def __init__(self, position: Point, scale: int, point_density: int = 50):
        self.position = position
        self.scale = scale
        self.point_density = point_density

    def draw(self, surface, position = None):
        if position is None:
            position = self.position
        points = []
        for i in range(2 * self.point_density):
            theta = i / self.point_density * pi
            points.append(Point(
                int(self.scale * (16 * sin(theta) ** 3) + position.x),
                -int(self.scale * (13 * cos(theta) - 5 * cos(2 * theta) - 2 * cos(3 * theta) - cos(4 * theta)) - position.y),
                ))
        pygame.draw.lines(surface, 'white', True, points)

class HeartScreen(GameScreen):
    def __init__(self):
        pygame.init()
        real_size = Point(600, 600)
        size = Point(real_size.x // 8, real_size.y // 8)
        super().__init__(pygame.display.set_mode(real_size), real_size, size)
        self.heart = Heart(Point(self.window_size.x // 2, self.window_size.y // 2), 1.5, 500)

    def update(self):
        self.screen.fill('black')
        self.heart.draw(self.screen)

if __name__ == '__main__':
    hs = HeartScreen()
    hs.run()
