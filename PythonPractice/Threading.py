import threading

def my_Function():
    print("Running my Function")

# craete a thread
t = threading.Thread(target=my_Function)
# starting the thread
t.start()

print("Main Thread is Running")



# runnig function with arguments
def my_Function(arg1, arg2):
    print("Running my Function with arguments: ", arg1, arg2 )

# craete a thread
t = threading.Thread(target=my_Function, args=(1,2))
# starting the thread
t.daemon= True
t.start()

# if waiting for thread to complete
t.join()

print("Main Thread has complete")


# METHOD 1
print("# METHOD 1")
# Threas Synchronisation (lock and samphore)
import time

lock = threading.Lock()
def task1():
    lock.acquire()
    print("task 1 has started...")
    time.sleep(3)
    print("task 1 has completed...")
    # to release lock
    lock.release()
    
    
def task2():
    lock.acquire()
    print("task 2 has started...")
    time.sleep(5)
    print("task 2 has completed...")
    # to release lock
    lock.release()
    
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()

print("All tasks are completed")


# METHOD 2
print("# METHOD 2")
# samphore allow multiple thread to access share resources
# prevent over using of resourses

semaphore = threading.Semaphore(2)  # by passing value we can decide how many thread can run at a time
def task1():
    semaphore.acquire()
    print("task 1 has started...")
    time.sleep(3)
    print("task 1 has completed...")
    # to release semaphore
    semaphore.release()
    
    
def task2():
    semaphore.acquire()
    print("task 2 has started...")
    time.sleep(5)
    print("task 2 has completed...")
    # to release semaphore
    semaphore.release()
    
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()

print("All tasks are completed")    


# METHOD 3
print("# METHOD 3")
# multitasking in thread
def task1():
    print("task 1 has started...")
    time.sleep(3)
    print("task 1 has completed...")
    
    
def task2():
    print("task 2 has started...")
    time.sleep(5)
    print("task 2 has completed...")
   
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()

print("All tasks are completed") 


# METHOD 4 
print("# METHOD 4")
from concurrent.futures import ThreadPoolExecutor

def task1():
    print("task 1 has started...")
    time.sleep(5)
    print("task 1 has completed...")  
    return "Task1" 
    
def task2():
    print("task 2 has started...")
    time.sleep(2)
    print("task 2 has completed...")
    return "Task2"
# creating thread pool with 2 worker thread
with ThreadPoolExecutor(max_workers=2) as executor:
    task1_future = executor.submit(task1)
    task2_future = executor.submit(task2)
# wait for both task
task1_result = task1_future.result()
task2_result = task2_future.result()
print("All task has completes")



# DeadLock 
import time

lock1 = threading.Lock()
lock2 = threading.Lock()
def task1():
    lock1.acquire()
    print("task 1 acquire lock1...")
    lock2.acquire()
    print("task 1 acquire lock2...")
    
    time.sleep(3)
    print("task 1 has completed...")
    # to release lock
    lock1.release()
    lock2.release()
    
def task2():
    lock2.release()
    print("task 2 acquire lock2...")
    lock1.acquire()
    print("task 2 acquire lock1...")  
    print("task 2 has started...")
    time.sleep(5)
    print("task 2 has completed...")
    # to release lock
    lock1.release()
    lock2.release()
    
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()

print("All tasks are completed")


# threading Communication

# condition variable
condition = threading.Condition()

def my_func():
    with condition:
        print("thread is waiting for signal")
        condition.wait()
        print("Thread recieved signal")
        
t = threading.Thread(target=my_func)
t.start()

with condition:
    print("Sending signals")
    condition.notify()
t.join()


# creating thread with Queue
import queue
q = queue.Queue()

def my_func():
    while True:
        data = q.get()
        print(f"thread received data {data}")
        q.task_done()
        
t = threading.Thread(target=my_func)
t.start()

q.put("Hello")
q.put("World")
t.join()



# Daemon Thread

def my_func():
    while True:
        print("Daemon thread running")
        time.sleep(3)
        
t = threading.Thread(target=my_func)
t.daemon = True
t.start()
t.join()


def print_cube(num):
    print("Cube: {}" .format(num * num * num))

def print_square(num):
    print("Square: {}" .format(num * num))

if __name__ =="__main__":
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

t1.start()
t2.start()

t1.join()
t2.join()



def producer(q):
    for i in range(3):
        q.put(i)

def consumer(q):
    while True:
        item = q.get()
if item is None:
    break
print("Processed item:", item)

q = queue.Queue()
t1 = threading.Thread(target=producer, args=(q,))
t2 = threading.Thread(target=consumer, args=(q,))
t1.start()
t2.start()
q.put(None)
t1.join()
t2.join()