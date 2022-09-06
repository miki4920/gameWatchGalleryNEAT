import pygame

from pygame import display, Surface
from pygame.image import load
from pygame.transform import flip, scale

from random import choice

from config import KeyBinds, Config

pygame.init()
game_display = display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
vec = pygame.math.Vector2
frames_per_second = pygame.time.Clock()


class GameObject:
    def __init__(self, image, position):
        self.image = image
        self.rectangle = self.image.get_rect()
        self.rectangle.topleft = position

    def draw(self):
        return self.image, self.rectangle


class Player(GameObject):
    def __init__(self):
        image = Surface(Config.PLAYER_SIZE)
        image.fill(Config.PLAYER_COLOUR)
        super().__init__(image, (Config.PLAYER_VALID_X[0], Config.PLAYER_VALID_Y[0]))


class Walker(GameObject):
    def __init__(self, walker_data):
        image = load("sprites/walker.png")
        image = scale(image, Config.WALKER_SIZE)
        if walker_data["DIRECTION"] == 1:
            image = flip(image, True, False)
        image.convert()
        super().__init__(image, (walker_data["POSITION"]))
        self.position = self.rectangle.topleft
        self.bottom_y = walker_data["POSITION"][1]
        self.top_y = self.bottom_y - Config.WALKER_JUMP_DISTANCE
        self.velocity = vec(Config.WALKER_SPEED_X * walker_data["DIRECTION"], Config.WALKER_SPEED_Y)

    def update(self):
        self.position = vec(self.position) + self.velocity
        if self.position.y < self.top_y:
            self.position.y = self.top_y
            self.velocity.y = -self.velocity.y
        elif self.position.y > self.bottom_y:
            self.position.y = self.bottom_y
            self.velocity.y = -self.velocity.y
        self.rectangle.topleft = self.position


class Environment:
    def __init__(self):
        self.static = self.create_static()
        self.games = {}

    @staticmethod
    def create_static():
        static = []
        for surface_data in Config.STATIC_SURFACES:
            surface = Surface(surface_data["SIZE"])
            surface.fill(surface_data["COLOUR"])
            static.append(GameObject(surface, surface_data["POSITION"]))
        for image_data in Config.STATIC_IMAGES:
            image = load(image_data["IMAGE"])
            image = scale(image, image_data["SIZE"])
            image.convert()
            static.append(GameObject(image, image_data["POSITION"]))
        return static

    def add_object(self, game_id):
        self.games[game_id] = {"player": Player(), "walkers": []}

    def get_keys(self):
        keys = pygame.key.get_pressed()
        self.update(list(self.games.keys())[0], keys)

    def add_walker(self, game_id):
        walker = Walker(choice(Config.WALKER_DATA))
        if len(self.games[game_id]["walkers"]) <= 2:
            self.games[game_id]["walkers"].append(walker)

    def update(self, game_id, keys):
        game = self.games[game_id]
        for walker in game["walkers"]:
            walker.update()
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
            for walker in game["walkers"]:
                game_display.blit(*walker.draw())
        display.update()


if __name__ == "__main__":
    environment = Environment()
    environment.add_object("magic")
    while True:
        environment.add_walker("magic")
        environment.render_environment()
        environment.get_keys()
        pygame.event.pump()
        frames_per_second.tick(50)