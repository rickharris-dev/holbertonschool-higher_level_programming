import threading

class FibonacciThread(threading.Thread):

    def __init__(self, number):
        threading.Thread.__init__(self)
        if type(number) != int:
            raise Exception("number is not an integer")
        self.__number = number

    def run(self):
        a = 1
        b = 1
        i = 2
        if self.__number == 0:
            result = a
        elif self.__number == 1:
            result = b
        else:
            while i < self.__number:
                c = a + b
                a = b
                b = c
                i += 1
            result = b
        print str(self.__number) + " => " + str(result)
