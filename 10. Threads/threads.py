#Using thread
# import _thread
# import time
#
# # Define a function for the thread
# def print_time(threadName,delay):
#     count=0
#     while count < 5:
#         time.sleep(delay)
#         count+=1
#         print("%s: %s"%(threadName,time.ctime(time.time())))
# # Create two threads
# try:
#     _thread.start_new_thread(print_time,("Thread-1",2,))
#     _thread.start_new_thread(print_time,("Thread-2",4,))
# except:
#     print("Error:unable to start thread")
#
# while 1:
#     pass


#Using threading
# import threading
# import time
#
# exitFlag=0
# class myThread(threading.Thread):
#     def __init__(self,threadId,name,counter):
#         threading.Thread.__init__(self)
#         self.threadId=threadId
#         self.name=name
#         self.counter=counter
#     def run(self):
#         print("Starting",self.name)
#         print_me(self.name,5,self.counter)
#         print("Exiting",self.name)
#
# def print_me(threadName,counter,delay):
#     while counter:
#         if exitFlag:
#             threadName.exit()
#         time.sleep(delay)
#         print("%s: %s"%(threadName,time.ctime(time.time())))
#         counter-=1
#
# #Create two threads
# thread1= myThread(1,"Thread-1",1)
# thread2= myThread(2,"Thread-2",2)
#
# #Start new threads
# thread1.start()
# thread2.start()
#
# print("Exiting Main thread")



# import threading

# class PrimeNumber(threading.Thread):
#     def __init__(self, number):
#         threading.Thread.__init__(self)
#         self.Number = number
#
#     def run(self):
#         counter = 2
#         while counter * counter < self.Number:
#             if self.Number % counter == 0:
#                 print("%d is not a prime number, because %d = %d * %d" % (
#                 self.Number, self.Number, counter, self.Number / counter))
#                 return
#             counter += 1
#             print("%d is a prime number" % self.Number)
#
#
# threads = []
# while True:
#     input_var = int(input("number: "))
#     if input_var < 1:
#         break
#
#     thread = PrimeNumber(input_var)
#     threads += [thread]
#     # print(threads)
#     thread.start()
#
# for x in threads:
#     x.join()

# #Synchronizing threads while using critical section
# import threading
# import time
#
# class myThread(threading.Thread):
#     def __init__(self,threadID,name,counter):
#         threading.Thread.__init__(self)
#         self.threadID=threadID
#         self.name=name
#         self.counter=counter
#     def run(self):
#         print("Starting"+self.name)
#         #Get lock to synchronize thread
#         threadLock.acquire()
#         print_me(self.name,self.counter,3)
#         #Free lock to release next thread
#         threadLock.release()
# def print_me(threadName,delay,counter):
#     while counter:
#         time.sleep(delay)
#         print("%s: %s" % (threadName, time.ctime(time.time())))
#         counter-=1
#
# threadLock=threading.Lock()
# threads=[]
#
# thread1= myThread(1,"Thread-1",1)
# thread2= myThread(2,"Thread-2",2)
#
# thread1.start()
# thread2.start()
#
# threads.append(thread1)
# threads.append(thread2)
#
# for t in threads:
#     t.join()
#
# print("Exiting main thread")

#Determining name of current thread
# import threading
# import time
#
# def worker():
#     print(threading.currentThread().getName(),"Starting")
#     time.sleep(2)
#     print(threading.currentThread().getName(),"Exiting")
#
# def my_service():
#     print(threading.currentThread().getName(),"Starting")
#     time.sleep(3)
#     print(threading.currentThread().getName(),"Exiting")
#
# t=threading.Thread(name="my_service",target=my_service)
# w=threading.Thread(name="worker",target=worker)
# w2=threading.Thread(target=worker)
#
#
# t.start()
# w.start()
# w2.start()


#Q1
# import time
# import threading
# from threading import Thread
#
# def sleepMe():
#     print("Thread is sleeping",threading.currentThread().getName())
#     time.sleep(5)
#     print("Thread is awake",threading.currentThread().getName())
#
# t=Thread(target=sleepMe,args=())
# t.start()






