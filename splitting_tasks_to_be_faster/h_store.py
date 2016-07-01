import time
import random
import threading

class Store:

    def __init__(self, item_number, person_capacity):
        self.__item_number = item_number
        self.__capacity = threading.Semaphore(person_capacity)

    def enter(self):
        self.__capacity.acquire()

    def buy(self):
        n = random.sample(range(5,11), 1)[0]
        time.sleep(n)
        if self.__item_number > 0:
            self.__item_number -= 1
            self.__capacity.release()
            return True
        else:
            self.__capacity.release()
            return False
