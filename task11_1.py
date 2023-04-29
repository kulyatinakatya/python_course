class Table:

    def __init__(self, l, w, h):
        self.long = l
        self.width = w
        self.height = h

    def outing(self):
        print(self.long, self.width, self.height)


class Kitchen(Table):

    def howplaces(self, n):
        if n < 2:
            print("It is not kitchen table")
        else:
            self.places = n

    def outplaces(self):
        print(self.places)


class Design(Table):

    def put_flowers(self):
        if (self.long*self.width) > 2:
            print('flowers on the table!')

    def choiceofchairs(self):
        print('suitable chair height = ', self.height-0.2)



ex = Design(4, 1, 0.5)
ex.put_flowers()
ex.choiceofchairs()

