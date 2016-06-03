class Iterator:
    def __init__(self):
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        number = self.number
        self.number += 1
        return number
