# sites
# https://craftpix.net/freebies/
# https://freesound.org/
# crtl alt l

# Example file showing a basic pygame "game loop"
import pygame
from pygame import Surface, Rect

# menu_bg.png tamanho
W_BACK = 576
H_BACK = 324

# pygame setup
pygame.init()
print('setup start')
# criação de janela pygame
window: Surface = pygame.display.set_mode((W_BACK, H_BACK))

# carregar imagem e gerar uma superficie Surface
bg_surf: Surface = pygame.image.load("../asset/menu_bg.png").convert_alpha()
player1: Surface = pygame.image.load("../asset/player1.png").convert_alpha()

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

# Carrregar musica e deixar ela tocando
pygame.mixer_music.load('../asset/fase1.mp3')
pygame.mixer_music.play(-1)
pygame.mixer_music.set_volume(0.15)

print('loop start')
while True:
    clock.tick(100)
    print(f'{clock.get_fps(): .0f}')
    # esse loop está acontecendo 30 vezes por segundo
    window.blit(source=bg_surf, dest=bg_rect)
    window.blit(source=player1, dest=player1_rect)
    pygame.display.flip()

    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_w]:
        player1_rect.centery -= 1
    if pressed_key[pygame.K_s]:
        player1_rect.centery += 1
    if pressed_key[pygame.K_d]:
        player1_rect.centerx += 1
    if pressed_key[pygame.K_a]:
        player1_rect.centerx -= 1
        pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('loop end')
            pygame.quit()
            quit()
    pass
