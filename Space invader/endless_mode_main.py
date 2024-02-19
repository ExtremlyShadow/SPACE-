import sys

import pygame.time

from Endless_mode.endless_game_play import EndlessGamePlay
from entities.enemy_entity import Boss
from entities.player_entity import Player
from game.game_play import *
from const.value import *
from game.game_setting import GameSetting
from game.score import Score

pygame.init()
player1 = Player(PLAYER_IMAGE, INITIAL_PLAYER_X1, INITIAL_PLAYER_Y1, PLAYER_LIVES)
score = Score('Comic Sans MS', 40, (255, 255, 255))
boss = Boss(BOSS_IMAGE, BOSS_X, BOSS_Y, BOSS_HEALTH)
clock = pygame.time.Clock()


def main():
    game_setting = GameSetting(WIDTH, HEIGHT, BACKGROUND_IMAGE, PLAYER_IMAGE, CAPTION)
    game = EndlessGamePlay(game_setting, player1, score, boss)
    game.start()
    while game.state:
        pygame.key.set_repeat(True)
        clock.tick(FPS)
        game.render()
        game.next_state()

        pygame.display.update()

    pygame.quit()
    sys.exit(0)


main()
