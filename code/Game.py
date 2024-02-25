#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame


from code.Menu import Menu
from code.Const import WIN_H, WIN_W


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_W, WIN_H))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu.run()
