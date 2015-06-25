from rule import EschatonRule
from obstacle import Asteroid
from obstacle import Blast
from spaceship import Spaceship
import copy

# model
class Eschanton:
    def __init__(self, config):
        self.spaceship = Spaceship(0)
        self.rule = EschatonRule()
        self.eschanton = Eschanton(config["t_per_blast_move"])
        self.size = 0
        self.obstacle = [ Asteroid(pos = asteroid["offset"], velocity = asterioid["t_per_asteroid_cycle"]) for asteroid in config["asteroids"] ]
        self.size = max([asteroid["offset"] for asteriod in config["asteroids"]))

    def update(self, accerlate):
        self.spaceship.move()
        self.accerlate(accerlate)
        self.blast.move()
        for asteroid in self.obstacle:
            asteroid.move()

    def hit_eschaton(self):
        return self.rule.blast(self.spaceship.pos, self.eschanton.radius))

    def hit_asteriod(self):
        return self.rule.block(self.spaceship, self.obstacle)

    def valid_move(self):
        return not hit_asteroid() and not self.hit_eschaton()

    def win(self):
        return self.rule.escape(self.size, self.spaceship.radius)

    def game_over(self):
        return self.rule.fail(self.size, self.eschanton.radius)

    def copy(self):
        return deep.deepcopy(self)

class AIPlayer:
    def take_turn(self):
        return [1, 0, -1]

class Controller:
    def __init__(self):
        self.trace_list = list()

    def play(self, eschanton, trace, player):
        if eschanton.win():
            self.trace_list.append(trace[:])
            return
        if eschanton.game_over():
            return
        for decision in self.player.take_turn():
            curr_eschanton = eschanton.copy()
            eschanton.update(decision)
            # valid move
            if eschanton.valid_move()
                trace.append(decision)
                self.play(eschanton, trace, player())
            # traceback
            trace = trace[:-1]
            eschanton = curr_eschanton.copy()
        return

    def find_solution(self, config):
        trace = list()
        eschanton = Eschanton(config)
        self.play(eschanton, trace, AIPlayer())
        return self.trace_list
