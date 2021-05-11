from collections import deque

class Register(object):

    def __init__(self, register_number):
        self.register_number = register_number
        self.customers_queue = deque()

    def __lt__(self, other):
        if len(self.customers_queue) < len(other.customers_queue):
            return len(self.customers_queue) < len(other.customers_queue)
        elif len(self.customers_queue) > len(other.customers_queue):
            return len(self.customers_queue) > len(other.customers_queue)
        return self.register_number < other.register_number