class Train:
    def __init__(self, number, time):
        self.number = number
        self.time = time


class Ticket:
    def __init__(self, place, price, train):
        self.place = place
        self.price = price
        self.train = train


class Customer:
    def __init__(self, name):
        self.name = name

    def buy_ticket(self, ticket: Ticket):
        return(self.name + ', вы успешно приобрели билет. Поезд №' + ticket.train.number + ', время отправления '+ ticket.train.time +', место '+ ticket.place +'. Стоимость билета – ' + ticket.price+'руб.')


customer = Customer('Екатерина')
train = Train('547', '11:00')
ticket = Ticket('38', '2000', train)

print(customer.buy_ticket(ticket))