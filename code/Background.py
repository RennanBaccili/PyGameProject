#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Entity import Entity


class Background(Entity):
    def __init__(self, name, position: tuple):
        super().__init__(name, position)

    def move(self):
        pass
