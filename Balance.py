class Balance:
    def __init__(self):
        self.left = 0
        self.right = 0

    def add_right(self, right):
        self.right += right

    def add_left(self, left):
        self.left += left

    def result(self):
        if self.left == self.right:
            return '='
        if self.left > self.right:
            return 'L'
        if self.left < self.right:
            return 'R'
