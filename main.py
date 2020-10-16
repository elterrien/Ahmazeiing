#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
pygame.init()
from game import Game

# 1 Setting the scene
# open window
pygame.display.set_caption("Aaahmazeiiing !")
screen = pygame.display.set_mode((600, 600))

# load the maze frame
background = pygame.image.load('ressource/maze.png')

# load game
game = Game()

# display the maze frame
frame = True

# A while loop to keep the window open and up to date (So called "game loop")
while frame:

    # load background
    screen.blit(background, (0,0))

    # load badguy
    screen.blit(game.badguy.image, game.badguy.rect)

    # load hero
    screen.blit(game.hero.image, game.hero.rect)

    # check hero movement
    if game.pressed.get(pygame.K_RIGHT):
        game.hero.move_right()
    elif game.pressed.get(pygame.K_LEFT):
        game.hero.move_left()
    elif game.pressed.get(pygame.K_DOWN):
        game.hero.move_down()
    elif game.pressed.get(pygame.K_UP):
        game.hero.move_up()

    # Update the screen
    pygame.display.flip()

    # if the player close the window
    for event in pygame.event.get():
        # event being closure of the window
        if event.type == pygame.QUIT:
            frame = False
            pygame.quit()
        # enabling hero movement by checking if key is released
        elif event.type == pygame.KEYDOWN:
           game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
           game.pressed[event.key] = False