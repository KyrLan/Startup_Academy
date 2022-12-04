class Parallelogram:

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        s = self.width * self.length
        return s

class Square(Parallelogram):
    def get_area(self):
        s = self.width*2
        return s
