#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Entity import Entity


class Level:
    def __init__(self, window, name, menu_option):
        self.name = name
        self.window = window
        self.mode = menu_option
        self.entity_list: list[Entity] = []

    def run(self):
        print('fase 1')
        pass
