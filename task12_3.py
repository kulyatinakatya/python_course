class MedicalCard:
    def __init__(self, surname, health_group):
        self.surname = surname
        self.__health_group = health_group

    def __get_info(self):
        return self.__health_group

    def doctor(self):
        if self.__get_info() == 1:
            print('Dr.Ivanov')
        if self.__get_info() == 2:
            print('Dr.Stepanov')
        if self.__get_info() == 3:
            print('Dr.Ryazanov')


Alex = MedicalCard('Sergeeva', 2)
#Alex.__get_info()
Alex.doctor()


