import random

from const import *
from entity import Enemy

var = [Enemy(
    ENEMY_IMAGE,
    random.randint(WIDTH - MAX_X, WIDTH - MIN_X),
    random.randint(HEIGHT - MAX_Y, HEIGHT - MIN_Y),
    random.randint(MIN_HEALTH, MAX_HEALTH)
), Enemy(
    ENEMY_IMAGE,
    random.randint(WIDTH - MAX_X, WIDTH - MIN_X),
    random.randint(HEIGHT - MAX_Y, HEIGHT - MIN_Y),
    random.randint(MIN_HEALTH, MAX_HEALTH)
)]

print(len(var))
for i in var:
    print(i.X)