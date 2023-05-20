class Library:

    def __init__(self, author, title, num, holder=[]):
        self.author = author
        self.title = title
        self.__num_of_copies = num
        self.__holder = holder

    def __get_full_info(self, password):
        library_access = '123'
        if password == library_access:
            print('number of copies in the library:', self.__num_of_copies, '\n', 'holders:', self.__holder)
        else:
            print('Wrong password')

    def get_info(self):
        print('author:', self.author, '\n', 'title:', self.title)
        self.__get_full_info(input('Enter the password for full access: '))

    def set_NumOfCop(self):
        self.__num_of_copies -= 1

    def get_book(self, holder):
        if self.__num_of_copies >= 1:
            self.set_NumOfCop()
            self.__holder.append(holder)

    def set_NewHolder(self, name1, name2):
        if (name1 != name2) and (name2 not in self.__holder):
            self.__holder[self.__holder.index(name1)] = name2


book1 = Library('William Shakespeare', 'Romeo and Juliet', 3)
book1.get_book('Sam White')
book1.get_book('Eva Green')
book1.get_info()
book1.set_NewHolder('Eva Green', 'George')
book1.get_info()
