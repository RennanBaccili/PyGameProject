#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position: tuple):
        match entity_name:
            case 'Level1':
                return Background(f'm1/5.png', position)
