#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position: tuple = (0, 0)):
        match entity_name:
            case 'Level1':
                list_bg = []
                for i in range(1, 5):
                    list_bg.append(Background(f'm1/{i}.png', position))
                return list_bg
