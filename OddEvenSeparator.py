class OddEvenSeparator:
    def __init__(self):
        self.l = []
        self.even = []
        self.odd = []

    def add_number(self, number):
        self.l.append(number)

    def even(self):
        for i in self.l:
            if i % 2 == 0:
                self.even.append(i)
        return self.even

    def odd(self):
        for i in self.l:
            if i % 2 != 0:
                self.odd.append(i)
        return self.odd
