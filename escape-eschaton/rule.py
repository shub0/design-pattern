class Rule:
    def blast(self, ship_pos, radius):
        raise NotImplemented()

    def block(self, ship_pos, obstacle):
        raise NotImplemented()

    def win(self, size, pos):
        raise NotImplemented()

    def fail(self, max_size, curr_size):
        raise NotImplemented()

    def valid(self, ship, obstacles, curr_size):
        raise NotImplemented()

class EscapeEschatonRule(Rule):
    def _blast(self, ship_pos, eschaton_radius):
        return eschaton_radius >= ship_pos

    def _block(self, ship, obstacles):
        # design a binary search instead of linear search
        if any( [asteroid.block(ship) for asteroid in obstacles] ):
            return True
        return False

    def escape(self, size, ship_pos):
        return ship_pos > size

    def fail(self, max_size, curr_size):
        return curr_size >= max_size

    def valid(self, spaceship, obstacles, eschanton_radius):
        # not hit asteriod/not destoried by blast/not hit escanton
        return not self._block(spaceship, obstacles) and not self._blast(spaceship.radius, eschanton_radius) and not self._blast(spaceship.pos, 0)
