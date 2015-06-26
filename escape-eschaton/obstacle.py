
# interface for Obstacle
class Obstacle:
    def move(self):
        raise NotImplementedError()

    def block(self, pos):
        raise NotImplementedError()

class Asteroid(Obstacle):
    def __init__(self, offset, freq):
        self._angle = 360 / freq * offset
        self._velocity = 360.0 / freq

    def move(self):
        self._angle += self._velocity
        if self._angle >= 360.0:
            self._angle -= 360.0

    def block(self, ship):
        return int(self._angle) == ship.angle

    def __repr__(self):
        return "angle: %.1f, velocity: %.2f" % (self._angle, self._velocity)

class EschantonPlant(Obstacle):
    def __init__(self, velocity):
        self._radius = 0
        self._velocity = 1.0 / velocity

    def move(self):
        self._radius += self._velocity

    def block(Self, ship):
        return self._radius >= ship.raidus

    @property
    def radius(self):
        return int(self._radius)

    def __repr__(self):
        return 'Radius: %d, blast speed: %d' % (self.radius, self._velocity)
