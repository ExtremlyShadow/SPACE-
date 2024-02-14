import random
from typing import List

import pygame
from pygame.font import Font

from const import *
from entity import *
from state import *


class Score:
    score: int
    font: Font
    color: str
    X: float
    Y: float

    def __init__(self, font, size, color):
        self.score = 0
        self.font = pygame.font.Font(font, size)
        self.color = color
        self.X = 10
        self.Y = 10

    def draw(self, screen):
        score = self.font.render("Score: " + str(self.score), True, self.color)
        screen.blit(score, (self.X, self.Y))


class GameSetting:
    def __init__(self, width, height, bg_image, icon_image, caption):
        self.screen = pygame.display.set_mode((width, height))
        self.background = pygame.image.load(bg_image)
        self.background = pygame.transform.scale(self.background, (width, height))
        self.screen.blit(self.background, (0, 0))
        pygame.display.set_icon(pygame.image.load(icon_image))
        pygame.display.set_caption(caption)


class GamePlay:
    enemies: List[Enemy] = []
    bullets: List[Bullet] = []
    enemy_bullets: List[Enemy_Bullet] = []
    game_setting: GameSetting
    player: Player
    rockets: List[Rocket] = []
    state: bool = False

    def __init__(self, game_setting, player, rocket):
        self.game_setting = game_setting
        self.player = player
        self.rockets.append(rocket)

    def generate_enemy(self, num_of_enemies):
        for i in range(num_of_enemies):
            self.enemies.append(Enemy(
                ENEMY_IMAGE,
                random.randint(MIN_X, MAX_X),
                random.randint(MIN_Y, MAX_Y),
                random.randint(MIN_HEALTH, MAX_HEALTH)
            ))

    def enemy_fire(self):
        for enemy in self.enemies:
            enemy_bullet = Enemy_Bullet(ENEMY_BULLET_IMAGE, enemy.X, enemy.Y)
            enemy_bullet.fire(self.game_setting.screen, Position(enemy_bullet.X, HEIGHT - PLAYER_MIN_Y))
            self.enemy_bullets.append(enemy_bullet)

    def fire(self):
        bullet = Bullet(BULLET_IMAGE, self.player.X, self.player.Y)
        bullet.fire(self.game_setting.screen, Position(self.player.X, HEIGHT - MAX_Y))
        self.bullets.append(bullet)

    def handle_impact(self):
        for bullet in self.bullets:
            for enemy in self.enemies:
                if (enemy.X < bullet.X < enemy.X + enemy.size
                        and bullet.Y == enemy.Y
                        and bullet.bullet_state != BulletState.INVISIBLE):
                    bullet.hit()
                    enemy.hit(COMMON_BULLET_DAMAGE)
                if enemy.health == 0:
                    enemy.dead(DEAD_IMAGE, self.game_setting.screen)

    def clear_bullet(self):
        for bullet in self.bullets:
            if bullet.bullet_state == BulletState.INVISIBLE:
                del bullet

    def clear_enemy_bullet(self):
        for enemy_bullet in self.enemy_bullets:
            if enemy_bullet.bullet_state == BulletState.COOLDOWN or enemy_bullet.bullet_state == BulletState.INVISIBLE:
                del enemy_bullet

    def start(self):
        self.state = True
        self.generate_enemy(6)

    def render(self):
        self.game_setting.screen.blit(self.game_setting.background, (0, 0))
        self.player.draw(self.game_setting.screen, 32)
        self.enemy_fire()
        for enemy in self.enemies:
            if enemy.enemy_state == EnemyState.ALIVE:
                enemy.draw(self.game_setting.screen, 32)
        for bullet in self.bullets:
            if bullet.bullet_state == BulletState.FLYING:
                bullet.draw(self.game_setting.screen, 32)
        for enemy_bullet in self.enemy_bullets:
            if enemy_bullet.bullet_state == BulletState.FLYING:
                enemy_bullet.draw(self.game_setting.screen, 32)

    def next_state(self):
        self.handle_impact()
        self.clear_bullet()
        for enemy_bullet in self.enemy_bullets:
            if enemy_bullet.bullet_state == BulletState.FLYING:
                enemy_bullet.moving()

        for bullet in self.bullets:
            if bullet.bullet_state == BulletState.FLYING:
                bullet.moving()

        for enemy in self.enemies:
            if enemy.enemy_state == EnemyState.ALIVE:
                enemy.moving()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.moving_left()
                if event.key == pygame.K_RIGHT:
                    self.player.moving_right()
                if event.key == pygame.K_UP:
                    self.player.moving_up()
                if event.key == pygame.K_DOWN:
                    self.player.moving_down()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_buttons = pygame.mouse.get_pressed()
                if mouse_buttons[0]:
                    self.fire()
