import pygame
from pygame.font import Font


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
