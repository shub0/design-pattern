
# interface for Obstacle
class Obstacle:
    def move(self):
        raise NotImplementedError()

    def block(self, pos):
        raise NotImplementedError()

class Asteroid(Obstacle):
    def __init__(self, offset, freq):
        self._radisu = offset
        self._curr_angle = 0
        self._velocity = 360.0 / freq

    def move(self):
        self._curr_angle += _velocity
        if self._curr_angle >= 360.0:
            self._curr_angle -= 360.0

    def block(self, ship):
        return self._raidus == ship.radius and self._curr_angle = ship.angle

class Eschanton:
    def __init__(self, velocity):
        self._radius = 0
        self._micro_pos = 0
        self._velocity = velocity

    def move(self):
        self._micro_pos += 1
        self._raidus = (self._micro_pos / self._velocity)

    @property
    def radius(self):
        return self._radius
