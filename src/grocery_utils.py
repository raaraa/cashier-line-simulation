from collections import deque

from checkout_area import CheckoutArea
from customer import Customer
from register import Register


def parse_file(file_name: str) -> list:
    """
    Parses input file.

    :param file_name:
    :return: list containing all the data in the input file separated by line
    """
    with open(file_name) as f:
        lines = f.readlines()
    return lines


def populate_customer_queue(customer_data: list) -> deque:
    """
    Create main queue of all the customers.

    :param customer_data: data to create a customer from the input file
    :return: queue containing all the customers
    """
    q = deque()
    for line in customer_data:
        customer = create_customer(line)
        q.append(customer)
    return q


def create_customer(line) -> Customer:
    """
    Creates customer object from parsed line of data.

    :param line: single line of data from the input file
    :return: customer object
    """
    customer_type, arrival_time, items = line.split(' ')
    return Customer(customer_type, int(arrival_time.strip()), int(items))


def create_checkout_area(number_of_registers) -> CheckoutArea:
    """
    Creates checkout area by a list of register objects

    :param number_of_registers: number parsed from the input file.
    :return: checkout area that contains a list of all the registers.
    """
    registers_lst = []
    for i in range(number_of_registers):
        registers_lst.append(Register(i))
    return CheckoutArea(registers_lst)


def get_customers_at_current_time(time: int, customer_q: deque) -> list:
    """
    Gets all the customers at the current time t. If multiple customers at the same time,
    sorts them based off the problem constraints.

    :param time: current time interval
    :param customer_q: main customer queue
    :return: sorted list of customers at the current time interval
    """
    customer_list = []
    while customer_q and customer_q[0].arrival_time == time:
        customer_list.append(customer_q.popleft())
    return sorted(customer_list)


def calculate_time(checkout_area: CheckoutArea, customer_q: deque) -> int:
    """
    Calculates time taken to service all the customers in the queue.

    :param checkout_area:
    :param customer_q: main queue with all the customers
    :return: total time taken to service all customers
    """
    time = 1
    while customer_q or checkout_area.register_has_customer():
        customer_list = get_customers_at_current_time(time, customer_q)
        checkout_area.assign_customers_to_register(customer_list)
        checkout_area.check_out()
        time += 1
    return time
