import pygame, random

BLACK = (0, 0, 0)
BLUE = (0, 0, 25)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ALIEN_SIZE = (30, 0)
ALIEN_SPACER = 20
BARRIER_ROW = 10
BARRIER_COLUMN = 4
BULLET_SIZE = (5, 10)
MISSILE_SIZE = (5, 5)
BLOCK_SIZE = (10, 10)
RES = (800, 600)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.size = (60, 55)
        self.rect = self.image.get_rect()
        self.rect.x = (RES[0] / 2) - (self.size[0] / 2)
        self.rect.y = 520
        self.travel = 7
        self.speed = 350
        self.time = pygame.time.get_ticks()

    def update(self):
        self.rect.x += GameState.vector * self.travel


class GameState:
    pass
