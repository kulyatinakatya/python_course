class Dog:
    def __init__(self, dogsname, is_hungry):
        self.dogsname = dogsname
        self.is_hungry = is_hungry


class Human:
    def __init__(self, humansname, dogsname):
        self.humansname = humansname
        self.dogsname = dogsname

    def get_food(self, dog: Dog):
        if dog.is_hungry == True:
            dog.is_hungry = False


Bobby = Dog('Bobby', True)
Bob = Human('Bob', 'Bobby')
print('Before work of function: Is the dog hungry? ', Bobby.is_hungry)
Bob.get_food(Bobby)
print('After: Is the dog hungry? ', Bobby.is_hungry)
