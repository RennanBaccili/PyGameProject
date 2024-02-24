# Example file showing a basic pygame "game loop"
import pygame
from pygame import Surface, Rect

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

# obter rertangulo a patir da superficie, para movimentala
bg_rect: Rect = bg_surf.get_rect(left=0, top=0)
player1_rect: Rect = player1.get_rect(left=0, top=100)

# adicionar na tela(window)
window.blit(source=bg_surf, dest=bg_rect)
window.blit(source=player1, dest=player1_rect)

# Atualizar a janela
pygame.display.flip()

print('setup end')

# Colocar um relógio no jogo
clock = pygame.time.Clock()

print('loop start')
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('loop end')
            pygame.quit()
            quit()

    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_w]:
        player1_rect.centery -= 1
        window.blit(source=bg_surf, dest=bg_rect)
        window.blit(source=player1, dest=player1_rect)
        pygame.display.flip()
        pass
    pass
