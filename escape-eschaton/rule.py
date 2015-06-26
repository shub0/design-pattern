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
        if ship.radius >= len(obstacles):
            return False
        return obstacles[ship.radius].block(ship)

    def escape(self, size, ship_pos):
        return ship_pos >= size

    def fail(self, max_size, curr_size):
        return curr_size >= max_size

    def valid(self, spaceship, obstacles):
        # not destoried by blast/not hit escanton/not hit asteriod
        return not self._blast(spaceship.radius, obstacles[0].radius) and not self._blast(spaceship.radius, 0) and not self._block(spaceship, obstacles)
