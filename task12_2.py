class BankAccount:
    def __init__(self, customers_name, account_number, balance, password):
        self.customers_name = customers_name
        self.account_number = account_number
        self.__balance = balance
        self.__password = password

    def get_balance(self, password):
        if password == self.__password:
            print('Ваш баланс:', self.__balance, 'руб.')

    def change_balance(self, password, new_balance):
        if password == self.__password:
            self.__balance = new_balance + self.__balance


Alex = BankAccount('Alex', 547, 150, 'qwerty')
Alex.change_balance(input('Вы хотите изменить балланс, введите пароль: '), int(input('Внесите сумму: ')))
Alex.get_balance(input('Вы хотите узнать балланс, введите пароль: '))
