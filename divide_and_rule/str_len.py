import threading
from sys import argv

total_str_length = 0

class StrLenThread(threading.Thread):

    def __init__(self, word):
        threading.Thread.__init__(self)
        if type(word) != str:
            raise Exception("word is not a string")
        self.__word = word

    def run(self):
        global total_str_length
        total_str_length += len(self.__word)

if __name__ == "__main__":
    if len(argv) != 2 or type(argv[1]) != str:
        raise Exception("Program takes one string argument")

    words = argv[1].split(" ")
    str_length_threads = []

    total_str_length = len(words) - 1
    for word in words:
        str_length_thread = StrLenThread(word)
        str_length_threads += [str_length_thread]
        str_length_thread.start()

    for t in str_length_threads:
        t.join()

    print "%d" % total_str_length
