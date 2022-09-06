from pygame.locals import *


class KeyBinds:
    UP = K_UP
    DOWN = K_DOWN
    RIGHT = K_RIGHT
    LEFT = K_LEFT


class Config:
    SCALAR = 7
    SCREEN_WIDTH = 160 * SCALAR
    SCREEN_HEIGHT = 144 * SCALAR
    SCREEN_COLOUR = (255, 255, 255)

    STATIC_SURFACES = (
    {"SIZE": (46 * SCALAR, 4 * SCALAR), "POSITION": (0 * SCALAR, 42 * SCALAR), "COLOUR": (41, 89, 123)},
    {"SIZE": (46 * SCALAR, 4 * SCALAR), "POSITION": (114 * SCALAR, 42 * SCALAR), "COLOUR": (41, 89, 123)},
    {"SIZE": (46 * SCALAR, 4 * SCALAR), "POSITION": (0 * SCALAR, 106 * SCALAR), "COLOUR": (41, 89, 123)},
    {"SIZE": (46 * SCALAR, 4 * SCALAR), "POSITION": (114 * SCALAR, 106 * SCALAR), "COLOUR": (41, 89, 123)},
    {"SIZE": (28 * SCALAR, 4 * SCALAR), "POSITION": (66 * SCALAR, 42 * SCALAR), "COLOUR": (41, 89, 123)},
    {"SIZE": (28 * SCALAR, 4 * SCALAR), "POSITION": (66 * SCALAR, 106 * SCALAR), "COLOUR": (41, 89, 123)})

    STATIC_IMAGES = [{"SIZE": (160 * SCALAR, 34 * SCALAR), "POSITION": (0 * SCALAR, 46 * SCALAR),
                      "IMAGE": "sprites/background.png"},
                     {"SIZE": (160 * SCALAR, 34 * SCALAR), "POSITION": (0 * SCALAR, 110 * SCALAR),
                      "IMAGE": "sprites/background.png"}]

    PLAYER_SIZE = (18 * SCALAR, 3 * SCALAR)
    PLAYER_COLOUR = (0, 0, 0)
    PLAYER_VALID_X = (47 * SCALAR, 95 * SCALAR)
    PLAYER_VALID_Y = (42 * SCALAR, 106 * SCALAR)

    WALKER_SIZE = (14 * SCALAR, 16 * SCALAR)
    WALKER_DATA = ({"POSITION": (-14 * SCALAR, 26 * SCALAR), "DIRECTION": 1},
                   {"POSITION": (160 * SCALAR, 26 * SCALAR), "DIRECTION": -1},
                   {"POSITION": (-14 * SCALAR, 90 * SCALAR), "DIRECTION": 1},
                   {"POSITION": (160 * SCALAR, 90 * SCALAR), "DIRECTION": -1})
    WALKER_SPEED_X = 0.1 * SCALAR
    WALKER_SPEED_Y = -0.05 * SCALAR
    WALKER_JUMP_DISTANCE = 5 * SCALAR
