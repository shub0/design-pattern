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

    def block(self, ship_pos, obstacle):
        return obstacle.block(ship_pos)

    def escape(self, size, ship_pos):
        return ship_pos > size
