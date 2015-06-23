#! /usr/bin/python


class MathInterface:
    """Interface for proxy and real subject."""
    def add(self, x, y):
        raise NotImplementedError()

    def sub(self, x, y):
        raise NotImplementedError()

    def mul(self, x, y):
        raise NotImplementedError()

    def div(self, x, y):
        raise NotImplementedError()

class Math(MathInterface):
    """Real subject."""
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        return x / y

class Proxy(MathInterface):
    """Proxy."""
    def __init__(self):
        self.math = Math()

    def add(self, x, y):
        return self.math.add(x, y)

    def sub(self, x, y):
        return self.math.sub(x, y)

    def mul(self, x, y):
        return self.math.mul(x, y)

    def div(self, x, y):
        if y == 0:
            return float('inf')
        return self.math.div(x, y)

def main():
    p = Proxy()
    x, y = 4, 2
    print '4 + 2 = ' + str(p.add(x, y))
    print '4 - 2 = ' + str(p.sub(x, y))
    print '4 * 2 = ' + str(p.mul(x, y))
    print '4 / 2 = ' + str(p.div(x, y))

if __name__ == "__main__":
    main()
