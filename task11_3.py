import time


def find(dic, text):
    for key in dic:
        if text in key:
            return dic[key]
    return None


dic = {
    ('Brown', 'Violet', 'Pink'): 'James Blue',
    ('Yellow', 'Red', 'Orange'): 'Sam White'
    }

time_now = int(time.strftime('%H'))


class Worker:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.working_hours = [8, 18]
        self.access = 1

    def worker_info(self):
        print(self.name, self.surname)

    def access_level(self):
        print('access level -', self.access)

    def whoismymanager(self):
        print(self.name, ', your manager is', find(dic, self.surname))

    def is_at_work(self):
        if (time_now >= self.working_hours[0]) and (time_now <= self.working_hours[1]):
            print(self.name, self.surname, 'should be at work')
        else:
            print('it is not their working hours')


class Manager(Worker):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.working_hours = [10, 18]
        self.access = 2

    def access_level(self):
        super(Manager, self).access_level()

    def is_at_work(self):
        super(Manager, self).is_at_work()


class Boss(Manager):
    
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.working_hours = [12, 16]
        self.access = 3

    def access_level(self):
        super(Boss, self).access_level()

    def is_at_work(self):
        super(Boss, self).is_at_work()


Alex = Worker('Alex', 'Brown')
Alex.worker_info()
Alex.access_level()
Alex.whoismymanager()
Alex.is_at_work()

print('\n')
Sam = Manager('Sam', 'White')
Sam.worker_info()
Sam.access_level()
Sam.is_at_work()

print('\n')
Eva = Boss('Eva', 'Green')
Eva.worker_info()
Eva.access_level()
Eva.is_at_work()