import threading

class OrderedArray:

    list = []

    def __init__(self):
        pass

    def add(self, number):
        if type(number) != int:
            raise Exception("number is not an integer")
        order_array_thread = OrderedArrayThread(number)
        order_array_thread.start()

    def isSorting(self):
        if OrderedArrayThread.total_count > OrderedArrayThread.complete_count:
            return True
        return False

    def __str__(self):
        list_string = "[" + ', '.join(str(x) for x in OrderedArray.list) + "]"
        return list_string

class OrderedArrayThread(threading.Thread):

    total_count = 0
    complete_count = 0

    def __init__(self, number):
        threading.Thread.__init__(self)
        OrderedArrayThread.total_count += 1
        if type(number) != int:
            raise Exception("number is not an integer")
        self.__number = number

    def run(self):
        i = 0
        while i < len(OrderedArray.list) and self.__number > OrderedArray.list[i]:
            i += 1
        OrderedArray.list.insert(i, self.__number)
        OrderedArrayThread.complete_count += 1
