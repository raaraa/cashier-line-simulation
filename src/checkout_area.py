from register import Register
from collections import deque


class CheckoutArea(object):

    def __init__(self, register_list):
        self.register_list = register_list

    def get_register_by_shortest_line_size(self) -> Register:
        """
        Gets the register with the shortest line (fewest number of customers in line).
        """
        return sorted(self.register_list)[0]

    def get_register_by_least_number_of_items(self) -> Register:
        """
        Gets register with the customer that has the fewest number of items left to checkout.
        """
        min_items, return_register = float('inf'), None
        for register in self.register_list:
            if not len(register.customers_queue):
                return register
            last_customer = register.customers_queue[-1]
            if last_customer.items < min_items:
                return_register = register
                min_items = last_customer.items
        return return_register

    def assign_customers_to_register(self, customer_list: list) -> None:
        """
        Adds customers to correct register objects queue of customers.

        :param customer_list: list of customer/customers at the current time.
        """
        for customer in customer_list:
            if customer.type == 'A':
                register_shortest_line = self.get_register_by_shortest_line_size()
                register_shortest_line.customers_queue.append(customer)
            elif customer.type == 'B':
                register_least_items = self.get_register_by_least_number_of_items()
                register_least_items.customers_queue.append(customer)
            else:
                raise Exception('File contains incorrect type of customer class.')

    def check_out(self):
        """
        Logic to checkout customer items for every register.
        """
        for register in self.register_list:
            if self.is_training_register(register):
                self.training_register_checkout(register.customers_queue)
            else:
                self.regular_register_checkout(register.customers_queue)

    def is_training_register(self, register: Register) -> bool:
        """
        Checks if the current register is a training register.

        :param register: register to check status of
        """
        return register.register_number == len(self.register_list) - 1

    def register_has_customer(self) -> bool:
        """
        Checks to see if any register is still servicing a customer.
        """
        for register in self.register_list:
            if len(register.customers_queue):
                return True
        return False

    @staticmethod
    def training_register_checkout(register_customer_q: deque):
        """
        Logic to simulate a trainee register.

        :param register_customer_q: queue of customers for register
        """
        if not register_customer_q:
            return
        customer = register_customer_q[0]
        if customer:
            customer.items -= (1 / 2)
            if customer.items == 0:
                register_customer_q.popleft()

    @staticmethod
    def regular_register_checkout(register_customer_q: deque):
        """
        Logic to simulate a regular register.

        :param register_customer_q: queue of customers for register
        """
        if not register_customer_q:
            return
        customer = register_customer_q[0]
        if customer:
            customer.items -= 1
            if customer.items == 0:
                register_customer_q.popleft()
