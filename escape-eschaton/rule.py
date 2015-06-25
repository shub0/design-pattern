class Rule:
    def blast(self, ship_pos, radius):
        raise NotImplemented()

    def block(self, ship_pos, obstacle):
        raise NotImplemented()

    def win(self, size, pos):
        raise NotImplemented()

class EschatonRule(Rule):
    def blast(self, ship_pos, eschaton_radius):
        return ship_pos > eschaton_radius

    def block(self, ship, obstacles):
        # design a binary search instead of linear search
        if any( [asteroid.block(ship) for asteroid in obstacles] ):
            return True
        return False

    def escape(self, size, ship_pos):
        return ship_pos > size

    def fail(self, max_size, curr_size):
        return curr_size >= max_size
