class Generator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self.generator()

    def generator(self):
        current = self.start
        while current <= self.end:
            yield current
            current += 1


gen = Generator(1, 111)

for num in gen:
    print(num)