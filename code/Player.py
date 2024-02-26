#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Entity import Entity


class Player(Entity):
    def __init__(self, name, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_w]:
            self.rect.centery -= 1
        if pressed_key[pygame.K_s]:
            self.rect.centery += 1
        if pressed_key[pygame.K_d]:
            self.rect.centerx += 1
        if pressed_key[pygame.K_a]:
            self.rect.centerx -= 1
            pass
        pass
