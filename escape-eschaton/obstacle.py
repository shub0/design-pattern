
# interface for Obstacle
class Obstacle:
    def move(self):
        raise NotImplementedError()

    def block(self, pos):
        raise NotImplementedError()

class Asteroid(Obstacle):
    def __init__(self, pos, velocity):
        self._pos = pos
        self._curr_pos = pos
        self._velocity = velocity

    def move(self):
        self._curr_pos += 1
        self._pos = (self._curr_pos % self._velocity)

    def block(self, pos):
        return self._curr_pos == pos

class Blast(Obstacle):
    def __init__(self, velocity):
        self._pos = 0
        self._micro_pos = 0
        self._velocity = velocity

    def move(self):
        self._micro_pos += 1
        self._pos = (self._micro_pos % self._velocity)

    def block(self, pos):
        return self._pos >= pos
