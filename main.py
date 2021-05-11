from utils import parseFile, createRegs, populateCustomerQueue, calculateTime

if __name__ == '__main__':
    data = parseFile()
    num_of_registers, cust = data[0], data[1:]

    reg_obj = createRegs(num_of_registers)
    cust_q = populateCustomerQueue(cust)

    total_time = calculateTime(reg_obj, cust_q)
    print('Finished at: t=%s minutes' %total_time)