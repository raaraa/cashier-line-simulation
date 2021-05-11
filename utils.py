import sys
from registerUtils import RegisterUtils
from collections import deque
from register import Register
from customer import Customer

def createCustomer(line):
    customer_type, arrival_time, items = line.split(' ')
    return Customer(customer_type, int(arrival_time.strip()), int(items))

def parseFile():
    file_name = sys.argv[1]
    with open(file_name) as f:
        lines = f.readlines()
    return lines

def populateCustomerQueue(data):
    q = deque()
    for line in data:
        customer = createCustomer(line)
        q.append(customer)
    return q

def createRegs(number_of_registers):
    registers_lst = []
    for i in range(int(number_of_registers)):
        registers_lst.append(Register(i))
    return RegisterUtils(registers_lst)

def calculateTime(reg_obj: RegisterUtils, customer_q):
    time = 1
    while customer_q or reg_obj.registerHasCustomer():
        customer_list = getCustomersAtCurrentTime(time, customer_q)
        reg_obj.assignCustomersToRegister(customer_list)
        reg_obj.checkOut()
        time += 1
    return time

def getCustomersAtCurrentTime(time, customer_q: deque):
    customer_list = []
    while customer_q and customer_q[0].arrival_time == time:
        customer_list.append(customer_q.popleft())
    return sorted(customer_list)