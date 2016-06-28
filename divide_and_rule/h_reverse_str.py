import threading

class ReverseStrThread(threading.Thread):

    sentence = ""
    total_count = 0
    current_count = 0

    def __init__(self, word):
        threading.Thread.__init__(self)
        self.__order = ReverseStrThread.total_count
        ReverseStrThread.total_count += 1
        if type(word) != str:
            raise Exception("word is not a string")
        self.__word = word[::-1] + " "

    def run(self):
        while ReverseStrThread.current_count < self.__order:
            pass
        ReverseStrThread.sentence += self.__word
        ReverseStrThread.current_count += 1
