import sys

def fib(n):

    n = int(n)
    if n <= 1:
        return 1

    return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    print(fib(sys.argv[-1]))
