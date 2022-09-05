import pygame

from pygame import display, Surface
from pygame.sprite import Sprite
from config import KeyBinds, Config

pygame.init()
game_display = display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT), pygame.RESIZABLE)
vec = pygame.math.Vector2
frames_per_second = pygame.time.Clock()


class GameObject(Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rectangle = self.image.get_rect()
        self.rectangle.topleft = vec(position)

    def draw(self):
        return self.image, self.rectangle


class Player(GameObject):
    def __init__(self):
        image = Surface(Config.PLAYER_SIZE)
        image.fill(Config.PLAYER_COLOUR)
        super().__init__(image, (Config.PLAYER_VALID_X[0], Config.PLAYER_VALID_Y[0]))


class Walker:
    def __init__(self, position, velocity):
        self.position = vec(position)
        self.velocity = vec(velocity)


class Environment:
    def __init__(self):
        self.static = self.create_static()
        self.games = {}

    @staticmethod
    def create_static():
        static = []
        return []

    def add_object(self, genome_id):
        self.games[genome_id] = {"player": Player(), "walkers": []}

    def get_keys(self):
        keys = pygame.key.get_pressed()
        self.update(list(self.games.keys())[0], keys)

    def update(self, game_id, keys):
        game = self.games[game_id]
        player = game["player"]
        if keys[KeyBinds.DOWN] > 0.5:
            coordinate = player.rectangle.top + 64 * Config.SCALAR
            player.rectangle.top = coordinate if coordinate in Config.PLAYER_VALID_Y else player.rectangle.top
        if keys[KeyBinds.UP] > 0.5:
            coordinate = player.rectangle.top - 64 * Config.SCALAR
            player.rectangle.top = coordinate if coordinate in Config.PLAYER_VALID_Y else player.rectangle.top
        if keys[KeyBinds.LEFT] > 0.5:
            coordinate = player.rectangle.left - 48 * Config.SCALAR
            player.rectangle.left = coordinate if coordinate in Config.PLAYER_VALID_X else player.rectangle.left
        if keys[KeyBinds.RIGHT] > 0.5:
            coordinate = player.rectangle.left + 48 * Config.SCALAR
            player.rectangle.left = coordinate if coordinate in Config.PLAYER_VALID_X else player.rectangle.left

    def render_environment(self):
        game_display.fill(Config.SCREEN_COLOUR)
        for game_object in self.static:
            game_display.blit(*game_object.draw())
        for game in self.games.values():
            player = game["player"]
            game_display.blit(*player.draw())
        display.update()


if __name__ == "__main__":
    environment = Environment()
    environment.add_object("magic")
    while True:
        environment.render_environment()
        environment.get_keys()
        pygame.event.pump()
        frames_per_second.tick(60)