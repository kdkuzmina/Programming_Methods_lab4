class MultiplicativeCongruentialGenerator:
    def __init__(self, seed):
        self.seed = seed
        self.a = 6364136223846793005
        self.m = 2 ** 64

    def generate(self, n):
        numbers = []
        for _ in range(n):
            self.seed = (self.a * self.seed) % self.m
            numbers.append(self.seed / self.m)
        return numbers
