#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Level import Level
from code.Menu import Menu
from code.Const import WIN_H, WIN_W, MENU_OPTION


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_W, WIN_H))

    def run(self):
        while True:

            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, 'level1', menu_return)
                level.run()
