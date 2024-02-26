#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, menu_option):
        self.name = name
        self.window: Surface = window
        self.mode = menu_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))

    def run(self, ):
        # musica
        pygame.mixer_music.load('./asset/levels/m1/f1.mp3')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.15)
        # relógio
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                self.level_text(20, f'FPS {clock.get_fps():.0f}', COLOR_WHITE, (550, 10))
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
        pass

    def level_text(self,
                   text_size: int,
                   text: str,
                   text_color: tuple,
                   text_pos: tuple):
        text_font: Font = pygame.font.SysFont("Lacida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)
        # para atualizar a imagem, que no caso é texto criado
