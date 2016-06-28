import threading

class Sum:

    def __init__(self, nb_threads, numbers):
        if type(nb_threads) != int:
            raise Exception("nb_threads is not an integer")
        if type(numbers) != [int]:
            raise Exception("numbers is not an array of integers")

    def isComputing(self):

    def __str__(self):


class SumThread(threading.Thread):

    def __init__(self, numbers):
        if type(numbers) != [int]:
            raise Exception("numbers is not an array of integers")

    def run(self):
