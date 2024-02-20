import random

import pygame
import sys

pygame.init()

Enemy_images = ['image/Alien1.png', 'image/Alien2.png', 'image/Alien3.png', 'image/Alien4.png',
                'image/Alien5.png']
resized_width = 800
resized_height = 600
Y = 10
    # Load the original image
random_enemy_image = random.choice(Enemy_images)
original_image = pygame.image.load(random_enemy_image)
resized_image = pygame.transform.scale(original_image, (32, 32))

    # Set up the Pygame window
screen = pygame.display.set_mode((resized_width, resized_height))
pygame.display.set_caption('Resized Enemy Image')

    # Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Display the resized image
    for i in range(len(Enemy_images)):
        Y += i*10
    screen.blit(resized_image, (0, Y))
    pygame.display.flip()
