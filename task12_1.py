class PersonalInfo:
    def __init__(self, name, date, number):
        self.name = name
        self._dateofbirth = date
        self.__phonenumber = number


Mary = PersonalInfo('Mary', '04/06/2011', '+79129243846')

print(Mary.name)
print(Mary._dateofbirth)
print(Mary.__phonenumber)
