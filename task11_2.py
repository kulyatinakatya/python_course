class Figure:

    def __init__(self):
        self.color = 'White'

    def change_color(self, new_color):
        self.color = new_color
        print('New color is', self.color)

    def figure_info(self):
        pass


class Oval(Figure):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def figure_info(self):
        print('it is an oval!', 'one axis =', self.a, 'another axis =', self.b, 'color =', self.color)


class Square(Figure):
    def __init__(self, a):
        super().__init__()
        self.a = a

    def figure_info(self):
        print('it is a square!', 'side size =', self.a, 'color =', self.color)


ov = Oval(5, 8)
ov.figure_info()
ov.change_color('Black')
ov.figure_info()
sq = Square(7)
sq.figure_info()