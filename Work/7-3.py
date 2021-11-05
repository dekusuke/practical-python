import time

def after(seconds, func):
    time.sleep(seconds)
    func()

def greeting():
    print('Hello Guido')


def add(x, y):
    def do_add():
        print(f'Adding {x} + {y} -> {x+y}')
    return do_add


