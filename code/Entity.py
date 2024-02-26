#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image


# Para transformar ela em uma classe abstrata
class Entity(ABC):
    def __init__(self, name, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name).convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self):
        pass
