class MyRangeIterator:
    def __init__(self, number):
        self.number = number
        self.index = -1

    def __next__(self):
        if self.index == self.number - 1:
            raise StopIteration()

        self.index += 1
        return self.index


class MyRange:
    def __init__(self, number=0):
        self.number = number

    def __iter__(self):
        return MyRangeIterator(self.number)


for i in MyRange(5):
    print(i)
