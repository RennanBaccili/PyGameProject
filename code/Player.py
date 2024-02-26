#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_W, WIN_H, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.centery > 20:
            self.rect.centery -= 2
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.centery < WIN_H -20:
            self.rect.centery += 2
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.centerx < WIN_W -30:
            self.rect.centerx += 2
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.centerx > 30:
            self.rect.centerx -= 2
            pass

