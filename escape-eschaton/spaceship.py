class Spaceship:
    def __init__(self):
        self.pos = 0
        self.velocity = 0

    def move(self):
        self.pos += self.velocity

    def accerlate(self, accerlate):
        self.velocity += accerlate
