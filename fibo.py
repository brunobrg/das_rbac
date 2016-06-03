class Fibonacci:

    def fibo():
        x, y = 1, 1
        while True:
            yield x
            x, y = y, x + y
