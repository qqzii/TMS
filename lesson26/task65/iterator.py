
def prostoe(x):
    count = 2
    b = True
    while count < x:
        if x % count == 0:
            b = False
        count += 1
    return b, x

class lazy_map:
    def __init__(self, fn, ls):
        self.fn = fn
        self.ls = ls
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx > len(self.ls):
            raise StopIteration()
        else:
            val = self.fn(self.ls[self.idx])
            self.idx += 1
            return val

def iterator(x):
    iterator = lazy_map(prostoe, range(1000000))
    for i in range(x):
        print(next(iterator))

iterator(6)
