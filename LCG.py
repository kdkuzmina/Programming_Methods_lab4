class LinearCongruentialGenerator:
    def __init__(self, seed):
        self.seed = seed
        self.a = 2862933555777941757
        self.c = 3037000493
        self.m = 2 ** 48

    def generate(self, n):
        numbers = []
        for _ in range(n):
            self.seed = (self.a * self.seed + self.c) % self.m
            numbers.append(self.seed / self.m)
        return numbers


