class Spaceship:
    def __init__(self, radius=0, angle=0):
        self._radius   = radius
        self._velocity = 0
        self._angle    = angle

    def move(self):
        self._radius += self._velocity

    def accerlate(self, accerlate):
        self._velocity += accerlate

    @property
    def radius(self):
        return self._radius

    @property
    def angle(self):
        return self._angle

    def __repr__(self):
        return "Raidus: %d, speed: %d" % (self.radius, self._velocity)
