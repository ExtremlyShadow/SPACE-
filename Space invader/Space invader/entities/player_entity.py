from entities.entity import Entity
from const.state import *
from const.value import *


class Player(Entity):
    def __init__(self, image, x, y, player_lives):
        super().__init__(image, x, y, 1, 1, 32)
        self.lives = player_lives

    def hit(self):
        self.lives -= 1

    def moving_up(self):
        self.Y += self.y_velocity
        if self.Y >= MAX_Y:
            self.Y = MAX_Y

    def moving_down(self):
        self.Y -= self.y_velocity
        if self.Y <= PLAYER_MIN_Y:
            self.Y = PLAYER_MIN_Y

    def moving_left(self):
        self.X -= self.x_velocity
        if self.X <= MIN_X:
            self.X = MIN_X

    def moving_right(self):
        self.X += self.x_velocity
        if self.X >= MAX_X:
            self.X = MAX_X


class Bullet(Entity):
    def __init__(self, image, x, y):
        super().__init__(image, x, y, 0.5, 0.5, 32)
        self.bullet_state = BulletState.INVISIBLE
        self.time = 0

    def fire(self, screen, destination):
        self.bullet_state = BulletState.FLYING
        self.time = (destination.Y - self.Y) / self.y_velocity
        self.draw(screen)

    def moving(self):
        if self.time == 0:
            self.bullet_state = BulletState.INVISIBLE
            return
        self.Y += self.y_velocity
        self.time -= 1

    def hit(self):
        self.time = 0


class Rocket(Entity):
    def __init__(self, image, x, y):
        super().__init__(image, x, y, 0.5, 0.5, 32)
        self.time = 0
        self.rocket_state = RocketState.READY

    def fire(self, screen, destination):
        self.rocket_state = RocketState.FIRE
        self.time = ROCKET_MOVING_TIME
        self.draw(screen)
        self.y_velocity = (destination.Y - self.Y) / ROCKET_MOVING_TIME
        self.x_velocity = (destination.X - self.X) / ROCKET_MOVING_TIME

    def moving(self):
        if self.time == 0:
            self.rocket_state = RocketState.EXPLODE
            return
        self.Y += self.y_velocity
        self.X += self.x_velocity
        self.time -= 1

    def explode(self, explode_image, screen):
        screen.blit(explode_image, (self.X, self.Y))
        self.rocket_state = RocketState.RELOADING

    def ready(self):
        self.rocket_state = RocketState.READY
