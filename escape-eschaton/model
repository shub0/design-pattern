from rule import EschatonRule
from obstacle import Asteroid
from obstacle import Blast
from spaceship import Spaceship
import copy

# model
class EscapeEschanton:
    def __init__(self, rule, player, config):
        self.spaceship = Spaceship(0)
        self.obstacle = list()
        self.blast = Blast(config["t_per_blast_move"])
        for asteroid in config["asteroids"]:
            self.obstacle.append(Asteroid(pos = asteroid["offset"], velocity = asterioid["t_per_asteroid_cycle"]))

    def update(self):
        self.blast.move()
        for asteroid in self.obstacle:
            asteroid.move()

    def copy(self):
        return deep.deepcopy(self)
