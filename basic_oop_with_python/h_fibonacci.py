''' Prints the fibonacci number at the given index with the sequence starting at one '''
def fibonacci(index):
    i = 2
    a = 1
    b = 1
    if index == 1:
        return a
    elif index == 2:
        return b
    else:
        while i < index:
            c = a + b
            a = b
            b = c
            i += 1
        return c

