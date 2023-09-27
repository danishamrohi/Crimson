import pygame
import pygame_menu
import json
import random
import math
import sys

import Character
import UI

pygame.init()
clock = pygame.time.Clock()
surface = pygame.display.set_mode((600, 400))

player_idle = [
                pygame.image.load("./sprites/player/idle/00.png"),
                pygame.image.load("./sprites/player/idle/01.png"),
                pygame.image.load("./sprites/player/idle/02.png"),
                pygame.image.load("./sprites/player/idle/03.png")
              ]

player_attack = [
                pygame.image.load("./sprites/player/attack/00.png"),
                pygame.image.load("./sprites/player/attack/01.png"),
                pygame.image.load("./sprites/player/attack/02.png"),
                pygame.image.load("./sprites/player/attack/03.png")
              ]

def start_the_game():
    menu.disable()
    player = Character.Character(50, 50, player_idle, player_attack)
    moving_sprites = pygame.sprite.Group()
    moving_sprites.add(player)
    attack_button = UI.Button(200, 200, 100, 50, "Attack", (0, 255, 0))
    name_label = UI.Label(300, 300, "Bob")
    while True:
        for event in pygame.event.get():
            mouse_position = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if attack_button.on_button(mouse_position):
                    player.attack()
        surface.fill((0,0,0))
        attack_button.draw(surface)
        name_label.draw(surface)
        moving_sprites.draw(surface)
        moving_sprites.update()
        pygame.display.update()
        clock.tick(10)

menu = pygame_menu.Menu("", 600, 400)

menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)
