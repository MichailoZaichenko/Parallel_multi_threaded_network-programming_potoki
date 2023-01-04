import threading
import random
l1 = threading.Lock()
sm = threading.Semaphore(3)
list1 = []

def task1():
    global l1
    global list1
    l1.acquire()
    for i in range(10):
        n = random.randint(1,10000)
        list1.append(n)
    print(f"Список: {list1} \n")
    l1.release()


def task2():
    global l1
    global list1
    while l1.locked():
        pass
    summ = sum(list1)
    print(f"Сумма: {summ}\n")

def task3():
    global l1
    global list1
    while l1.locked():
        pass
    aver = sum(list1)/len(list1)
    print(f"Среднее: {aver}\n")


th1 = threading.Thread(target=task1)
th2 = threading.Thread(target=task2)
th3 = threading.Thread(target=task3)

th1.start()
th1.join()

th2.start()
th3.start()
th2.join()
th3.join()