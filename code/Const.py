# Colors
import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 128)

# Menu
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'EXIT')

# Tamanho
WIN_W = 576
WIN_H = 324

# i
IMAGE_LEVEL = {'Level1': 5}

# speed
ENTITY_SPEED = {'levels/m1/1.png': 0,
                'levels/m1/2.png': 1,
                'levels/m1/3.png': 2,
                'levels/m1/4.png': 3,
                'levels/m1/5.png': 4,
                }

PLAYER_KEY_UP = {'players/player1.png': pygame.K_UP,
                 'players/player2.png': pygame.K_w
                 }
PLAYER_KEY_DOWN = {'players/player1.png': pygame.K_DOWN,
                   'players/player2.png': pygame.K_s
                   }
PLAYER_KEY_LEFT = {'players/player1.png': pygame.K_LEFT,
                   'players/player2.png': pygame.K_a
                   }
PLAYER_KEY_RIGHT = {'players/player1.png': pygame.K_RIGHT,
                    'players/player2.png': pygame.K_d
                    }
