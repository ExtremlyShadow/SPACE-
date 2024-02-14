import pygame.image

ENEMY_IMAGE = 'Enemy.png'
BULLET_IMAGE = 'Bullet.png'
PLAYER_IMAGE = 'Player.png'
ROCKET_IMAGE = 'rocket.png'
EXPLOSION_IMAGE = 'explosion.png'
BACKGROUND_IMAGE = 'background.png'
DEAD_IMAGE = pygame.image.load('explosion.png')
ENEMY_BULLET_IMAGE = 'enemy_bullet.png'

WIDTH = 800
HEIGHT = 600
MIN_X = 0
MAX_X = 750
MIN_Y = 400
MAX_Y = 600
PLAYER_MIN_Y = 0

COMMON_BULLET_DAMAGE = 1
MIN_HEALTH = 2
MAX_HEALTH = 4

INITIAL_PLAYER_X = 400
INITIAL_PLAYER_Y = 200
PLAYER_HEALTH = 5

CAPTION = 'Test'
