#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background
from code.Const import WIN_W, IMAGE_LEVEL, WIN_H
from code.Player import Player


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position: tuple = (0, 0)):
        match entity_name:
            case level if level in IMAGE_LEVEL:
                list_bg = []
                for i in range(1, IMAGE_LEVEL[level]):
                    list_bg.append(Background(f'm1/{i}.png', position))
                    list_bg.append(Background(f'm1/{i}.png', (WIN_W, 0)))
                return list_bg
            case 'Player1':
                return Player(f'm1/player1.png', (10, WIN_H/2))

