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

    def get_book(self, holder):
        if self.__num_of_copies >= 1:
            self.__num_of_copies -= 1
            self.__holder.append(holder)


book1 = Library('William Shakespeare', 'Romeo and Juliet', 3)
book1.get_book('Sam White')
book1.get_book('Eva Green')
book1.get_info()
