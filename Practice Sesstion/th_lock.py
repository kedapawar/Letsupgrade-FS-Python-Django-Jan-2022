import threading 

lock = threading.Lock()
deposit = 100

def add_profit(): 
    global deposit
    lock.acquire()
    deposit = deposit + 10
    lock.release()

def pay_bill(): 
    global deposit
    lock.acquire()
    deposit = deposit - 10
    lock.release()

thread1 = threading.Thread(target = add_profit, args = ())
thread2 = threading.Thread(target = pay_bill, args = ())

thread1.start() 
thread2.start() 

thread1.join()
thread2.join()

print(deposit)