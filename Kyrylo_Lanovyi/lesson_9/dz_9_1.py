class Auto():

    def __init__(self, mark, color, volume):
        self.mark = mark
        self.color = color
        self.volume = volume

    def forward(self):
        return '{} {} is going forward'.format(self.color, self.mark)

    def backward(self):
        return '{} {} is going back'.format(self.color, self.mark)

class Car(Auto):

    def left(self):
        return '{} {} is going left'.format(self.color, self.mark)

    def right(self):
        return '{} {} is going right'.format(self.color, self.mark)

car1 = Auto('Volvo', 'White', '2.0')
print(car1.forward())
print(car1.backward())

car2 = Car('Renault', 'Red', '1.6')
print(car2.left())
print(car2.right())