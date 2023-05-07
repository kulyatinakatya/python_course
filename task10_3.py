class Shape:
    def __init__(self, color, size):
        self.color = color
        self.size = size


class Triangle(Shape):
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def __repr__(self):
        return self.size+' '+self.color+' '+'triangle'


class Rectangle(Shape):
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def __repr__(self):
        return self.size+' '+self.color+' '+'rectangle'



box = [Triangle('red', 'big'), Rectangle('blue', 'small')]
box.append(Triangle('yellow', 'big'))
print(box)

print(isinstance(box[1], Triangle))