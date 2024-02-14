import sys

import pygame

from helper import *
from const import *

pygame.init()
player = Player(PLAYER_IMAGE, INITIAL_PLAYER_X, INITIAL_PLAYER_Y, PLAYER_HEALTH)
rocket = Rocket(ROCKET_IMAGE, 0, 0)


def main():
    game_setting = GameSetting(WIDTH, HEIGHT, BACKGROUND_IMAGE, PLAYER_IMAGE, CAPTION)
    game = GamePlay(game_setting, player, rocket)
    game.start()
    while game.state:
        pygame.key.set_repeat(True)
        game.render()
        game.next_state()

        pygame.display.update()

    pygame.quit()
    sys.exit(0)

main()
