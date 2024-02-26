#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import WIN_W, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        # inicia a janela e a imagem
        self.window: Surface = window
        self.surf = pygame.image.load('./asset/menu_bg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        # som menu
        pygame.mixer_music.load('./asset/menu_song.mp3')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.15)

        # variable de escopo
        menu_option = 0

        while True:
            # Menu itens
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(70, "Mountain", COLOR_ORANGE, ((WIN_W / 2), 60))
            self.menu_text(60, "Shooter", COLOR_ORANGE, ((WIN_W / 2), 110))
            for i in range(len(MENU_OPTION)):
                if menu_option == i:
                    self.menu_text(25, MENU_OPTION[i], COLOR_YELLOW, ((WIN_W / 2), 170 + 35 * i))
                else:
                    self.menu_text(25, MENU_OPTION[i], COLOR_WHITE, ((WIN_W / 2), 170 + 35 * i))


            # Eventos de tela
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    #Movimento de seleção de item
                    if event.key == pygame.K_DOWN and menu_option < len(MENU_OPTION):
                        menu_option += 1
                    if event.key == pygame.K_UP and menu_option > 0:
                        menu_option -= 1

                    # Eventos Kit
                    if event.key == pygame.K_RETURN and menu_option == 3:
                        pygame.quit()
                        quit()

                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]
                pygame.display.flip()
            pass

    # menu_text, função para criar imagens a partir de texto
    def menu_text(self,
                  text_size: int,
                  text: str,
                  text_color: tuple,
                  text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont("Lacida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
        # para atualizar a imagem, que no caso é texto criado
