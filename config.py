from pygame.locals import *


class KeyBinds:
    UP = K_UP
    DOWN = K_DOWN
    RIGHT = K_RIGHT
    LEFT = K_LEFT


class Config:
    SCALAR = 4
    SCREEN_WIDTH = 160 * SCALAR
    SCREEN_HEIGHT = 144 * SCALAR
    SCREEN_COLOUR = (255, 255, 255)

    FLOOR_LONG = (46 * SCALAR, 4 * SCALAR)
    FLOOR_LONG_POSITIONS = ((0 * SCALAR, 42 * SCALAR), (114 * SCALAR, 42 * SCALAR),
                            (0 * SCALAR, 106 * SCALAR), (114 * SCALAR, 106 * SCALAR))
    FLOOR_SHORT = (28 * SCALAR, 4 * SCALAR)
    FLOOR_SHORT_POSITIONS = ((66 * SCALAR, 42*SCALAR), (66 * SCALAR, 106 * SCALAR))

    BACKGROUND_TOP = {}
    BACKGROUND_BOTTOM = {}

    PLAYER_SIZE = (18 * SCALAR, 3 * SCALAR)
    PLAYER_COLOUR = (255, 128, 128)
    PLAYER_VALID_X = (47 * SCALAR, 95 * SCALAR)
    PLAYER_VALID_Y = (42 * SCALAR, 106 * SCALAR)