# Example file showing a basic pygame "game loop"
import pygame
from pygame import Surface

# bg.png tamanho
W_BACK = 576
H_BACK = 324

# pygame setup
pygame.init()
print('setup start')
# criação de janela pygame
window: Surface = pygame.display.set_mode((W_BACK, H_BACK))

# carregar imagem e gerar uma superficie Surface
bg_surf: Surface = pygame.image.load("./asset/bg.png").convert_alpha()
player1: Surface = pygame.image.load("./asset/player1.png").convert_alpha()

# adicionar na tela(window)
window.blit(source=bg_surf, dest=(0, 0))
window.blit(source=player1, dest=(0, 160))

# Atualizar a janela
pygame.display.flip()

print('setup end')
print('loop start')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('loop end')
            pygame.quit()
            quit()
    pass
