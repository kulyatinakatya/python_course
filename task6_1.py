import time


def time_recursive(a):
    n = int(input('Введите число = '))
    if n >= 0:
        time.sleep(n)
        return time_recursive(n)


a = 1
time_recursive(a)