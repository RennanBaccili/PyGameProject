#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_W, IMAGE_LEVEL, WIN_H
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position: tuple = (0, 0)):
        match entity_name:
            case level if level in IMAGE_LEVEL:
                list_bg = []
                for i in range(1, IMAGE_LEVEL[level]):
                    list_bg.append(Background(f'levels/m1/{i}.png', position))
                    list_bg.append(Background(f'levels/m1/{i}.png', (WIN_W, 0)))
                return list_bg
            case 'Player1':
                return Player(f'players/player1.png', (10, WIN_H / 2))
            case 'Player2':
                return Player(f'players/player2.png', (10, WIN_H / 1.5))
            case 'Enemy1':
                return Enemy(f'enemy/enemy1.png', (WIN_W + 40, random.randint(0,  WIN_H -40)))
            case 'Enemy2':
                return Enemy(f'enemy/enemy2.png', (WIN_W + 40, random.randint(0, WIN_H -40)))
