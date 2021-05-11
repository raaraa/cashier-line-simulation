from register import Register

class RegisterUtils(object):

    def __init__(self, register_list):
        self.register_list = register_list

    def getRegisterByShortestLineSize(self) -> Register:
        return sorted(self.register_list)[0]

    def getRegisterByLeastNumberOfItems(self) -> Register:
        min_items, return_register = float('inf'), None
        for register in self.register_list:
            if not len(register.customers_queue):
                return register
            last_customer = register.customers_queue[-1]
            if last_customer.items < min_items:
                return_register = register
                min_items = last_customer.items
        return return_register

    def assignCustomersToRegister(self, customer_list: list):
        for customer in customer_list:
            if customer.type == 'A':
                register_shortest_line = self.getRegisterByShortestLineSize()
                register_shortest_line.customers_queue.append(customer)
            elif customer.type == 'B':
                register_least_items = self.getRegisterByLeastNumberOfItems()
                register_least_items.customers_queue.append(customer)

    def checkOut(self):
        for register in self.register_list:
            register_customer_q = register.customers_queue
            if self.isTrainingRegister(register):
                self.trainingRegisterCheckout(register_customer_q)
            else:
                self.regularRegisterCheckout(register_customer_q)

    def isTrainingRegister(self, register : Register):
        return register.register_number == len(self.register_list) - 1

    def trainingRegisterCheckout(self, register_customer_q):
        if not register_customer_q:
            return
        customer = register_customer_q[0]
        if customer:
            customer.items -= 1 / 2
            if customer.items == 0:
                register_customer_q.popleft()

    def regularRegisterCheckout(self, register_customer_q):
        if not register_customer_q:
            return
        customer = register_customer_q[0]
        if customer:
            customer.items -= 1
            if customer.items == 0:
                register_customer_q.popleft()

    def registerHasCustomer(self):
        for register in self.register_list:
            if len(register.customers_queue):
                return True
        return False