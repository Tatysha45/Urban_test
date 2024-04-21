class EvenNumbers():
    def __init__(self, start=10, end=25):
        self.start = start if start % 2 == 0 else start + 1
        self.end = end

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        result = self.current
        self.current += 2
        return result

en = EvenNumbers(10,25)
for i in en:
    print(i)
