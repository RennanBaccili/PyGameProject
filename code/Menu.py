#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import WIN_W


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('./asset/menu_bg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        # inicio o som do menu
        pygame.mixer_music.load('./asset/menu_song.mp3')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.15)

        # imagem do menu
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", (255, 128, 0), ((WIN_W / 2), 70))
            pygame.display.flip()

    def menu_text(self,
                  text_size: int,
                  text: str,
                  text_color: tuple,
                  text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont("Lacida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
        # para atualizar a imagem, que no caso é texto criado
