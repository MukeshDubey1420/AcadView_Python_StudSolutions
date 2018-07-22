#Threading

import threading
from threading import Thread
import time

#1.
t = threading.current_thread()
name = threading.current_thread().getName()
id = threading.current_thread().ident

print(t,name,id,sep="\n")
print(t,t.getName(),t.ident,sep="\n")






#2.
def display():
    print("Child Thread:",threading.current_thread())

t = Thread(target=display)
t.setName("MyThread")
t.start()

print("Main thread executing:",threading.currentThread())








#3.
def display():
    for x in range(10):
        print(threading.current_thread().getName(),": Hello World!")

t = Thread(target=display)
t.start()

print("Main thread executing:",threading.currentThread())






#3.1
def display(n):
    for x in range(n):
        print(threading.current_thread().getName(),": Hello World!")
n=5
t = Thread(target=display,args=(n,))
t.start()

print("Main thread executing:",threading.currentThread())








#4.
def display():
    for x in range(10):
        print(threading.current_thread().getName(),":",x)
        time.sleep(1)

t = Thread(target=display)
t.start()

for x in range(10):
    print(threading.current_thread().getName(), ":", x)
    time.sleep(1)






#5.
class MyThread(Thread):
    def run(self):
        print("Child Thread:",threading.current_thread().getName())

t = MyThread()

t.run()








#6.
class MyThread(Thread):
    def run(self):
        for x in range(10):
            print("Child Thread:", threading.current_thread().getName())
            time.sleep(1)

t = MyThread()

t.start()











#7.
class MyThread(Thread):
    def run(self):
            print("Child Thread:", threading.current_thread().getName())
            print("Active Threads:",threading.active_count())


t = MyThread()
print("Active Threads:",threading.active_count())
t.start()











8.
class MyThread(Thread):
    def run(self):
            print("Child Thread:", threading.current_thread().getName())


t = MyThread()
t.start()

t.join()

print("Child Thread is alive:",t.is_alive())
print("Main Thread is alive:",threading.current_thread().is_alive())











#9.
class MyThread(Thread):
    def run(self):
            print("Starting Thread:", threading.current_thread().getName())
            time.sleep(2)
            print("Ending Thread:", threading.current_thread().getName())


t1 = MyThread()
t2 = MyThread()
t3 = MyThread()

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("Child Thread is alive:",t1.is_alive())
print("Child Thread is alive:",t2.is_alive())
print("Child Thread is alive:",t3.is_alive())
print("Main Thread is alive:",threading.current_thread().is_alive())










#10.
def double(num):
    for x in num:
        time.sleep(1)
        print("Double:",2*x)

def square(num):
    for x in num:
        time.sleep(1)
        print("Square:",x*x)


n = [1,2,3,4,5]

bt = time.time()

square(n)
double(n)

et = time.time()

print("Time taken:",et-bt)










#11.
def double(num):
    for x in num:
        time.sleep(1)
        print("Double:",2*x)

def square(num):
    for x in num:
        time.sleep(1)
        print("Square:",x*x)


n = [1,2,3,4,5]

bt = time.time()

t1 = Thread(target=square,args=(n,))
t2 = Thread(target=double,args=(n,))

t1.start()
t2.start()

t1.join()
t2.join()

et = time.time()

print("Time taken:",et-bt)








#12.
def show(name):
    print("Hello:",end=" ")
    time.sleep(2)
    print(name)




t1 = Thread(target=show,args=("abc",))
t2 = Thread(target=show,args=("def",))
t3 = Thread(target=show,args=("ghi",))

t1.start()
t2.start()
t3.start()




#13.
l = threading.Lock()
def show(name):
    l.acquire()
    print("Hello:",end=" ")
    time.sleep(2)
    print(name)
    l.release()


t1 = Thread(target=show,args=("abc",))
t2 = Thread(target=show,args=("def",))
t3 = Thread(target=show,args=("ghi",))

t1.start()
t2.start()
t3.start()