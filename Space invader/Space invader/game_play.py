import random
import pygame
from typing import List

from entities.entity import Position
from entities.enemy_entity import Enemy, Egg
from entities.player_entity import Player, Bullet, Rocket
from const.state import *
from const.value import *
from game_setting import GameSetting


class GamePlay:
    enemies: List[Enemy] = []
    bullets: List[Bullet] = []
    eggs: List[Egg] = []
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

    def enemy_spawn_egg(self):
        for enemy in self.enemies:
            if enemy.enemy_state == EnemyState.ALIVE:
                egg = Egg(EGG_IMAGE, enemy.X, enemy.Y)
                self.eggs.append(egg)

    def update_eggs(self):
        for egg in self.eggs:
            egg.reload()
            if egg.egg_state == EggState.FLYING:
                egg.fall(self.game_setting.screen, Position(egg.X, HEIGHT - PLAYER_MIN_Y))

    def fire(self):
        bullet = Bullet(BULLET_IMAGE, self.player.X, self.player.Y)
        bullet.fire(self.game_setting.screen, Position(self.player.X, HEIGHT - MAX_Y))
        self.bullets.append(bullet)

    def handle_impact(self):
        for bullet in self.bullets:
            for enemy in self.enemies:
                if (enemy.X < bullet.X < enemy.X + enemy.size
                        and enemy.Y < bullet.Y < enemy.Y + enemy.size
                        and bullet.bullet_state != BulletState.INVISIBLE):
                    bullet.hit()
                    enemy.hit(COMMON_BULLET_DAMAGE)
                if enemy.health == 0:
                    enemy.dead(DEAD_IMAGE, self.game_setting.screen)

    def clear_bullet(self):
        for bullet in self.bullets:
            if bullet.bullet_state == BulletState.INVISIBLE:
                del bullet

    def clear_egg(self):
        for egg in self.eggs:
            if egg.egg_state == EggState.INVISIBLE:
                del egg

    def start(self):
        self.state = True
        self.generate_enemy(6)

    def render(self):
        self.game_setting.screen.blit(self.game_setting.background, (0, 0))
        self.player.draw(self.game_setting.screen)
        self.enemy_spawn_egg()
        self.update_eggs()
        for enemy in self.enemies:
            if enemy.enemy_state == EnemyState.ALIVE:
                enemy.draw(self.game_setting.screen)
        for egg in self.eggs:
            if egg.egg_state == EggState.FLYING:
                egg.draw(self.game_setting.screen)
        for bullet in self.bullets:
            if bullet.bullet_state == BulletState.FLYING:
                bullet.draw(self.game_setting.screen)

    def next_state(self):
        self.handle_impact()
        self.clear_bullet()
        self.clear_egg()

        for bullet in self.bullets:
            if bullet.bullet_state == BulletState.FLYING:
                bullet.moving()

        for enemy in self.enemies:
            if enemy.enemy_state == EnemyState.ALIVE:
                enemy.moving()

        for egg in self.eggs:
            egg.moving()
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
