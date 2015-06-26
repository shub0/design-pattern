from rule import EscapeEschatonRule
from obstacle import Asteroid
from obstacle import EschantonPlant
from spaceship import Spaceship
import copy

# model class
class Eschanton:
    def __init__(self, config):
        self.spaceship = Spaceship(0)
        self.rule = EscapeEschatonRule()
        self.eschanton = EschantonPlant(config["t_per_blast_move"])
        self.size = 0
        self.obstacle = [ Asteroid(offset = asteroid["offset"], freq = asteroid["t_per_asteroid_cycle"]) for asteroid in config["asteroids"] ]
        self.size = max( [ asteroid["offset"] for asteriod in config["asteroids"] ] )

    def update(self, accerlate):
        self.spaceship.move()
        self.spaceship.accerlate(accerlate)
        self.eschanton.move()
        for asteroid in self.obstacle:
            asteroid.move()

    def valid_move(self):
        return self.rule.valid(self.spaceship, self.obstacle, self.eschanton.radius)

    def win(self):
        return self.rule.escape(self.size, self.spaceship.radius)

    def game_over(self):
        return self.rule.fail(self.size, self.eschanton.radius)

    def copy(self):
        return copy.deepcopy(self)

# controller class
class AIPlayer:
    def take_turn(self):
        return [1, 0, -1]

class Game:
    def __init__(self):
        self.trace_list = list()
        self.player = AIPlayer()

    def escape(self, eschanton, trace):
        if eschanton.win():
            self.trace_list.append(trace[:])
            return
        if eschanton.game_over():
            return
        for decision in self.player.take_turn():
            curr_eschanton = eschanton.copy()
            eschanton.update(decision)
            # valid move
            if eschanton.valid_move():
                trace.append(decision)
                self.escape(eschanton, trace)
            # traceback
            trace = trace[:-1]
            eschanton = curr_eschanton.copy()
        return

    def find_solution(self, config):
        trace = list()
        eschanton = Eschanton(config)
        self.escape(eschanton, trace)
        return self.trace_list


if __name__ == '__main__':
    game = Game()
    config = {
        "t_per_blast_move": 10,
        "asteroids": [
            {
                "offset": 0,
                "t_per_asteroid_cycle": 2
            },
            {
                "offset": 1,
                "t_per_asteroid_cycle": 3
            },
            {
                "offset": 3,
                "t_per_asteroid_cycle": 4
            },
            {
                "offset": 1,
                "t_per_asteroid_cycle": 2
            }
        ]
    }
    print len(game.find_solution(config))
