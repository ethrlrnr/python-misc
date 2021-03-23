class RightTriangle:
    def __init__(self, opposite, adjacent):
        self.opposite = opposite
        self.adjacent = adjacent

    def find_hypotenuse(self):
        return (self.opposite**2 + self.adjacent**2)**0.5
