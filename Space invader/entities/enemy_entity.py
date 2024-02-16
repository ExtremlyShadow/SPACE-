import pygame.image

from entities.entity import Entity
from const.state import *
from const.value import *


class Egg(Entity):
    def __init__(self, image, x, y):
        super().__init__(image, x, y, 0.5, 0.5, IMAGE_SIZE)
        self.egg_state = EggState.INVISIBLE
        self.time = 0
        self.reload_time = RELOAD_TIME

    def fall(self, screen, destination):
        self.time = (self.Y - destination.Y) / self.y_velocity
        self.draw(screen)
        self.reload_time -= 1

    def moving(self):
        if self.time == 0:
            self.egg_state = EggState.INVISIBLE
            return
        self.Y -= self.y_velocity
        self.time -= 1

    def hit(self):
        self.time = 0

    def reload(self):
        if self.reload_time <= 0:
            self.reload_time = RELOAD_TIME
            self.egg_state = EggState.FLYING
        elif self.reload_time >= 0:
            self.reload_time -= 1
            self.egg_state = EggState.RELOAD


class Enemy(Entity):
    def __init__(self, image, x, y, enemy_health):
        super().__init__(image, x, y, 0.5, 0.5, 32)
        self.enemy_state = EnemyState.ALIVE
        self.health = enemy_health

    def hit(self, damage):
        self.health -= damage

    def dead(self, dead_image, screen):
        screen.blit(pygame.image.load(dead_image), (self.X, HEIGHT - self.Y))
        self.enemy_state = EnemyState.DEAD

    def moving(self):
        self.X -= self.x_velocity
        if self.X <= MIN_X or self.X >= MAX_X:
            self.x_velocity *= -1
