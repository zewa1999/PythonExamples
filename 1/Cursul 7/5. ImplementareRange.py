class GeneratorulMeu():
    current = 0

    def __init__(self, primul, ultimul):
        self.primul = primul
        self.ultimul = ultimul

    def __iter__(self):
        return self

    def __next__(self):
        if GeneratorulMeu.current < self.ultimul:
            numar = GeneratorulMeu.current
            GeneratorulMeu.current+=1
            return numar
        raise StopIteration

gen = GeneratorulMeu(0, 100)
for i in gen:
    print(i)