import pygame
from pygame.locals import *
from pygame_tools import *

#theta = i/self.density * 3.14159265
#x = 16 * pow(sin(theta), 3)
#x = int(self.scale * x + self.pos[0])
#y = 13 * cos(theta) - 5 * cos(2 * theta) - 2 * cos(3 * theta) - cos(4 * theta)
#y = -int(self.scale * y - self.pos[1])

class HeartScreen(GameScreen):
    def __init__(self):
        pygame.init()
        real_size = Point(600, 600)
        size = Point(real_size.x / 4, real_size.y / 4)
        super().__init__(pygame.display.set_mode(real_size), real_size, size)

if __name__ == '__main__':
    hs = HeartScreen()
    hs.run()
