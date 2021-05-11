import sys
from grocery_utils import parse_file, create_checkout_area, populate_customer_queue, calculate_time


def grocery_simulator(file_name):
    data = parse_file(file_name)
    num_of_registers, customer_data = int(data[0]), data[1:]

    checkout_area = create_checkout_area(num_of_registers)
    customer_q = populate_customer_queue(customer_data)

    total_time = calculate_time(checkout_area, customer_q)
    return 'Finished at: t=%s minutes' % total_time


if __name__ == '__main__':
    print(grocery_simulator(sys.argv[1]))
