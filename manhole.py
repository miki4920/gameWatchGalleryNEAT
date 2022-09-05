import pygame

from pygame import display, Surface
from config import KeyBinds, Config

pygame.init()
game_display = display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT), pygame.RESIZABLE)
vec = pygame.math.Vector2
frames_per_second = pygame.time.Clock()


class GameObject:
    def __init__(self, size, colour, position):
        self.surface = Surface(vec(size))
        self.surface.fill(colour)
        self.rectangle = self.surface.get_rect()
        self.rectangle.midtop = vec(position)

    def draw(self):
        return self.surface, self.rectangle


class Player(GameObject):
    def __init__(self):
        super().__init__(Config.PLAYER_SIZE, Config.PLAYER_COLOUR, (50, 50))


class Walker:
    def __init__(self, position, velocity):
        self.position = vec(position)
        self.velocity = vec(velocity)


class Environment:
    def __init__(self):
        self.games = {}

    def add_object(self, genome_id):
        self.games[genome_id] = {"player": Player(), "walkers": []}

    def get_keys(self):
        keys = pygame.key.get_pressed()
        self.update(list(self.games.keys())[0], keys)

    def update(self, game_id, keys):
        game = self.games[game_id]
        player = game["player"]
        if keys[KeyBinds.DOWN] > 0.5:
            player.y = 1
        if keys[KeyBinds.UP] > 0.5:
            player.y = 0
        if keys[KeyBinds.LEFT] > 0.5:
            player.x = 0
        if keys[KeyBinds.RIGHT] > 0.5:
            player.x = 1

    def render_environment(self):
        game_display.fill((0, 0, 0))
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