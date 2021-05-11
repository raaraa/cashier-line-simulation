class Customer(object):

    def __init__(self, type, arrival_time, items):
        self.type = type
        self.arrival_time = arrival_time
        self.items = items

    def __lt__(self, other):
        if self.items < other.items:
            return self.items < other.items
        elif self.items > other.items:
            return other.items > self.items
        else:
            return self.type < other.type
